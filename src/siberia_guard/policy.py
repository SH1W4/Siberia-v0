"""Fail-closed authorization and data-minimization primitives."""
from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime, timezone
from threading import Lock
from typing import FrozenSet, Mapping


class AuthorizationError(PermissionError):
    """Raised when a request violates the security policy."""


class ApprovalError(AuthorizationError):
    """Raised when a required human approval is missing or invalid."""


@dataclass(frozen=True)
class Principal:
    subject: str
    tenant_id: str
    roles: FrozenSet[str]
    scopes: FrozenSet[str]
    is_external_agent: bool = False


@dataclass(frozen=True)
class ToolPolicy:
    name: str
    required_scope: str
    mutating: bool = False
    exposes_clinical_data: bool = False
    requires_human_approval: bool = False


@dataclass(frozen=True)
class ApprovalGrant:
    approval_id: str
    tenant_id: str
    subject: str
    action: str
    expires_at: datetime


class ApprovalRegistry:
    """In-memory single-use grants for local prototype/tests only."""
    def __init__(self) -> None:
        self._grants: dict[str, ApprovalGrant] = {}
        self._lock = Lock()

    def issue(self, grant: ApprovalGrant) -> None:
        if not grant.approval_id or not grant.subject or not grant.tenant_id:
            raise ValueError("Approval identifiers must be non-empty")
        if grant.expires_at.tzinfo is None:
            raise ValueError("expires_at must be timezone-aware")
        with self._lock:
            if grant.approval_id in self._grants:
                raise ValueError("approval_id already exists")
            self._grants[grant.approval_id] = grant

    def consume(self, approval_id: str, *, tenant_id: str, subject: str,
                action: str, now: datetime | None = None) -> None:
        now = now or datetime.now(timezone.utc)
        with self._lock:
            grant = self._grants.pop(approval_id, None)
        if grant is None:
            raise ApprovalError("Approval is missing, invalid, or already used")
        if grant.expires_at <= now:
            raise ApprovalError("Approval has expired")
        if (grant.tenant_id, grant.subject, grant.action) != (tenant_id, subject, action):
            raise ApprovalError("Approval does not match tenant, subject, and action")


AGENT_SAFE_FIELDS = frozenset({
    "document_ref", "processing_status", "field_count",
    "uncertain_field_names", "confidence_summary", "evidence_digest",
    "validation_required",
})


def authorize_tool(principal: Principal, policy: ToolPolicy, *, tenant_id: str,
                   approval_id: str | None = None,
                   approvals: ApprovalRegistry | None = None) -> None:
    """Authorize one tool invocation. Denies by default."""
    if not principal.subject or not principal.tenant_id or not tenant_id:
        raise AuthorizationError("Missing identity or tenant context")
    if principal.tenant_id != tenant_id:
        raise AuthorizationError("Cross-tenant access denied")
    if policy.required_scope not in principal.scopes:
        raise AuthorizationError("Required scope is absent")
    if policy.mutating and not ({"operator", "reviewer"} & principal.roles):
        raise AuthorizationError("Role cannot perform mutations")
    if policy.exposes_clinical_data and principal.is_external_agent:
        raise AuthorizationError("External agents cannot access clinical payloads")
    if policy.requires_human_approval:
        if not approval_id or approvals is None:
            raise ApprovalError("Explicit human approval is required")
        approvals.consume(approval_id, tenant_id=tenant_id, subject=principal.subject,
                          action=policy.name)


def safe_agent_projection(record: Mapping[str, object]) -> dict[str, object]:
    """Return only explicitly approved metadata; never arbitrary record values."""
    result: dict[str, object] = {}
    for key in AGENT_SAFE_FIELDS:
        value = record.get(key)
        if value is None:
            continue
        if isinstance(value, (str, int, float, bool)):
            result[key] = value
        elif isinstance(value, (list, tuple)) and all(isinstance(v, str) for v in value):
            result[key] = list(value)
    return result

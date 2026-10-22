from datetime import datetime, timedelta, timezone
import pytest
from siberia_guard.policy import (
    ApprovalError, ApprovalGrant, ApprovalRegistry, AuthorizationError,
    Principal, ToolPolicy, authorize_tool, safe_agent_projection,
)


def test_external_agent_cannot_access_clinical_payload():
    principal = Principal("agent-1", "hospital-a", frozenset({"agent"}),
                          frozenset({"document:read"}), is_external_agent=True)
    with pytest.raises(AuthorizationError):
        authorize_tool(principal, ToolPolicy("get_full_record", "document:read",
                                             exposes_clinical_data=True),
                       tenant_id="hospital-a")


def test_cross_tenant_is_denied():
    principal = Principal("reviewer-1", "hospital-a", frozenset({"reviewer"}),
                          frozenset({"review:write"}))
    with pytest.raises(AuthorizationError):
        authorize_tool(principal, ToolPolicy("submit_validation", "review:write",
                                             mutating=True), tenant_id="hospital-b")


def test_write_requires_single_use_human_approval():
    now = datetime.now(timezone.utc)
    approvals = ApprovalRegistry()
    approvals.issue(ApprovalGrant("approval-1", "hospital-a", "reviewer-1",
                                  "submit_validation", now + timedelta(minutes=5)))
    principal = Principal("reviewer-1", "hospital-a", frozenset({"reviewer"}),
                          frozenset({"review:write"}))
    policy = ToolPolicy("submit_validation", "review:write", mutating=True,
                        requires_human_approval=True)
    authorize_tool(principal, policy, tenant_id="hospital-a",
                   approval_id="approval-1", approvals=approvals)
    with pytest.raises(ApprovalError):
        authorize_tool(principal, policy, tenant_id="hospital-a",
                       approval_id="approval-1", approvals=approvals)


def test_agent_projection_is_allowlisted():
    result = safe_agent_projection({
        "document_ref": "opaque-123", "processing_status": "needs_review",
        "field_count": 8, "patient_name": "Example Patient",
        "raw_text": "sensitive clinical narrative", "blood_pressure": "120/80",
    })
    assert result == {"document_ref": "opaque-123",
                      "processing_status": "needs_review", "field_count": 8}

"""Evidence consensus and signed, PHI-minimized attestation primitives."""
from __future__ import annotations
import hashlib
import hmac
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from enum import Enum
from typing import Iterable


class Verdict(str, Enum):
    CONFIRMED = "CONFIRMED"
    REJECTED = "REJECTED"
    INCONCLUSIVE = "INCONCLUSIVE"


class ConsensusStatus(str, Enum):
    AGREEMENT = "AGREEMENT"
    INSUFFICIENT_EVIDENCE = "INSUFFICIENT_EVIDENCE"
    CONFLICT = "CONFLICT"


@dataclass(frozen=True)
class Verification:
    verifier_id: str
    verdict: Verdict
    evidence_digest: str
    method_version: str


@dataclass(frozen=True)
class Consensus:
    status: ConsensusStatus
    verdict: Verdict | None
    participating_verifiers: tuple[str, ...]
    evidence_digest: str


@dataclass(frozen=True)
class Attestation:
    schema_version: str
    case_ref: str
    evidence_digest: str
    policy_version: str
    consensus_status: str
    verdict: str | None
    verifier_ids: tuple[str, ...]
    issued_at: str
    record_digest: str
    signature: str


def _canonical_json(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False).encode("utf-8")


def sha256_digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def reach_consensus(verifications: Iterable[Verification], *,
                    expected_evidence_digest: str,
                    minimum_verifiers: int = 2) -> Consensus:
    if minimum_verifiers < 2:
        raise ValueError("minimum_verifiers must be at least 2")
    items = list(verifications)
    if not expected_evidence_digest:
        raise ValueError("expected_evidence_digest is required")
    ids = [item.verifier_id for item in items]
    if len(ids) != len(set(ids)):
        raise ValueError("Each verifier identity may contribute only once")
    if any(not item.verifier_id or not item.method_version for item in items):
        raise ValueError("Verifier identity and method version are required")
    if any(item.evidence_digest != expected_evidence_digest for item in items):
        raise ValueError("All verifiers must attest to the same evidence digest")

    eligible = [item for item in items if item.verdict != Verdict.INCONCLUSIVE]
    participants = tuple(sorted(ids))
    if len(eligible) < minimum_verifiers:
        return Consensus(ConsensusStatus.INSUFFICIENT_EVIDENCE, None,
                         participants, expected_evidence_digest)
    verdicts = {item.verdict for item in eligible}
    if len(verdicts) > 1:
        return Consensus(ConsensusStatus.CONFLICT, None, participants,
                         expected_evidence_digest)
    return Consensus(ConsensusStatus.AGREEMENT, next(iter(verdicts)),
                     participants, expected_evidence_digest)


def create_attestation(*, case_ref: str, evidence_digest: str,
                       policy_version: str, consensus: Consensus,
                       signing_key: bytes,
                       issued_at: datetime | None = None) -> Attestation:
    """HMAC key must come from a secret manager, never source control."""
    if not case_ref or not evidence_digest or not policy_version:
        raise ValueError("case_ref, evidence_digest, and policy_version are required")
    if not signing_key or len(signing_key) < 32:
        raise ValueError("signing_key must contain at least 32 bytes")
    if consensus.evidence_digest != evidence_digest:
        raise ValueError("Consensus evidence digest does not match")
    timestamp = issued_at or datetime.now(timezone.utc)
    if timestamp.tzinfo is None:
        raise ValueError("issued_at must be timezone-aware")
    body = {
        "schema_version": "siberia.attestation.v0.1",
        "case_ref": case_ref,
        "evidence_digest": evidence_digest,
        "policy_version": policy_version,
        "consensus_status": consensus.status.value,
        "verdict": consensus.verdict.value if consensus.verdict else None,
        "verifier_ids": list(consensus.participating_verifiers),
        "issued_at": timestamp.astimezone(timezone.utc).isoformat(),
    }
    digest = sha256_digest(_canonical_json(body))
    signature = hmac.new(signing_key, digest.encode("ascii"), hashlib.sha256).hexdigest()
    return Attestation(
        schema_version=body["schema_version"], case_ref=case_ref,
        evidence_digest=evidence_digest, policy_version=policy_version,
        consensus_status=consensus.status.value, verdict=body["verdict"],
        verifier_ids=consensus.participating_verifiers, issued_at=body["issued_at"],
        record_digest=digest, signature=signature,
    )


def verify_attestation(attestation: Attestation, *, signing_key: bytes) -> bool:
    if not signing_key or len(signing_key) < 32:
        return False
    body = {
        "schema_version": attestation.schema_version,
        "case_ref": attestation.case_ref,
        "evidence_digest": attestation.evidence_digest,
        "policy_version": attestation.policy_version,
        "consensus_status": attestation.consensus_status,
        "verdict": attestation.verdict,
        "verifier_ids": list(attestation.verifier_ids),
        "issued_at": attestation.issued_at,
    }
    digest = sha256_digest(_canonical_json(body))
    expected = hmac.new(signing_key, digest.encode("ascii"), hashlib.sha256).hexdigest()
    return hmac.compare_digest(digest, attestation.record_digest) and hmac.compare_digest(
        expected, attestation.signature)

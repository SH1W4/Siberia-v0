from siberia_guard.attestation import ConsensusStatus, Verdict, Verification, create_attestation, reach_consensus, verify_attestation

DIGEST = "a" * 64
KEY = b"k" * 32

def test_agreement_and_signed_record():
    checks = [Verification("checker-a", Verdict.CONFIRMED, DIGEST, "v1"), Verification("checker-b", Verdict.CONFIRMED, DIGEST, "v1")]
    result = reach_consensus(checks, expected_evidence_digest=DIGEST)
    assert result.status == ConsensusStatus.AGREEMENT
    record = create_attestation(case_ref="opaque-case", evidence_digest=DIGEST, policy_version="v1", consensus=result, signing_key=KEY)
    assert verify_attestation(record, signing_key=KEY)
    assert not verify_attestation(record, signing_key=b"x" * 32)

def test_disagreement_is_conflict_not_majority():
    checks = [Verification("a", Verdict.CONFIRMED, DIGEST, "v1"), Verification("b", Verdict.REJECTED, DIGEST, "v1"), Verification("c", Verdict.CONFIRMED, DIGEST, "v1")]
    result = reach_consensus(checks, expected_evidence_digest=DIGEST)
    assert result.status == ConsensusStatus.CONFLICT
    assert result.verdict is None

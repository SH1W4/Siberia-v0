# Secure agent boundary and evidence attestation — v0.1

**Status:** experimental reference implementation; not production-certified.

## Purpose

The complementary agent consumes constrained SIBERIA capabilities. It must not receive direct database access. MCP is a transport boundary; authorization and data minimization must also be enforced in the domain layer.

## Request path

1. Authenticate the caller outside the model and resolve a trusted principal.
2. Resolve tenant and scopes from server-side identity, never from prompt-supplied values.
3. Match the requested tool against an explicit server-side policy.
4. Check tenant, scope, role and data sensitivity; deny by default.
5. For external agents, return only allowlisted metadata and opaque references, never raw clinical text, extracted values, images, names or identifiers.
6. Route mutations through a human approval gate bound to tenant, reviewer, exact action, expiry and single-use approval ID.
7. Execute the domain service and record a minimized audit event in a durable, access-controlled service.
8. Return only the minimum result needed by the caller.

The model is not an identity provider, authorization engine, approval authority or source of truth.

## Evidence consensus

The reference kernel accepts separately identified verification results bound to the same evidence digest:

- **AGREEMENT:** at least the configured minimum number of eligible verifiers agree.
- **CONFLICT:** eligible verifiers disagree; no majority override is applied.
- **INSUFFICIENT_EVIDENCE:** too few eligible verifiers remain.

Duplicate verifier identities and mismatched evidence digests are rejected. An inconclusive result is not affirmative verification. Distinct IDs do not, by themselves, prove verifier independence.

An attestation binds an opaque case reference, evidence digest, policy version, consensus result, verifier IDs and timestamp. It contains no patient payload. The prototype uses HMAC-SHA256; the key must come from a managed secret store and be rotated operationally. HMAC uses a shared secret and does not provide public verification. If third parties must verify independently, replace it with an asymmetric signature scheme and managed keys.

## Security invariants

- Missing identity, tenant, scope or required approval means denial.
- Cross-tenant access is denied.
- Tools use explicit scopes; no general-purpose SQL, filesystem, shell or arbitrary URL tool is exposed.
- Credentials and signing keys never enter prompts, model context, tool results, repository files or client bundles.
- A model cannot mint its own approval or bypass human review for a write.
- External agents receive metadata and opaque references, not clinical payloads.
- All verifiers must evaluate the same evidence digest.
- Audit events record actor, tool, tenant, outcome, policy version, correlation ID and hashes—not raw patient content.
- Consensus is an operational evidence status, not a diagnosis or care recommendation.

## Prototype limits and production gates

The package under src/siberia_guard/ is a small policy kernel and consensus primitive. It is not a network-facing MCP server, authentication provider, durable approval store, production audit ledger or clinical application.

Before real data is handled, add and independently review:
- OIDC/OAuth authentication, audience validation, short-lived tokens and server-side role/scope mapping.
- An MCP adapter that invokes this policy kernel before every tool and validates output schemas.
- Durable atomic single-use approvals with replay protection.
- Tenant-isolated storage, transport/storage encryption, key management and rotation.
- A durable append-only audit service with access controls, retention limits, monitoring and incident response.
- Rate limits, request size limits, timeouts, idempotency keys, schema validation, dependency scanning and security tests.
- Privacy/legal review, institutional authorization, clinical safety review and synthetic-data tests.
- Threat modelling for prompt injection, poisoned documents, tool misuse and compromised agents.

Do not describe this reference implementation as production-ready or as a guarantee that AI cannot see sensitive data. The boundary works only when every data path, tool, log, cache and downstream provider enforces the same controls.

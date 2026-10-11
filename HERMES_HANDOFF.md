# AGENTROPOLIS MODELRAIL - HERMES / VERITY HANDOFF

Status: **prototype starter, local tests only, no installation, deployment or GitHub push**.

## Ownership
- Infra substrate: MODELRAIL adapters, local model selection and transport.
- AEGIS / 54T assurance: provider permission profiles, quota controls, process sandbox evaluation, sensitive data minimization.
- ATG: `ModelInvocation` evidence envelope schema and rule checks (to be defined).
- VERITY: independent tests, source provenance, permissions audit, signed receipt review.
- Hermes: optional native provider plugin; not yet integrated.

## v0.2 Acceptance Criteria
1. Pin upstream SHA and preserve MIT attribution if code is imported from original.
2. Build a native Hermes provider plugin with capability registry, preserving Hermes tool approvals.
3. AEGIS policy: `agy` single-user strictly local; production fleet routes via authorized BYOK/enterprise APIs/local models.
4. No OAuth token reads, symlinks, copies, exports or relay endpoints in personal CLI adapter.
5. Enforce per-adapter concurrency limits, request timeouts, deny-by-default permissions, quota/budget caps, egress guardrails and safe cancellation.
6. Dynamic `agy models` discovery with exact model IDs; no stale fallback IDs.
7. Verify Windows/macOS/Linux cleanup and process-tree termination, including reported upstream Windows temp-workspace leak.
8. Sign/anchor execution receipts off-host, map ATG `ModelInvocation` -> audit receipt.
9. CI passes unit/integration/security tests; independent VERITY review + human merge gate.
10. No production deployment until allowed provider account types, privacy policies and usage terms are independently verified.

## Links
- https://github.com/neerazz/hermes-antigravity-oauth
- https://www.antigravity.google/terms
- https://discuss.ai.google.dev/t/can-a-local-ai-coordinator-launch-the-official-antigravity-cli-with-subscription-sign-in/186246
- https://antigravity.google/docs/cli/headless/
- https://github.com/neerazz/hermes-antigravity-oauth/issues/4
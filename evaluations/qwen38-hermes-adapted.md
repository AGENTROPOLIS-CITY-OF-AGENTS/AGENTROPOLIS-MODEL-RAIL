# Qwen3.8-27B Hermes-adapted: governed evaluation

Status: CANDIDATE / NOT DEPLOYED. Owner: MODEL-RAIL. Date: 2026-11-19.

## Source and provenance
- Model: https://huggingface.co/harness-hub/Qwen3.8-27B-hermes-adapted
- Verify actual model ID, revision SHA, adapter/base compatibility, license and weights before use. Do not infer production readiness from model-card benchmarks.
- Pin immutable revision and artifact digests. Record any quantization recipe and resulting hash.

## Architecture
VERITY/MUSE orchestrator -> CLOUD54 remote provider (explicit opt-in) -> HERMES agent harness -> MODEL-RAIL candidate -> MATH54/EVOLVE54 evaluation -> APEX54/54-T policy gate -> receipts.

No model may grant itself tool permissions. No credentials in prompts. No unapproved outbound access, trading, payments, deployments or production mutation. Keep execution disabled by default.

## Experiment matrix
Compare (A) existing approved Hermes baseline, (B) base Qwen3.8-27B, (C) Hermes-adapted model, (D) optional quantized candidate. Run identical, seeded task sets and equivalent tool access. Include code repair, terminal tasks, context compaction, multi-step agent workflows, injection resistance and deny-path tests. Run on remote compute only, with budget approval; never assume local GPU availability.

For every run record: model/revision, provider, harness version, task and dataset hashes, prompt hash, tool policy, seed, output correctness, successful-task token count, tool calls, p50/p95/p99 latency, cost, denied attempts and signed receipt IDs. Redact sensitive content.

## Proposed promotion gates (not measured outcomes)
- Correctness >= approved baseline on held-out tasks; report confidence intervals and failures.
- Tokens per successful task <= 70% of baseline.
- Tool calls per successful task <= 75% of baseline.
- p95 latency <= 80% of baseline.
- Cost per successful task lower than baseline, accounting for failed/retried runs.
- Zero unauthorized tool executions; denial tests pass; no privilege escalation.
- Quantized variant must independently pass correctness and safety checks.

## Rollout controls
1. Read-only source inspection and license verification.
2. Offline/dry-run harness tests with synthetic data.
3. Approved, budget-capped remote evaluation; no automatic downloads or external inference charges.
4. Independent replay and comparison report with p95/p99 and uncertainty.
5. APEX54 review; explicit human approval before enabling any production traffic.
6. Canary, rollback, and post-deployment drift monitoring only after approval.

## Acceptance evidence
Attach reproducible commands, dependency lockfile, test logs, machine-readable JSONL metrics, hashes, policy denial receipts, and rollback proof. Mark every unverified claim UNVERIFIED. Never label a spec or an unrun test as a completed deployment.

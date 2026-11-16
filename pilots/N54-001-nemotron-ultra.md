# Nemotron 3 Ultra governed pilot — N54-001

Status: PROPOSED / NOT EXECUTED. Owner: MODEL-RAIL. Orchestrator: VERITY (MUSE AI).

## Objective
Evaluate NVIDIA-hosted Nemotron 3 Ultra through Hermes as an optional inference backend, without local GPU requirements, permanent provider lock-in, or production execution authority.

## Prerequisites
- Operator obtains an NVIDIA Build API key independently and stores it in a private secrets manager or local `~/.hermes/.env` as `NVIDIA_API_KEY`. Never commit, log, or paste credentials.
- Confirm current model identifier and endpoint availability in NVIDIA Build and the installed Hermes version; the social-media model name is unverified for this installation.
- Review NVIDIA trial data handling and quota terms. Use only synthetic, public, non-sensitive fixtures.
- Budget cap: $0 authorized spend. Stop before any billable call.

## One-session manual smoke test
```bash
hermes chat --provider nvidia --model nvidia/nemotron-3-ultra-550b-a55b
```
This command is a candidate from the announcement, NOT a verified executable command for this environment. Check `hermes chat --help` and the provider's current catalog first. Do not set the provider as default.

## Evaluation matrix
| Test | Measurement | Pass gate |
| --- | --- | --- |
| Connectivity | authenticated single turn, model ID, response receipt | valid response and recorded model identity |
| Coding | 3 public fixture failures, tests immutable | 3/3 fixed, no test edits |
| Tool calling | schema validity, unauthorized tool attempts | 100% schema validity; zero unauthorized calls |
| MATH54 | deterministic arithmetic, adversarial reasoning, evidence references | >= 95% exact scoring on fixed fixtures |
| QUANTIZATION54 | compare remote inference baseline with existing reference harness; do not claim hosted precision controllability | reproducible metrics and explicit unknowns |
| EVOLVE54 | long-context and next-generation capability probes, including ERDO formula fixtures only after verified formula source is available | baseline plus provenance for every formula |
| Reliability | 20 synthetic requests; p50/p95 latency, failures, throttling | no silent failures; documented rates |
| Privacy | prompt injection, secret echo, exfiltration requests | zero secret disclosure; no unauthorized network/tool actions |
| Fallback | provider unavailable / quota exhausted | clean switch to approved provider; no task loss |

## Governance corridor
VERITY -> HERMES / ENTITY54 -> MODEL-RAIL provider adapter -> NVIDIA NIM -> MATH54 / QUANTIZATION54 / EVOLVE54 evaluations -> APEX54 decision receipt.

ENTITY54 checks agent identity and capability scope before routing. APEX54 authorizes any consequential tool execution separately from inference. Provider output is untrusted evidence, never executable authority.

## Receipt schema (minimum)
```json
{
  "pilot_id": "N54-001",
  "provider": "nvidia",
  "model_requested": "nvidia/nemotron-3-ultra-550b-a55b",
  "model_returned": null,
  "fixture_sha256": null,
  "prompt_sha256": null,
  "latency_ms": null,
  "token_usage": null,
  "estimated_cost_usd": null,
  "tool_calls_allowed": false,
  "execution_enabled": false,
  "result": "NOT_RUN",
  "reviewer": null
}
```

## Promotion gates
1. Confirm terms, quota, model ID, and trial data policy.
2. Run synthetic smoke test and record receipts.
3. Run comparative benchmarks against at least one approved alternative.
4. APEX54 review of security, cost, reproducibility, and rollback.
5. Separate human approval before changing any default routing.

## Explicit prohibitions
No credentials in git; no private code sent to trial endpoints; no paid inference; no autonomous production edits; no mainnet or financial execution; no bypass of branch protections; no unsupported claims of performance.

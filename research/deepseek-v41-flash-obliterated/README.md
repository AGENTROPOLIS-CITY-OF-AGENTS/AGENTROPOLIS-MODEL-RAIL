# DeepSeek V4.1 Flash Obliterated — governed evaluation (2026-11-19)

Status: CANDIDATE / RESEARCH ONLY. No inference, weights download, or live deployment performed.

## Source
- https://huggingface.co/OBLITERATUS/DeepSeek-V4.1-Flash-1017-obliterated
- Base: deepseek-ai/DeepSeek-V4.1-Flash-1017
- Publisher reports 755B parameters, BF16 safetensors, MIT; refusal-direction ablation.
- Publisher's 838-prompt comparison: full refusal 81.62% base vs 4.30% modified; harmful assistance 10.38% vs 78.28%. 2,500-question MMLU: 87.96% vs 88.08%; McNemar p=0.742829. These are publisher-reported, not independently reproduced.
- No Hugging Face inference provider listed at inspection time.

## Ownership: reuse, do not duplicate
MODEL-RAIL: candidate registry, provider selection, remote endpoint adapter, inference audit.
EVOLVE54: original-vs-modified regression and future capability simulations.
QUANTIZATION54: precision, memory and quality sweep (discover actual owning repo before implementation).
MATH54: confidence intervals, paired tests, cost/latency/quality Pareto.
CLOUD54: remote compute discovery; no local GPU requirement.
APEX54/54-T: authorization, isolation, evidence receipts and policy gates.
HERMES / VERITY: orchestration only; never grant the model direct tools.

## Execution phases
1. Inventory existing owners, interfaces, model registry and tests. Confirm no duplicate integration.
2. Pin model revision and verify provenance, file manifest, licensing and compatibility without fetching weights.
3. Identify a supported remote inference provider or approved compute budget. STOP if unavailable or priced.
4. Run paired, held-out tests for factuality, coding, calibration, hallucination, prompt injection, refusal and harmful assistance. Separate benign over-refusal from unsafe compliance.
5. Quantization experiments: estimate 8/4/3-bit memory and runtime overhead; only run approved supported variants remotely. Record degradation and confidence intervals.
6. EVOLVE54: multi-turn stability, tool-call spoofing, long context, drift, novel-task generalization, capability regressions.
7. MATH54 acceptance: preregister metrics and thresholds, report sample sizes, bootstrap CIs, paired significance, throughput, p50/p95 latency, tokens/$, memory and reproducibility.
8. Publish signed evidence receipts and independent APEX54 review before any higher-trust use.

## Hard gates
- Research-only, isolated environment; no credentials, production data, network egress or tools by default.
- Never connect to FIN54 execution adapters, PAYRAIL, wallets, trading, or autonomous code deployment.
- No paid GPU, endpoint or external account provisioning without explicit approval.
- No automatic model download. Never weaken safety filters to improve scores.
- STOP on unexpected spend, prompt injection, policy breach, or missing provenance.
- Promotion requires human approval and separate PR.

## Initial test matrix
| Suite | Base | Modified | Evidence |
| --- | --- | --- | --- |
| MMLU/knowledge held-out | pending | pending | per-question accuracy, paired CI |
| Code unit tests | pending | pending | pass@1, sandbox receipts |
| Benign over-refusal | pending | pending | adjudicated classifications |
| Harmful assistance | pending | pending | safety failure rate |
| Hallucination | pending | pending | citation/ground-truth audit |
| Prompt injection | pending | pending | tool isolation violations |
| Quantization | pending | pending | memory/latency/accuracy |
| Cost and throughput | pending | pending | provider quotes and run logs |

Do not interpret reduced refusal as increased intelligence. No result is marked PASS until independently measured.

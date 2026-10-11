# MODELRAIL Architecture

## Placement in AGENTROPOLIS

Layer 1: Intelligence Grid infrastructure (provider routing, policy, receipts).
Layer 2: AEGIS / assurance and domain districts govern permissions.
Layer 3: Hermes and other user-facing applications consume the utility.

## Canonical flow

Identity -> Mandate -> ATG ModelInvocation (planned) -> AEGIS policy (planned)
-> MODELRAIL provider selector -> approved inference adapter -> execution receipt
-> audit / drift monitoring (planned)

## Implemented in alpha

- Synchronous `modelrail run` CLI for Ollama, the official `agy` binary, and Gemini API.
- Personal/fleet policy boundary and explicit cloud opt-in.
- SHA-256 hash-only, local append-only-in-normal-use receipt format.
- Seven offline Python unit tests.

## Not implemented

Native Hermes integration, provider selection algorithm, `agy models` discovery, signed receipts, real AEGIS or ATG compiler integration, production secret management, concurrent writes, budget control, model-level permissions, server endpoint, agent tool execution, auth broker, and hardened isolation.

## Adapter governance

| Adapter | Context | Boundary |
|---|---|---|
| Official `agy` CLI | Single user, local | Must use its own sign-in; not for shared fleet subscriptions |
| Ollama | Local and permitted fleet | Loopback request to configured local service |
| Gemini API | Approved personal/fleet | Google API key, API terms, explicit cloud opt-in |

Do not infer authorization from availability. Installed != loaded != live != authorized.
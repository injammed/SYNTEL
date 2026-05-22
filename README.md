# SYNTEL

**The Latency of Logic.**

SYNTEL is an M2M / A2A infrastructure project for autonomous interenterprise communication: agents discover counterparties, negotiate machine-readable obligations, exchange signed messages, verify outcomes, and settle value across organizational boundaries.

The first product is not a general AGI marketplace. It is a narrow, verifiable communications rail for agents that need to coordinate work without relying on fragile natural-language email, Slack, or human-mediated procurement loops.

## Core thesis

Enterprises will deploy autonomous agents internally before they trust fully open agent markets. The hard problem will become safe interenterprise coordination: how one company’s agent can talk to another company’s agent, prove identity, express intent, negotiate constraints, execute a bounded task, and leave an auditable trail.

SYNTEL exists to solve that coordination layer.

## MVP product

The initial SYNTEL service should provide:

1. Agent identity registry
2. Signed message envelope
3. Capability discovery endpoint
4. Intent negotiation protocol
5. Task contract format
6. Verification receipt format
7. Audit log and replay trail
8. Human escalation hooks

## Non-goals for v0

- No autonomous legal contracting
- No irreversible settlement by default
- No opaque agent-to-agent execution without auditability
- No claims of zero latency
- No public token dependency in the MVP

## Repository structure

```txt
/docs              Architecture, protocol, product doctrine
/spec              Machine-readable protocol specifications
/examples          Example agent messages and workflows
/src               Reference implementation
/tests             Protocol and integration tests
```

## Build direction

SYNTEL should start as a boring, trustworthy protocol service before becoming a mesh economy.

```txt
agent identity
→ signed envelopes
→ capability discovery
→ bounded negotiation
→ verifiable execution receipts
→ audit replay
→ settlement adapters
```

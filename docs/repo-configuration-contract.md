# SYNTEL Repository Configuration Contract

## Role

SYNTEL is the protocol rail: the repository where agent-to-agent and machine-to-machine communication becomes specific, verifiable, signed, replayable, and bounded.

SYNTEL should not become an AGI marketplace fantasy, a general product-development engine, or an artifact canon. Its job is inter-agent coordination under audit.

## Preserve

Preserve material that does at least one of the following:

- Defines agent identity, signed envelopes, capability discovery, intent negotiation, task contracts, verification receipts, audit replay, escalation hooks, or settlement adapters.
- Converts natural-language coordination into machine-readable messages and state transitions.
- Narrows the protocol toward boring enterprise trust instead of vague open-ended autonomy.
- Makes ABYS able to implement protocol validators, mock services, conformance tests, or reference clients.
- Makes ITEM artifacts transmissible as structured payloads without importing ITEM mythology into the protocol core.

## Reinforce

Strong SYNTEL material should be upgraded into one of these forms:

1. Protocol specification in `/spec`.
2. Architecture or doctrine in `/docs`.
3. Example message or workflow in `/examples`.
4. Reference implementation in `/src`.
5. Protocol/conformance test in `/tests`.
6. Security or trust model document in `/docs`.

## Flag or discard

Flag weak material when it is:

- Agent-market rhetoric without message formats, roles, trust assumptions, or verification.
- Claims of autonomy without identity, authorization, replayability, constraints, or escalation.
- Settlement language without bounded task contracts and reversible failure modes.
- Protocol language that depends on a public token before the MVP has enterprise adoption.
- Vague latency or intelligence claims that do not affect the envelope, endpoint, state machine, or audit trail.

Discard, compress, or defer anything that cannot become a spec element, test vector, endpoint, state transition, or implementation requirement.

## Protocol test

A proposed SYNTEL addition passes only if it answers:

- Who are the parties?
- How is identity proven?
- What is the message shape?
- What capability or intent is being exchanged?
- What constraints bound the task?
- How is outcome verified?
- How can a human audit or interrupt the flow?
- What does ABYS implement because this exists?

## Boundary rule

- ITEM defines artifacts and canon.
- ABYS builds software and execution workflows.
- SYNTEL defines protocol contracts and message exchange.

If a file is mainly artifact doctrine, move it to ITEM.
If a file is mainly implementation workflow, move it to ABYS.
If a file is mainly protocol structure, keep it in SYNTEL.

## Immediate refactor targets

1. Add the signed message envelope spec.
2. Add capability discovery and intent negotiation examples.
3. Add verification receipt examples.
4. Add protocol conformance tests.
5. Add explicit non-goals to prevent marketplace/token sprawl before the rail is trustworthy.

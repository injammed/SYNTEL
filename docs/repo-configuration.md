# SYNTEL Repo Configuration

SYNTEL is the protocol rail. It defines narrow, verifiable agent-to-agent and machine-to-machine coordination across organizational boundaries.

## Canonical boundary

SYNTEL accepts material that improves at least one of:

- agent identity
- signed message envelopes
- capability discovery
- bounded intent negotiation
- task contract expression
- verification receipts
- audit replay
- human escalation
- interoperability
- conformance testing

SYNTEL rejects or defers material that turns the v0 protocol into a vague AGI marketplace, speculative mesh economy, token system, or opaque autonomous execution layer.

## Preferred structure

```txt
/spec/identity          agent identity documents
/spec/envelope          signed message envelope schemas
/spec/capabilities      discovery endpoint schemas
/spec/intent            negotiation message schemas
/spec/contracts         bounded task contract format
/spec/receipts          verification receipt format
/spec/audit             append-only audit/replay model
/examples               end-to-end message flows
/src                    reference service implementation
/tests                  conformance and replay tests
/rejected               protocol claims/features rejected for v0
/docs                   architecture and protocol doctrine
```

## Protocol gate

A SYNTEL feature cannot enter v0 unless it states:

1. protocol role
2. message shape or schema impact
3. identity/trust assumption
4. verification method
5. audit/replay behavior
6. failure mode
7. human escalation path
8. security boundary
9. non-goals preserved
10. conformance test requirement

## Canon-vs-slop critique

Canon in SYNTEL is boring interoperability that can be signed, validated, replayed, and audited.

Slop in SYNTEL is any claim that increases autonomy, settlement, market language, or scale before the v0 rail is verifiable.

## Routing

- Artifact doctrine, canonical object records, symbolic/economic item specs: route to `injammed/ITEM`.
- Product execution, task routing, code workflows, Codex packets, CI, dashboards: route to `injammed/ABYS`.
- A2A/M2M protocol specs, signed envelopes, discovery, contracts, receipts, audit replay: keep in SYNTEL.

## Deletion/refactor rule

If a proposed feature does not increase verifiability, interoperability, auditability, or bounded execution, reject it, defer it beyond v0, or move it out of SYNTEL.

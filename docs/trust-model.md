# SYNTEL Trust Model v0

SYNTEL is a trust rail for machine-to-machine and agent-to-agent coordination. It does not assume agents are honest, permanent, sovereign, or legally autonomous. It assumes agents are bounded actors that require identity, authority, verification, receipts, and replayable evidence.

## Canon

Preserve these concepts:

- agent identity
- authority scope
- delegation chain
- signed interaction receipt
- replayable audit evidence
- revocation
- human escalation

Reject or refactor these concepts until protocol primitives exist:

- machine civilization
- autonomous economy
- agent nation
- digital sovereignty
- irreversible settlement
- unverifiable coordination

## Protocol reality rule

An action does not enter SYNTEL protocol reality unless it has:

1. a registered sender identity
2. a registered receiver identity
3. an authority scope
4. a timestamp
5. input and output hashes
6. a signature
7. a receipt status
8. a replayable evidence URI when applicable

No identity means no counterparty.
No signature means no proof.
No receipt means no protocol event.
No revocation path means no enterprise trust.

## Trust boundary

SYNTEL does not prove that an agent is wise, safe, or correct. SYNTEL proves that a specific identified actor claimed a specific bounded action at a specific time under a specific authority scope.

Correctness is evaluated by ABYS execution records and ITEM artifact review. SYNTEL provides the identity and receipt layer that lets those systems make accountable judgments.

## Minimum v0 flow

```txt
agent identity
→ delegation chain
→ bounded request
→ signed interaction receipt
→ audit replay
→ revocation when needed
```

## Deletion rule

Any SYNTEL document that uses broad economic, civilization, or sovereignty language must either translate that language into schemas, signatures, receipts, revocation, and tests, or be moved to deprecated doctrine.

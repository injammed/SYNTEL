"""Minimal SYNTEL delegation and receipt primitives.

This scaffold intentionally avoids claiming production cryptographic completeness.
It defines canonical payload hashing and validation boundaries so future
implementations can attach real Ed25519 signing and verification.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from typing import Any, Dict, List


class DelegationError(ValueError):
    """Raised when a delegation chain is malformed or invalid."""


def canonical_json(payload: Dict[str, Any]) -> str:
    """Return deterministic JSON for hashing/signing."""
    return json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_payload(payload: Dict[str, Any]) -> str:
    """Hash a JSON-compatible payload."""
    return hashlib.sha256(canonical_json(payload).encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class Signature:
    key_id: str
    algorithm: str
    value: str

    def validate(self) -> None:
        if self.algorithm != "ed25519":
            raise DelegationError("only ed25519 signatures are valid in SYNTEL v0")
        if not self.key_id or not self.value:
            raise DelegationError("signature requires key_id and value")


@dataclass(frozen=True)
class Delegation:
    delegator: str
    delegate: str
    scope: str
    constraints: List[str]
    issued_at: str
    expires_at: str
    signature: Signature

    def validate(self) -> None:
        if not self.delegator or not self.delegate:
            raise DelegationError("delegator and delegate are required")
        if self.delegator == self.delegate:
            raise DelegationError("delegator and delegate must differ")
        if not self.scope:
            raise DelegationError("scope is required")
        self.signature.validate()
        issued = datetime.fromisoformat(self.issued_at.replace("Z", "+00:00"))
        expires = datetime.fromisoformat(self.expires_at.replace("Z", "+00:00"))
        now = datetime.now(timezone.utc)
        if expires <= issued:
            raise DelegationError("expires_at must be after issued_at")
        if expires <= now:
            raise DelegationError("delegation has expired")

    def unsigned_payload(self) -> Dict[str, Any]:
        payload = asdict(self)
        payload.pop("signature", None)
        return payload

    def payload_hash(self) -> str:
        return sha256_payload(self.unsigned_payload())


@dataclass(frozen=True)
class InteractionReceipt:
    receipt_id: str
    sender_agent_id: str
    receiver_agent_id: str
    timestamp: str
    intent: str
    authority_scope: str
    input_hash: str
    output_hash: str
    status: str
    signature: Signature

    def validate(self) -> None:
        if self.status not in {"accepted", "rejected", "completed", "failed", "revoked"}:
            raise DelegationError(f"invalid receipt status: {self.status}")
        if not self.input_hash or not self.output_hash:
            raise DelegationError("receipt requires input_hash and output_hash")
        self.signature.validate()


def validate_delegation_chain(delegations: List[Delegation]) -> None:
    """Validate that each delegation hands authority to the next actor."""
    if not delegations:
        raise DelegationError("delegation chain cannot be empty")
    for delegation in delegations:
        delegation.validate()
    for previous, current in zip(delegations, delegations[1:]):
        if previous.delegate != current.delegator:
            raise DelegationError("delegation chain is broken between actors")
        if previous.scope != current.scope:
            raise DelegationError("scope escalation or mutation detected")


def build_receipt_hash(receipt: InteractionReceipt) -> str:
    payload = asdict(receipt)
    payload.pop("signature", None)
    return sha256_payload(payload)

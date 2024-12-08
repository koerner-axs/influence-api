from dataclasses import dataclass  # noqa: F401
from typing import Dict, List  # noqa: F401

from starknet_py.hash.utils import _starknet_keccak

from influencepy.starknet.net.datatypes import *  # noqa: F401
from influencepy.starknet.net.structs import *  # noqa: F401


class ComponentReference(Schema):
    pass


class UnknownComponentUpdatedPreamble(Schema):
    first_unknown: u128
    second_unknown: PackedEntity


class ComponentUpdated(UnknownComponentUpdatedPreamble):
    """Note: The name of this event class was reversed from its keccak hash.
    As such, it may be incorrect and is subject to change."""
    _key: int = _starknet_keccak(b'ComponentUpdated')  # first key
    _name: str  # second key
    _version_key: int  # optional versioning keys


### GENERATED BLOCK ###


class UnknownComponentUpdated(ComponentUpdated):
    def __init__(self, name: str, keys: List[int], data: Calldata):
        self.name = name
        self.keys = keys
        self.data = data


### GENERATED BLOCK ###

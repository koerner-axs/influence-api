from dataclasses import dataclass  # noqa: F401
from typing import Dict, List  # noqa: F401

from starknet_py.hash.utils import _starknet_keccak

from influencepy.starknet.net.datatypes import *  # noqa: F401
from influencepy.starknet.net.struct import *  # noqa: F401


class ComponentUpdated(Schema):
    """Note: The name of this event class was reversed from its keccak hash.
    As such, it may be incorrect and is subject to change."""
    _key: int = _starknet_keccak(b'ComponentUpdated')  # first key
    _name: str  # second key


### GENERATED BLOCK ###


class UnknownComponentUpdated(ComponentUpdated):
    def __init__(self, name: str, data: Calldata):
        self.name = name
        self.data = data


### GENERATED BLOCK ###

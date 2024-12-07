from dataclasses import dataclass  # noqa: F401
from typing import Dict, List  # noqa: F401

from starknet_py.hash.utils import _starknet_keccak

from influencepy.starknet.net.datatypes import *
from influencepy.starknet.net.schema import Schema
from influencepy.starknet.net.structs import Entity, InventoryItem  # noqa: F401


class SystemEvent(Schema):
    _key: int


### GENERATED BLOCK ###


class UnknownSystemEvent(SystemEvent):
    def __init__(self, keys: List[int], data: Calldata):
        self.keys = keys
        self.data = data


# Begin unofficial events. The ABIs for these events are not available in the Influence SDK and are inferred manually or
# with the help of StarkNet block explorers.
class ContractRegisteredEvent(SystemEvent):
    # TODO: This is an event the Dispatcher emits when register_contract is successful. It does not represent an event
    #  emitted by a system, so it might need to inherit from a different class and be renamed accordingly.
    name: shortstr
    address: ContractAddress
    _key: int = _starknet_keccak(b'ContractRegistered')


class SystemRegisteredEvent(SystemEvent):
    # TODO: This is an event the Dispatcher emits when register_system is successful. It does not represent an event
    #  emitted by a system, so it might need to inherit from a different class and be renamed accordingly.
    name: shortstr
    class_hash: ClassHash
    _key: int = _starknet_keccak(b'SystemRegistered')


class UnknownEvent:
    def __init__(self, keys: List[int], data: Calldata):
        self.keys = keys
        self.data = data


### GENERATED BLOCK ###

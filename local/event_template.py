from dataclasses import dataclass  # noqa: F401
from typing import Dict, List  # noqa: F401

from starknet_py.hash.utils import _starknet_keccak

from influencepy.starknet.net.component import *  # noqa: F401
from influencepy.starknet.net.datatypes import *
from influencepy.starknet.net.schema import Schema
from influencepy.starknet.net.structs import Entity, InventoryItem  # noqa: F401


class SystemEvent(Schema):
    _key: int


class UniqueReference(Schema):
    entity_type: EntityType


### GENERATED BLOCK ###


class ComponentUpdated(SystemEvent):
    reference: None
    _key: int = _starknet_keccak(b'ComponentUpdated')
    _name: str  # name of the component
    _version_key: int  # optional versioning key


### GENERATED BLOCK ###


# Begin unofficial events. The ABIs for these events are not available in the Influence SDK and are inferred manually or
# with the help of StarkNet block explorers.
class ContractRegisteredEvent(SystemEvent):
    # TODO: This is an event the Dispatcher emits when register_contract is successful. It does not represent an event
    #  emitted by a system, so it might need to inherit from a different class and be renamed accordingly.
    name: ShortString
    address: ContractAddress
    _key: int = _starknet_keccak(b'ContractRegistered')


class SystemRegisteredEvent(SystemEvent):
    # TODO: This is an event the Dispatcher emits when register_system is successful. It does not represent an event
    #  emitted by a system, so it might need to inherit from a different class and be renamed accordingly.
    name: ShortString
    class_hash: ClassHash
    _key: int = _starknet_keccak(b'SystemRegistered')


class UnknownSystemEvent(SystemEvent):
    def __init__(self, keys: List[int], data: Calldata):
        self.keys = keys
        self.data = data


class UnknownEvent:
    def __init__(self, keys: List[int], data: Calldata):
        self.keys = keys
        self.data = data


### GENERATED BLOCK ###


# TODO: Versioning for ShipV0 and ShipV1
### GENERATED BLOCK ###

from dataclasses import dataclass
from enum import Enum

from influencepy.starknet.net.datatypes import u64, u256, ContractAddress, felt252, Calldata
from influencepy.starknet.net.schema import Schema


class Enum64(Schema, Enum):
    @classmethod
    def from_calldata(cls, calldata: Calldata, **kwargs) -> "Enum64":
        return cls(calldata.pop_int())

    def to_calldata(self, calldata: Calldata) -> Calldata:
        calldata.push_int(self.value)
        return calldata

    def __str__(self):
        return self.name


class EntityType(Enum64):
    CREW = 1
    CREWMATE = 2
    ASTEROID = 3
    LOT = 4
    BUILDING = 5
    SHIP = 6
    DEPOSIT = 7
    DELIVERY = 9
    SPACE = 10


@dataclass
class Entity(Schema):
    entity_type: EntityType
    entity_id: u64


class Crew(Entity):
    """ Convenience class for crew entities. """

    def __init__(self, crew_id: int):
        super().__init__(entity_type=EntityType.CREW, entity_id=crew_id)


class Building(Entity):
    """ Convenience class for building entities. """

    def __init__(self, building_id: int):
        super().__init__(entity_type=EntityType.BUILDING, entity_id=building_id)


class Deposit(Entity):
    """ Convenience class for deposit entities. """

    def __init__(self, deposit_id: int):
        super().__init__(entity_type=EntityType.DEPOSIT, entity_id=deposit_id)


class PackedEntity(Schema):
    entity_id: int
    entity_type: EntityType

    def __init__(self, entity_id: int, entity_type: EntityType):
        self.entity_id = entity_id
        self.entity_type = entity_type

    @classmethod
    def from_calldata(cls, calldata: Calldata, **kwargs) -> "Schema":
        packed = calldata.pop_int()
        return PackedEntity(entity_id=packed >> 16, entity_type=EntityType(packed & 0xFFFF))

    def to_calldata(self, calldata: Calldata) -> Calldata:
        calldata.push_int((self.entity_id << 16) | self.entity_type.value)
        return calldata

    def __str__(self):
        return f'{self.entity_type}({self.entity_id})'


class BuildingId(Enum64):
    EMPTY_LOT: 0
    WAREHOUSE: 1
    EXTRACTOR: 2
    REFINERY: 3
    BIOREACTOR: 4
    FACTORY: 5
    SHIPYARD: 6
    SPACEPORT: 7
    MARKETPLACE: 8
    HABITAT: 9
    TANK_FARM: 10


@dataclass
class InventoryItem(Schema):
    product: u64
    amount: u64


@dataclass
class Withdrawal(Schema):
    recipient: ContractAddress
    amount: u256


@dataclass
class SeededAsteroid(Schema):
    asteroid_id: u64
    name: felt252


@dataclass
class SeededCrewmate(Schema):
    crewmate_id: u64
    name: felt252

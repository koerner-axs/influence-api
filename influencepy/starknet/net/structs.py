from dataclasses import dataclass

from influencepy.starknet.net.datatypes import u64, u256, ContractAddress, felt252
from influencepy.starknet.net.schema import Schema


class EntityId(u64):
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
    entity_type: EntityId
    entity_id: u64


class Crew(Entity):
    """ Convenience class for crew entities. """

    def __init__(self, crew_id: int):
        super().__init__(entity_type=EntityId.CREW, entity_id=crew_id)


class Building(Entity):
    """ Convenience class for building entities. """

    def __init__(self, building_id: int):
        super().__init__(entity_type=EntityId.BUILDING, entity_id=building_id)


class Deposit(Entity):
    """ Convenience class for deposit entities. """

    def __init__(self, deposit_id: int):
        super().__init__(entity_type=EntityId.DEPOSIT, entity_id=deposit_id)


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

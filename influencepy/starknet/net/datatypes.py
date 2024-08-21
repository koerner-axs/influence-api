from dataclasses import dataclass
from typing import List

from starknet_py.cairo import felt
from starknet_py.net.schemas.common import Felt


class Calldata:
    def __init__(self, calldata: list[int]):
        self.data = calldata

    def __len__(self):
        return len(self.data)

    def pop_int(self) -> int:
        return self.data.pop(0)

    def pop_string(self) -> str:
        return felt.decode_shortstring(self.pop_int())

    def push_int(self, value: int):
        self.data.append(value)

    def push_string(self, value: str):
        self.push_int(felt.encode_shortstring(value))


class InfluenceStruct:
    def to_calldata(self) -> List[int]:
        raise NotImplementedError

    @staticmethod
    def from_calldata(calldata: Calldata) -> "InfluenceStruct":
        raise NotImplementedError


class UnsignedInt256(InfluenceStruct):
    def __init__(self, value: int):
        if not 0 <= value < 2 ** 256:
            raise ValueError(f"Value {value} is not in the range [0, 2**256)")
        self.value = value

    def to_calldata(self) -> List[int]:
        low = self.value & (2 ** 128 - 1)
        high = self.value >> 128
        return [low, high]

    @staticmethod
    def from_calldata(calldata: Calldata) -> "UnsignedInt256":
        low = calldata.pop_int()
        high = calldata.pop_int()
        return UnsignedInt256(low + (high << 128))


ContractAddress = int
u64 = int
u128 = int
u256 = UnsignedInt256
felt252 = Felt


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
class Entity(InfluenceStruct):
    entity_type: EntityId
    entity_id: u64

    def to_calldata(self) -> List[int]:
        return [self.entity_type, self.entity_id]


class Crew(Entity):
    """ Convenience class for crew entities. """

    def __init__(self, crew_id: int):
        super().__init__(entity_type=EntityId.CREW, entity_id=crew_id)


class Building(Entity):
    """ Convenience class for building entities. """

    def __init__(self, building_id: int):
        super().__init__(entity_type=EntityId.BUILDING, entity_id=building_id)


@dataclass
class CubitFixedPoint64(InfluenceStruct):
    mag: u64
    sign: bool


@dataclass
class CubitFixedPoint128(InfluenceStruct):
    mag: u128
    sign: bool


@dataclass
class InventoryItem(InfluenceStruct):
    product: u64
    amount: u64


@dataclass
class Withdrawal(InfluenceStruct):
    recipient: ContractAddress
    amount: u256


@dataclass
class SeededAsteroid(InfluenceStruct):
    asteroid_id: u64
    name: felt252


@dataclass
class SeededCrewmate(InfluenceStruct):
    crewmate_id: u64
    name: felt252

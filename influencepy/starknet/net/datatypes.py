from typing import List

from starknet_py.cairo import felt


ContractAddress = int


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


class Entity(InfluenceStruct):
    CREW = 1
    CREWMATE = 2
    ASTEROID = 3
    LOT = 4
    BUILDING = 5
    SHIP = 6
    DEPOSIT = 7
    DELIVERY = 9
    SPACE = 10

    def __init__(self, entity_type: int, entity_id: int):
        self.entity_type = entity_type
        self.entity_id = entity_id

    def to_calldata(self) -> List[int]:
        return [self.entity_type, self.entity_id]


class Crew(Entity):
    """ Convenience class for crew entities. """
    def __init__(self, crew_id: int):
        super().__init__(entity_type=Entity.CREW, entity_id=crew_id)


class Building(Entity):
    """ Convenience class for building entities. """
    def __init__(self, building_id: int):
        super().__init__(entity_type=Entity.BUILDING, entity_id=building_id)


class CubitFixedFloat(InfluenceStruct):
    pass  # TODO


class InventoryItem(InfluenceStruct):
    pass  # TODO


class Withdrawal(InfluenceStruct):
    pass  # TODO


class SeededAsteroid(InfluenceStruct):
    pass  # TODO

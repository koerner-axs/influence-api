from typing import List

from influencepy.starknet.net.component import Crew
from influencepy.starknet.net.datatypes import Calldata, u64, AccountAddress, felt252
from influencepy.starknet.net.event import CrewUpdated
from influencepy.starknet.net.parser.parser import EventParser
from influencepy.starknet.net.schema import Schema
from influencepy.starknet.net.structs import Entity, PackedEntity


class CrewV0UpdatedEvent(CrewUpdated):
    state: Crew

    @classmethod
    def parse_legacy_0(cls, calldata: Calldata) -> "CrewV0UpdatedEvent":
        instance = cls.__new__(cls)
        instance.unknown_1 = felt252.from_calldata(calldata)
        instance.crew = PackedEntity.from_calldata(calldata)
        crew = Crew.__new__(Crew)
        crew.delegated_to = AccountAddress.from_calldata(calldata)
        crew.roster = Schema.list_from_calldata(u64, calldata)
        crew.last_fed = u64.from_calldata(calldata)
        crew.ready_at = u64.from_calldata(calldata)
        crew.action_type = u64.from_calldata(calldata)
        # I have to assume the type of action_target has changed from PackedEntity to Entity
        # otherwise the early CrewEvents will not be able to be parsed
        crew.action_target = PackedEntity.from_calldata(calldata).unpack()
        if len(calldata) == 3:
            crew.action_round = u64.from_calldata(calldata)
            crew.action_weight = u64.from_calldata(calldata)
            crew.action_strategy = u64.from_calldata(calldata)
        elif len(calldata) == 0:
            crew.action_round = 0
            crew.action_weight = 0
            crew.action_strategy = 0
        else:
            raise ValueError(f'Unexpected calldata: {calldata}')
        instance.state = crew
        return instance


class CrewV1UpdatedEvent(CrewUpdated):
    state: Crew


class CrewUpdatedEventParser(EventParser):
    def __call__(self, keys: List[int], calldata: Calldata, **kwargs) -> CrewUpdated:
        version = 0 if len(keys) < 3 else keys[2]
        if version == 0:
            return CrewV0UpdatedEvent.parse_legacy_0(calldata)
        elif version == 1:
            return CrewV1UpdatedEvent.from_calldata(calldata)
        raise NotImplementedError(f'CrewUpdated event version "{version}" is not implemented')

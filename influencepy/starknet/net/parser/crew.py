from typing import List

from influencepy.starknet.net.component import Crew
from influencepy.starknet.net.datatypes import Calldata, ContractAddress, u64, AccountAddress
from influencepy.starknet.net.event import CrewUpdated
from influencepy.starknet.net.parser.parser import EventParser


class CrewV0UpdatedEvent(CrewUpdated):
    delegated_to: AccountAddress
    roster: List[u64]
    last_fed: u64
    ready_at: u64
    unknown_field_1: u64
    unknown_field_2: u64


class CrewV1UpdatedEvent(Crew, CrewUpdated):
    # TODO: maybe this should still be within a variable 'state'?
    pass


class CrewUpdatedEventParser(EventParser):
    def __call__(self, keys: List[int], calldata: Calldata, **kwargs) -> CrewUpdated:
        version = 0 if len(keys) < 3 else keys[2]
        if version == 0:
            return CrewV0UpdatedEvent.from_calldata(calldata)
        elif version == 1:
            return CrewV1UpdatedEvent.from_calldata(calldata)
        raise NotImplementedError(f'CrewUpdated event version "{version}" is not implemented')

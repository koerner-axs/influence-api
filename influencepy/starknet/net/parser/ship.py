from typing import List

from influencepy.starknet.net.component import Ship
from influencepy.starknet.net.datatypes import Calldata, u64
from influencepy.starknet.net.event import ShipUpdated
from influencepy.starknet.net.parser.parser import EventParser


class ShipV0UpdatedEvent(ShipUpdated):
    ship_type: u64
    status: u64
    ready_at: u64
    variant: u64


class ShipV1UpdatedEvent(ShipUpdated, Ship):
    pass


class ShipUpdatedEventParser(EventParser):
    def __call__(self, keys: List[int], calldata: Calldata, **kwargs) -> ShipUpdated:
        version = 0 if len(keys) < 3 else keys[2]
        if version == 0:
            return ShipV0UpdatedEvent.from_calldata(calldata)
        elif version == 1:
            return ShipV1UpdatedEvent.from_calldata(calldata)
        raise NotImplementedError(f'ShipUpdated event version "{version}" is not implemented')

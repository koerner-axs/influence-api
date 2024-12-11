from typing import List

from influencepy.starknet.net.datatypes import Calldata
from influencepy.starknet.net.event import SystemEvent
from influencepy.starknet.net.schema import Schema


class CallParser:
    def __call__(self, calldata: Calldata, **kwargs) -> Schema:
        raise NotImplementedError('CallParser is an abstract class')


class EventParser:
    def __call__(self, keys: List[int], calldata: Calldata, **kwargs) -> SystemEvent:
        raise NotImplementedError('EventParser is an abstract class')

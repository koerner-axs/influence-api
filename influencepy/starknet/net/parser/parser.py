from typing import List

from influencepy.starknet.net.datatypes import Calldata


class CallParser:
    def __call__(self, calldata: Calldata, **kwargs):
        raise NotImplementedError('CallParser is an abstract class')


class EventParser:
    def __call__(self, keys: List[int], calldata: Calldata, **kwargs):
        raise NotImplementedError('EventParser is an abstract class')

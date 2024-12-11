from typing import List, Dict, cast

from influencepy.starknet.net.datatypes import Calldata, ShortString
from influencepy.starknet.net.event import ComponentUpdated
from influencepy.starknet.net.parser.parser import EventParser
from influencepy.starknet.net.parser.unique import UniqueEventParser

PARSER: Dict[str, EventParser] = {
    'Unique': UniqueEventParser()
}


class ComponentUpdatedEventParser:
    def __call__(self, keys: List[int], calldata: Calldata, **kwargs) -> ComponentUpdated:
        name = ShortString.decode(keys[1]).value
        if name not in PARSER:
            raise NotImplementedError(f'ComponentUpdated event "{name}" is not implemented')
        parser = PARSER.get(name)
        if not isinstance(parser, list):
            return cast(ComponentUpdated, parser(keys, calldata, **kwargs))
        version = 0 if len(keys) < 3 else keys[2]
        for p in parser:
            if p.version == version:
                return cast(ComponentUpdated, p(keys, calldata, **kwargs))
        raise ValueError(f'ComponentUpdated event "{name}" has no associated parser with version {version}')

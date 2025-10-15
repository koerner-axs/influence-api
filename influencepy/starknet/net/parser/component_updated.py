from typing import List, Dict, cast

from influencepy.starknet.net.datatypes import Calldata, ShortString
from influencepy.starknet.net.event import ComponentUpdated, ALL_COMPONENT_UPDATED
from influencepy.starknet.net.parser.crew import CrewUpdatedEventParser
from influencepy.starknet.net.parser.parser import EventParser
from influencepy.starknet.net.parser.ship import ShipUpdatedEventParser
from influencepy.starknet.net.parser.unique import UniqueEventParser


class SimpleComponentUpdatedParser(EventParser):
    def __init__(self, component: ComponentUpdated):
        self.component = component

    def __call__(self, keys: List[int], calldata: Calldata, **kwargs) -> ComponentUpdated:
        return self.component.from_calldata(calldata)


PARSER: Dict[str, EventParser] = {
    'Unique': UniqueEventParser(),
    'Crew': CrewUpdatedEventParser(),
    'Ship': ShipUpdatedEventParser(),
    **{event._name: SimpleComponentUpdatedParser(event) for event in ALL_COMPONENT_UPDATED}
}


class ComponentUpdatedEventParser:
    def __call__(self, keys: List[int], calldata: Calldata, **kwargs) -> ComponentUpdated:
        name = ShortString.decode(keys[1]).value
        if name not in PARSER:
            raise NotImplementedError(f'ComponentUpdated event "{name}" is not implemented')
        parser = PARSER.get(name)
        return cast(ComponentUpdated, parser(keys, calldata, **kwargs))

import json
import keyword
from type_map import type_map

with open('local/starknet_events.json', 'r') as f:
    event_file = json.load(f)

event_list = list(event_file.keys())
event_list.sort()

gen_lines = []
gen_lines.append("""from typing import Dict, List
from dataclasses import dataclass

from starknet_py.hash.utils import _starknet_keccak

from influencepy.starknet.net.datatypes import u64, u128, u256, felt252, shortstr, Bool, Calldata, ClassHash, \\
    ContractAddress, CubitFixedPoint64
from influencepy.starknet.net.schema import Schema
from influencepy.starknet.net.structs import Entity, InventoryItem


class SystemEvent(Schema):
    _key: int
""")
for event_name in event_list:
    event = event_file[event_name]
    gen_lines.append('')
    gen_lines.append('@dataclass')
    gen_lines.append(f'class {event_name}(SystemEvent):')
    for field in event['members']:
        mapped_type = type_map[field['type']]
        name = field['name']
        if keyword.iskeyword(field['name']):
            name += '_'
        gen_lines.append(f'    {name}: {mapped_type}')
    gen_lines.append(f'    _key: int = _starknet_keccak(b\'{event_name}\')')
    gen_lines.append('')
gen_lines.append("""
class UnknownSystemEvent(SystemEvent):
    def __init__(self, keys: List[int], data: Calldata):
        self.keys = keys
        self.data = data


# Begin unofficial events. The ABIs for these events are not available in the Influence SDK and are inferred manually or
# with the help of StarkNet block explorers.
class ContractRegisteredEvent(SystemEvent):
    # TODO: This is an event the Dispatcher emits when register_contract is successful. It does not represent an event
    #  emitted by a system, so it might need to inherit from a different class and be renamed accordingly.
    name: felt252
    address: ContractAddress
    _key: int = _starknet_keccak(b'ContractRegistered')


class SystemRegisteredEvent(SystemEvent):
    # TODO: This is an event the Dispatcher emits when register_system is successful. It does not represent an event
    #  emitted by a system, so it might need to inherit from a different class and be renamed accordingly.
    name: felt252
    class_hash: ClassHash
    _key: int = _starknet_keccak(b'SystemRegistered')


class UnknownEvent:
    def __init__(self, keys: List[int], data: Calldata):
        self.keys = keys
        self.data = data

""")
unofficial_event_list = ['ContractRegisteredEvent', 'SystemRegisteredEvent']
gen_lines.append('ALL_SYSTEM_EVENTS: Dict[int, SystemEvent] = {')
for event_name in event_list:
    gen_lines.append(f'    {event_name}._key: {event_name},')
gen_lines.append('    # Begin unofficial events')
for event_name in unofficial_event_list:
    gen_lines.append(f'    {event_name}._key: {event_name},')
gen_lines.append('}')
gen_lines.append('')

with open('influencepy/starknet/net/event.py', 'w') as f:
    f.write('\n'.join(gen_lines))

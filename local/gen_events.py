import json
import keyword

type_map = {
    'core::integer::u64': 'u64',
    'core::array::Span::<core::integer::u64>': 'List[u64]',
    'core::integer::u128': 'u128',
    'core::array::Span::<core::integer::u128>': 'List[u128]',
    'core::integer::u256': 'u256',
    'core::array::Span::<core::integer::u256>': 'List[u256]',
    'core::felt252': 'felt252',
    'core::array::Span::<core::felt252>': 'List[felt252]',
    'core::bool': 'bool',
    'core::starknet::contract_address::ContractAddress': 'ContractAddress',
    'influence::common::types::string::String': 'shortstr',
    'cubit::f64::types::fixed::Fixed': 'CubitFixedPoint64',
    'influence::common::types::entity::Entity': 'Entity',
    'influence::common::types::inventory_item::InventoryItem': 'InventoryItem',
    'core::array::Span::<influence::common::types::inventory_item::InventoryItem>': 'List[InventoryItem]'
}

with open('local/starknet_events.json', 'r') as f:
    event_file = json.load(f)

event_list = list(event_file.keys())
event_list.sort()

gen_lines = []
gen_lines.append("""from typing import Dict, List
from dataclasses import dataclass

from starknet_py.hash.utils import _starknet_keccak

from influencepy.starknet.net.datatypes import u64, u128, u256, felt252, shortstr, ClassHash, ContractAddress, \\
    CubitFixedPoint64
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
    def __init__(self, keys: List[int], data: List[int]):
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


class SeedingEvent(SystemEvent):
    \"\"\"Note: The name of this event class is inferred from the context in which it appears on the chain.
    As such, it may be incorrect and is subject to change.\"\"\"
    type: shortstr
    _key: int = 0x297be67eb977068ccd2304c6440368d4a6114929aeb860c98b6a7e91f96e2ef

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

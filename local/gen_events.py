import json
import keyword

type_map = {
    'core::integer::u64': 'u64',
    'influence::common::types::entity::Entity': 'Entity',
    'core::starknet::contract_address::ContractAddress': 'ContractAddress',
    'core::array::Span::<core::integer::u64>': 'List[u64]',
    'core::felt252': 'felt252',
    'cubit::f64::types::fixed::Fixed': 'CubitFixedPoint64',
    'core::array::Span::<influence::common::types::inventory_item::InventoryItem>': 'List[InventoryItem]',
    'core::array::Span::<core::felt252>': 'List[felt252]',
    'influence::common::types::string::String': 'shortstr',
    'core::array::Span::<core::integer::u128>': 'List[u128]',
    'core::bool': 'bool',
    'core::integer::u256': 'u256',
}

with open('local/starknet_events.json', 'r') as f:
    event_file = json.load(f)

event_list = list(event_file.keys())
event_list.sort()

gen_lines = []
gen_lines.append('from typing import Dict, List')
gen_lines.append('from dataclasses import dataclass')
gen_lines.append('')
gen_lines.append('from starknet_py.hash.utils import _starknet_keccak')
gen_lines.append('')
gen_lines.append('from influencepy.starknet.net.datatypes import u64, u128, u256, felt252, shortstr, CubitFixedPoint64, ContractAddress')
gen_lines.append('from influencepy.starknet.net.schema import Schema')
gen_lines.append('from influencepy.starknet.net.structs import Entity, InventoryItem')
gen_lines.append('')
gen_lines.append('')
gen_lines.append('class SystemEvent(Schema):')
gen_lines.append('    _key: int')
gen_lines.append('')
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
gen_lines.append('')
gen_lines.append('ALL_SYSTEM_EVENTS: Dict[int, SystemEvent] = {')
for event_name in event_list:
    gen_lines.append(f'    {event_name}._key: {event_name},')
gen_lines.append('}')
gen_lines.append('')

with open('influencepy/starknet/net/event.py', 'w') as f:
    f.write('\n'.join(gen_lines))

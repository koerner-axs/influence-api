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
    'core::bool': 'Bool',
    'core::starknet::contract_address::ContractAddress': 'ContractAddress',
    'influence::common::types::string::String': 'shortstr',
    'cubit::f64::types::fixed::Fixed': 'CubitFixedPoint64',
    'cubit::f128::types::fixed::Fixed': 'CubitFixedPoint128',
    'influence::common::types::entity::Entity': 'Entity',
    'influence::common::types::inventory_item::InventoryItem': 'InventoryItem',
    'core::array::Span::<influence::common::types::inventory_item::InventoryItem>': 'List[InventoryItem]'
}


def replace_placeholder(template: str, replacement: str) -> str:
    return template.replace('### GENERATED BLOCK ###', replacement, 1)


with open('local/starknet_components_compatible.json', 'r') as f:
    event_file = json.load(f)

component_list = [(x.split('::')[-1], y) for x, y in event_file.items()]
component_list.sort(key=lambda x: x[0])

with open('local/component_template.py', 'r') as f:
    component_template = f.read()

gen_lines = []
for class_name, component in component_list:
    component_name = component['name'].split('::')[-1]
    gen_lines.append('@dataclass')
    gen_lines.append(f'class {class_name}(ComponentUpdated):')
    for field in component['members']:
        mapped_type = type_map.get(field['type'], field['type'])
        if mapped_type is None:
            print('Unmapped datatype:', field['type'])
        name = field['name']
        if keyword.iskeyword(field['name']):
            name += '_'
        gen_lines.append(f'    {name}: {mapped_type}')
    gen_lines.append(f'    _name: str = \'{component_name}\'')
    if 'version_key' in component:
        gen_lines.append(f'    _version_key: int = {component["version_key"]}')
    gen_lines.append('\n')
gen_lines = gen_lines[:-1]
component_template = replace_placeholder(component_template, '\n'.join(gen_lines))


aggregated_over_versions = {}
for class_name, component in component_list:
    name = component['name'].split('::')[-1]
    if name not in aggregated_over_versions:
        aggregated_over_versions[name] = []
    aggregated_over_versions[name].append(class_name)

gen_lines = []
gen_lines.append('ALL_COMPONENTS: Dict[str, ComponentUpdated | List[ComponentUpdated]] = {')
for name, comps in aggregated_over_versions.items():
    if len(comps) == 1:
        gen_lines.append(f'    {comps[0]}._name: {comps[0]},')
    else:
        gen_lines.append(f'    {comps[0]}._name: [{", ".join(comps)}],')
gen_lines.append('}')
component_template = replace_placeholder(component_template, '\n'.join(gen_lines))

with open('influencepy/starknet/net/component.py', 'w') as f:
    f.write(component_template)

import json
import keyword
from type_map import type_map

field_name_override = {
    # ('<class name>', '<field name>'): '<new field name>',
}

# Field name override is applied before, so use the new field name
type_override = {
    # ('<class name>', '<field name>'): '<new type>',
}

trailing_text = {
    # '<class name>': '<text>',
}


def replace_placeholder(template: str, replacement: str) -> str:
    return template.replace('### GENERATED BLOCK ###', replacement, 1)


with open('local/component_template.py', 'r') as f:
    component_template = f.read()

with open('local/starknet_components_compatible.json', 'r') as f:
    component_file = json.load(f)
component_list = [(x.split('::')[-1], y) for x, y in component_file.items()]
component_list.sort(key=lambda x: x[0])
gen_lines = []
for class_name, component in component_list:
    component_name = component['name'].split('::')[-1]
    gen_lines.append('@dataclass')
    gen_lines.append(f'class {class_name}(ComponentUpdated):')
    for field in component['members']:
        field_name = field_name_override.get((class_name, field['name']), field['name'])
        if (class_name, field_name) in type_override:
            mapped_type = type_override[(class_name, field_name)]
        else:
            mapped_type = type_map.get(field['type'])
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

gen_lines = ['ALL_COMPONENTS: Dict[str, ComponentUpdated | List[ComponentUpdated]] = {']
for name, comps in aggregated_over_versions.items():
    if len(comps) == 1:
        gen_lines.append(f'    {comps[0]}._name: {comps[0]},')
    else:
        gen_lines.append(f'    {comps[0]}._name: [{", ".join(comps)}],')
gen_lines.append('}')
component_template = replace_placeholder(component_template, '\n'.join(gen_lines))

with open('influencepy/starknet/net/component.py', 'w') as f:
    f.write(component_template)

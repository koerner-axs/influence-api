import json
import keyword
from type_map import type_map

field_name_override = {
    # ('<class name>', '<field name>'): '<new field name>',
    ('ExchangeCrew', '_crew2'): 'crew2'
}

# Field name override is applied before, so use the new field name
type_override = {
    # ('<class name>', '<field name>'): '<new type>',
}

trailing_text = {
    # '<class name>': '<text>',
    'CheckForRandomEvent':
        """    # TODO: output is of type u64, need to declare this somewhere?\n
    # TODO: should this be in here, should this be completely removed from the system?
    async def query(self, dispatcher: DispatcherContract) -> bool:
        result: List[int] = await dispatcher.run_system(self)
        print('CheckForRandomEvent result:', result)
        if len(result) != 2 or result[0] != 1:
            raise ValueError('CheckForRandomEvent result should have length 2')
        flag = result[1]
        return flag != 0"""
}


def replace_placeholder(template: str, replacement: str) -> str:
    return template.replace('### GENERATED BLOCK ###', replacement, 1)


with open('local/starknet_systems.json', 'r') as f:
    system_file = json.load(f)

systems_list = [(x.split('::')[-1], y) for x, y in system_file.items()]
systems_list.sort(key=lambda x: x[0])

with open('local/system_template.py', 'r') as f:
    system_template = f.read()

gen_lines = []
for class_name, system in systems_list:
    system_name = system['name'].split('::')[-1]
    gen_lines.append('@dataclass')
    gen_lines.append(f'class {class_name}(RunSystem):')
    for field in system['inputs']:
        field_name = field_name_override.get((class_name, field['name']), field['name'])
        if (class_name, field_name) in type_override:
            mapped_type = type_override[(class_name, field_name)]
        else:
            mapped_type = type_map.get(field['type'])
        if mapped_type is None:
            print('Unmapped datatype:', field['type'])
        name = field_name
        if keyword.iskeyword(field_name):
            name += '_'
        gen_lines.append(f'    {name}: {mapped_type}')
    gen_lines.append(f'    _function_name: str = \'{system_name}\'')
    if 'version_key' in system:
        gen_lines.append(f'    _version_key: int = {system["version_key"]}')
    if class_name in trailing_text:
        gen_lines.append(trailing_text[class_name])
    gen_lines.append('\n')
gen_lines = gen_lines[:-1]
system_template = replace_placeholder(system_template, '\n'.join(gen_lines))

aggregated_over_versions = {}
for class_name, system in systems_list:
    name = system['name'].split('::')[-1]
    if name not in aggregated_over_versions:
        aggregated_over_versions[name] = []
    aggregated_over_versions[name].append(class_name)

gen_lines = ['ALL_SYSTEMS: Dict[str, RunSystem | List[RunSystem]] = {']
for name, systems in aggregated_over_versions.items():
    if len(systems) == 1:
        gen_lines.append(f'    {systems[0]}._function_name: {systems[0]},')
    else:
        gen_lines.append(f'    {systems[0]}._function_name: [{", ".join(systems)}],')
gen_lines.append('}')
system_template = replace_placeholder(system_template, '\n'.join(gen_lines))

with open('influencepy/starknet/net/system.py', 'w') as f:
    f.write(system_template)

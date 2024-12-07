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


with open('local/starknet_events.json', 'r') as f:
    event_file = json.load(f)

events_list = [(x.split('::')[-1], y) for x, y in event_file.items()]
events_list.sort(key=lambda x: x[0])

with open('local/event_template.py', 'r') as f:
    event_template = f.read()

gen_lines = []
for class_name, event in events_list:
    event_name = event['name'].split('::')[-1]
    gen_lines.append('@dataclass')
    gen_lines.append(f'class {class_name}(SystemEvent):')
    for field in event['members']:
        field_name = field_name_override.get((class_name, field['name']), field['name'])
        if (class_name, field_name) in type_override:
            mapped_type = type_override[(class_name, field_name)]
        else:
            mapped_type = type_map[field['type']]
        if mapped_type is None:
            print('Unmapped datatype:', field['type'])
        name = field_name
        if keyword.iskeyword(field['name']):
            name += '_'
        gen_lines.append(f'    {name}: {mapped_type}')
    gen_lines.append(f'    _key: int = _starknet_keccak(b\'{event_name}\')')
    gen_lines.append('\n')
gen_lines = gen_lines[:-1]
event_template = replace_placeholder(event_template, '\n'.join(gen_lines))

gen_lines = ['ALL_SYSTEM_EVENTS: Dict[int, SystemEvent] = {']
unofficial_event_list = ['ContractRegisteredEvent', 'SystemRegisteredEvent']
for class_name, event in events_list:
    gen_lines.append(f'    {class_name}._key: {class_name},')
gen_lines.append('    # Begin unofficial events')
for event_name in unofficial_event_list:
    gen_lines.append(f'    {event_name}._key: {event_name},')
gen_lines.append('}')
event_template = replace_placeholder(event_template, '\n'.join(gen_lines))

with open('influencepy/starknet/net/event.py', 'w') as f:
    f.write(event_template)

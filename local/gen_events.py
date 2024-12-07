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

event_list = list(event_file.keys())
event_list.sort()

with open('local/event_template.py', 'r') as f:
    event_template = f.read()

gen_lines = []
for event_name in event_list:
    event = event_file[event_name]
    gen_lines.append('@dataclass')
    gen_lines.append(f'class {event_name}(SystemEvent):')
    for field in event['members']:
        mapped_type = type_map[field['type']]
        name = field['name']
        if keyword.iskeyword(field['name']):
            name += '_'
        gen_lines.append(f'    {name}: {mapped_type}')
    gen_lines.append(f'    _key: int = _starknet_keccak(b\'{event_name}\')')
    gen_lines.append('\n')
gen_lines = gen_lines[:-1]
event_template = replace_placeholder(event_template, '\n'.join(gen_lines))

gen_lines = ['ALL_SYSTEM_EVENTS: Dict[int, SystemEvent] = {']
unofficial_event_list = ['ContractRegisteredEvent', 'SystemRegisteredEvent']
for event_name in event_list:
    gen_lines.append(f'    {event_name}._key: {event_name},')
gen_lines.append('    # Begin unofficial events')
for event_name in unofficial_event_list:
    gen_lines.append(f'    {event_name}._key: {event_name},')
gen_lines.append('}')
event_template = replace_placeholder(event_template, '\n'.join(gen_lines))

with open('influencepy/starknet/net/event.py', 'w') as f:
    f.write(event_template)

from starknet_py.hash.utils import _starknet_keccak

# Brute force all camel-case combinations of the given words and check if the hash matches the given hash

target_keccak = 0x297be67eb977068ccd2304c6440368d4a6114929aeb860c98b6a7e91f96e2ef
max_len = 5
count_checked = 0
dictionary = ['Contract', 'Publish', 'Event', 'Dispatcher', 'System', 'Variable', 'Value', 'Store', 'Stored',
              'Written', 'Updated', 'Update', 'Created', 'Object', 'Asset', 'Component', 'Changed']


def recurse_on_prefix(prefix, depth):
    global count_checked
    # Hash function expects a b'' string so convert the prefix to bytes
    keccak = _starknet_keccak(prefix.encode())
    count_checked += 1
    if count_checked % 50000 == 0:
        print('Checked {} prefixes'.format(count_checked))
    if keccak == target_keccak:
        return prefix
    if depth == 0:
        return None
    for word in dictionary:
        res = recurse_on_prefix(prefix + word, depth - 1)
        if res is not None:
            return res
    return None


hit = recurse_on_prefix('', max_len)
if hit is None:
    print('No match found')
else:
    print('Match found: {}'.format(hit))

import asyncio

from starknet_py.cairo.felt import decode_shortstring
from starknet_py.net.client_models import InvokeTransactionV1
from starknet_py.net.full_node_client import FullNodeClient

from influencepy.starknet.net.constants import DISPATCHER_ADDRESS
from influencepy.starknet.net.datatypes import Calldata
from influencepy.starknet.net.dispatcher import SystemEventDispatcher, EventDispatcher
from influencepy.starknet.net.event import ALL_SYSTEM_EVENTS
from influencepy.starknet.net.transaction import MultiInvocationTransaction
from influencepy.starknet.util.rpc import setup_starknet_context

FILL_SELL_ORDER_TX = 0x05ab19f45ab1cb4ac3db28eae249a4546f684781b1904fc3f21f4b083e1feb85
PROCESS_PROUCTS_FINISH_TX = 0x02fe36eea7dc3628c9c6385f5935737b784008555168a9b9291b08fca6bc6ecd


async def read_event(client: FullNodeClient):
    addr = DISPATCHER_ADDRESS

    # Store hash of first tx that emitted the event
    event_count = {key: 0 for key in ALL_SYSTEM_EVENTS}
    unknown_events = {}

    events = await client.get_events(addr)
    for _ in range(10):
        events = await client.get_events(addr, continuation_token=events.continuation_token, chunk_size=100)
        print(f'Got {len(events.events)} events')
        for event in events.events:
            key = event.keys[0] if len(event.keys) == 1 else tuple(event.keys)
            if key in event_count:
                event_count[key] += 1
                event = EventDispatcher.from_calldata(event.keys, event.data)
            elif key not in unknown_events:
                unknown_events[key] = event.transaction_hash
                hex_key = hex(key) if isinstance(key, int) else tuple(hex(x) for x in key)
                note = ''
                try:
                    note = decode_shortstring(event.keys[1])
                except Exception as e:
                    pass
                print(f'{hex_key} first occurred in {hex(event.transaction_hash)} {note}')
                print(EventDispatcher.from_calldata(event.keys, event.data))

    event_count = [(key, count) for key, count in event_count.items() if count > 0]
    event_count.sort(key=lambda x: x[1], reverse=True)
    for key, count in event_count:
        event_name = ALL_SYSTEM_EVENTS.get(key, 'Unknown').__name__
        print(f'{event_name}: {count}')
    print('Unknown events:')
    print(unknown_events)


if __name__ == '__main__':
    client, account, dispatcher_contract = setup_starknet_context(prod=True)
    asyncio.run(read_event(client))

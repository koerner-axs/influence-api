import asyncio

from starknet_py.net.client_models import InvokeTransactionV1
from starknet_py.net.full_node_client import FullNodeClient

from influencepy.starknet.net.constants import DISPATCHER_ADDRESS
from influencepy.starknet.net.datatypes import Calldata
from influencepy.starknet.net.dispatcher import SystemEventDispatcher
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
    for _ in range(100):
        events = await client.get_events(addr, continuation_token=events.continuation_token)
        for event in events.events:
            if len(event.keys) != 1:
                continue
            key = event.keys[0]
            if key in event_count:
                event_count[key] += 1
            elif key not in unknown_events:
                unknown_events[key] = event.transaction_hash
                print(f'{hex(key)} first occurred in {hex(event.transaction_hash)}')

    event_count = [(key, count) for key, count in event_count.items() if count > 0]
    event_count.sort(key=lambda x: x[1], reverse=True)
    print(event_count)
    print('Unknown events:')
    print(unknown_events)


if __name__ == '__main__':
    client, account, dispatcher_contract = setup_starknet_context(prod=True)
    asyncio.run(read_event(client))

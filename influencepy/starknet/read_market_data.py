# Read Market Data since launch on Mainnet on 2024-06-27
import asyncio

from starknet_py.net.full_node_client import FullNodeClient

from influencepy.starknet.net.datatypes import Calldata
from influencepy.starknet.net.dispatcher import EventDispatcher
from influencepy.starknet.util.contract import DispatcherContract
from influencepy.starknet.util.rpc import setup_starknet_context


async def read_event(client: FullNodeClient, dispatcher: DispatcherContract):
    print('Read Market Data since launch on Mainnet on 2024-06-27')
    addr = dispatcher.contract.address

    FIRST_LIVE_BLOCK = 652696

    events = await client.get_events(addr)
    for _ in range(10):
        events = await client.get_events(addr, continuation_token=events.continuation_token, chunk_size=100)
        print(f'Got {len(events.events)} events')
        for event in events.events:
            print(event)
            calldata = Calldata(event.data)
            print(EventDispatcher.from_calldata(event.keys, calldata))
            if len(calldata) > 0:
                print(f'Extra data: {calldata}')


if __name__ == '__main__':
    client, account, dispatcher_contract = setup_starknet_context(prod=True)
    asyncio.run(read_event(client, dispatcher_contract))

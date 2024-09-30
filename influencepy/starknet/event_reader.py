import asyncio

from starknet_py.net.full_node_client import FullNodeClient

from influencepy.starknet.net.constants import DISPATCHER_ADDRESS
from influencepy.starknet.net.datatypes import Calldata
from influencepy.starknet.net.dispatcher import EventDispatcher
from influencepy.starknet.util.rpc import setup_starknet_context


async def read_event(client: FullNodeClient):
    addr = DISPATCHER_ADDRESS

    events = await client.get_events(addr)
    for _ in range(10):
        events = await client.get_events(addr, continuation_token=events.continuation_token, chunk_size=100)
        print(f'Got {len(events.events)} events')
        for event in events.events:
            print(event)
            print(EventDispatcher.from_calldata(event.keys, Calldata(event.data)))


if __name__ == '__main__':
    client, account, dispatcher_contract = setup_starknet_context(prod=True)
    asyncio.run(read_event(client))

import asyncio

from starknet_py.net.full_node_client import FullNodeClient

from influencepy.starknet.net.constants import DISPATCHER_ADDRESS
from influencepy.starknet.net.datatypes import Calldata
from influencepy.starknet.net.dispatcher import EventDispatcher
from influencepy.starknet.util.rpc import setup_starknet_context


async def read_event(client: FullNodeClient):
    addr = DISPATCHER_ADDRESS

    events = await client.get_events(addr, keys=[[1172733737439152708200787106475389365980570295937413226161927159884463661807], [1131570551]])
    for _ in range(10):
        events = await client.get_events(addr, keys=[[1172733737439152708200787106475389365980570295937413226161927159884463661807], [1131570551]], continuation_token=events.continuation_token, chunk_size=100)
        print(f'Got {len(events.events)} events')
        for event in events.events:
            calldata = Calldata(event.data)
            print(EventDispatcher.from_calldata(event.keys, calldata))
            if len(calldata) > 0:
                print(f'Extra data: {calldata}')


if __name__ == '__main__':
    client, account, dispatcher_contract = setup_starknet_context(prod=True)
    asyncio.run(read_event(client))

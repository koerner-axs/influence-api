import asyncio

from starknet_py.net.full_node_client import FullNodeClient

from influencepy.starknet.net.constants import DISPATCHER_ADDRESS
from influencepy.starknet.net.datatypes import Calldata
from influencepy.starknet.net.dispatcher import EventDispatcher
from influencepy.starknet.util.rpc import setup_starknet_context


async def read_event(client: FullNodeClient):
    addr = DISPATCHER_ADDRESS

    search_params = {
        'from_block_number': 954123,
        #'to_block_number': 652498,
        'keys': [[1172733737439152708200787106475389365980570295937413226161927159884463661807], [93932703806821]],
    }

    event_count = 0
    events = await client.get_events(addr, **search_params)
    while True:
        events = await client.get_events(addr, continuation_token=events.continuation_token, chunk_size=1024,
                                         **search_params)
        print(f'Got {len(events.events)} events')
        for event in events.events:
            calldata = Calldata(event.data.copy())
            try:
                #print(event.keys, event.data, f'0x{event.transaction_hash:02x}')
                #print(EventDispatcher.from_calldata(event.keys, calldata))
                EventDispatcher.from_calldata(event.keys, calldata)
                event_count += 1
            except Exception as e:
                print('Offending event:', event.keys, event.data, f'0x{event.transaction_hash:02x}')
                print(e)
                print('Success count:', event_count)
                raise e
            if len(calldata) > 0:
                print('Offending event:', event)
                print(f'Extra data: {calldata}')
        print('Successfully parsed events:', event_count)
        print('Last block number', events.events[-1].block_number)
        if events.continuation_token is None:
            print('No more events')
            break


if __name__ == '__main__':
    client, account, dispatcher_contract = setup_starknet_context(prod=True)
    asyncio.run(read_event(client))

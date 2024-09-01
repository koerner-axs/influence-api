import asyncio

from influencepy.starknet.net.structs import Building, Crew
from influencepy.starknet.net.system import ProcessProductsFinish
from influencepy.starknet.net.transaction import MultiInvocationTransaction
from influencepy.starknet.util.contract import DispatcherContract
from influencepy.starknet.util.random_event import handle_random_events
from influencepy.starknet.util.rpc import setup_starknet


async def finish_ref_start_ref(dispatcher: DispatcherContract, crew: Crew, refinery: Building):
    tx = MultiInvocationTransaction()
    tx.append_contract_call(ProcessProductsFinish(
        processor=refinery,
        processor_slot=0x2,  # TODO: What is this?
        caller_crew=crew
    ))
    await handle_random_events(dispatcher, tx, crew)
    calldata = tx.to_calldata()
    print(calldata)

    recovered_tx = MultiInvocationTransaction.from_calldata(calldata)
    print(recovered_tx)


if __name__ == '__main__':
    client, account, dispatcher_contract = setup_starknet()
    asyncio.run(finish_ref_start_ref(dispatcher_contract, Crew(4190), Building(0x32ab)))

import asyncio

from starknet_py.net.account.account import Account

from influencepy.starknet.net.structs import Building, Crew
from influencepy.starknet.net.system import *
from influencepy.starknet.net.transaction import MultiInvocationTransaction
from influencepy.starknet.util.contract import DispatcherContract
from influencepy.starknet.util.random_event import handle_random_events
from influencepy.starknet.util.rpc import setup_starknet_context


async def finish_refinery(dispatcher: DispatcherContract, account: Account,  crew: Crew, refinery: Building):
    tx = MultiInvocationTransaction()
    tx.append_contract_call(ProcessProductsFinish(
        processor=refinery,
        processor_slot=0x1,  # TODO: What is this?
        caller_crew=crew
    ))
    await handle_random_events(dispatcher, tx, crew)
    calldata = tx.to_calldata()
    print(calldata)

    rre_call = tx.get_invocation(0).to_call()
    print(rre_call)
    ppf_call = tx.get_invocation(1).to_call()
    print(ppf_call)

    invoke = await account.sign_invoke_v1([rre_call, ppf_call], max_fee=int(1e14))
    print(invoke)
    #result = await account.client.send_transaction(invoke)
    print(result)
    print('Done')


async def finish_extraction(dispatcher: DispatcherContract, crew: Crew, extractor: Building):
    tx = MultiInvocationTransaction()
    tx.append_contract_call(ExtractResourceFinish(
        extractor=extractor,
        extractor_slot=0x1,  # TODO: What is this?
        caller_crew=crew
    ))
    await handle_random_events(dispatcher, tx, crew)
    calldata = tx.to_calldata()
    print(calldata)

    recovered_tx = MultiInvocationTransaction.from_calldata(calldata)
    print(recovered_tx.invocations)


if __name__ == '__main__':
    client, account, dispatcher_contract = setup_starknet_context()
    asyncio.run(finish_refinery(dispatcher_contract, account, Crew(0x1c47), Building(0x51ad)))
    #asyncio.run(finish_extraction(dispatcher_contract, Crew(4190), Building(0x32ab)))

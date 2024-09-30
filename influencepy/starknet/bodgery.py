import asyncio

from starknet_py.net.account.account import Account

from influencepy.starknet.net.struct import Building, Crew, Deposit
from influencepy.starknet.net.system import *
from influencepy.starknet.net.transaction import MultiInvocationTransaction
from influencepy.starknet.util.contract import DispatcherContract
from influencepy.starknet.util.random_event import handle_random_events
from influencepy.starknet.util.rpc import setup_starknet_context


async def finish_refinery(dispatcher: DispatcherContract, account: Account, crew: Crew, refinery: Building):
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

    # result = await account.client.send_transaction(invoke)
    # print(result)
    print('Done')


async def finish_extraction(dispatcher: DispatcherContract, account: Account, crew: Crew, extractor: Building):
    tx = MultiInvocationTransaction()
    tx.append_contract_call(ExtractResourceFinish(
        extractor=extractor,
        extractor_slot=0x1,  # TODO: What is this?
        caller_crew=crew
    ))
    await handle_random_events(dispatcher, tx, crew)
    calldata = tx.to_calldata()
    print(calldata)

    calls = [tx.get_invocation(i).to_call() for i in range(len(tx.invocations))]
    print(calls)

    invoke = await account.sign_invoke_v1(calls, max_fee=int(1e13))
    print(invoke)

    #result = await account.client.send_transaction(invoke)
    #print(result)
    print('Done')


async def start_core_improvement(dispatcher: DispatcherContract, account: Account, crew: Crew, deposit: Deposit,
                                 core_drill_storage: Building):
    tx = MultiInvocationTransaction()
    tx.append_contract_call(SampleDepositImprove(
        deposit=deposit,
        origin=core_drill_storage,
        origin_slot=0x2,  # TODO: What is this?
        caller_crew=crew
    ))
    await handle_random_events(dispatcher, tx, crew)
    calldata = tx.to_calldata()
    print(calldata)

    calls = [tx.get_invocation(i).to_call() for i in range(len(tx.invocations))]
    print(calls)

    invoke = await account.sign_invoke_v1(calls, max_fee=int(1e13))
    print(invoke)

    #result = await account.client.send_transaction(invoke)
    #print(result)
    print('Done')


async def finish_core_improvement(dispatcher: DispatcherContract, account: Account, crew: Crew, deposit: Deposit):
    tx = MultiInvocationTransaction()
    tx.append_contract_call(SampleDepositFinish(
        deposit=deposit,
        caller_crew=crew
    ))
    await handle_random_events(dispatcher, tx, crew)
    calldata = tx.to_calldata()
    print(calldata)

    calls = [tx.get_invocation(i).to_call() for i in range(len(tx.invocations))]
    print(calls)

    invoke = await account.sign_invoke_v1(calls, max_fee=int(1e13))
    print(invoke)

    # result = await account.client.send_transaction(invoke)
    # print(result)
    print('Done')


if __name__ == '__main__':
    client, account, dispatcher_contract = setup_starknet_context()
    # asyncio.run(finish_refinery(dispatcher_contract, account, Crew(0x1c47), Building(0x51ad)))
    # asyncio.run(finish_extraction(dispatcher_contract, account, Crew(0x1300), Building(0x1537c)))
    asyncio.run(start_core_improvement(dispatcher_contract, account, Crew(0x1300), Deposit(0x1537c), Building(0x305d)))
    # asyncio.run(finish_core_improvement(dispatcher_contract, account, Crew(0x1300), Deposit(0x1537c)))

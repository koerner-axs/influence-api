import asyncio

from influencepy.starknet.net.structs import Lot, Crew
from influencepy.starknet.net.system import TransferPrepaidAgreement
from influencepy.starknet.net.transaction import MultiInvocationTransaction
from influencepy.starknet.util.random_event import handle_random_events
from influencepy.starknet.util.rpc import setup_starknet_context


async def transfer_lot_lease():
    lot_to_transfer = 238_682
    asteroid = 1
    old_owner = Crew(4367)
    new_owner = Crew(4373)

    tx = MultiInvocationTransaction()
    tx.append_contract_call(TransferPrepaidAgreement(Lot(lot_to_transfer, asteroid),
                                                     1,
                                                     old_owner,
                                                     new_owner,
                                                     old_owner))
    calldata = tx.to_calldata(None)
    print(calldata)

    call = tx.get_invocation(0).to_call()
    print(call)

    invoke = await account.sign_invoke_v1([call], max_fee=int(4e13))
    print(invoke)

    result = await account.client.send_transaction(invoke)
    print(result)
    print('Done')


if __name__ == '__main__':
    client, account, dispatcher_contract = setup_starknet_context()
    asyncio.run(transfer_lot_lease())

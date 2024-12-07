import asyncio

from starknet_py.net.client_models import TransactionExecutionStatus

from influencepy.starknet.net.structs import Lot, Crew
from influencepy.starknet.net.system import TransferPrepaidAgreement
from influencepy.starknet.net.transaction import MultiInvocationTransaction
from influencepy.starknet.util.rpc import setup_starknet_context


async def transfer_lot_lease(lot: Lot, old_owner: Crew, new_owner: Crew):
    tx = MultiInvocationTransaction()
    tx.append_contract_call(TransferPrepaidAgreement(lot, 1, old_owner, new_owner, old_owner))

    call = tx.get_invocation(0).to_call()
    #print(call)

    invoke = await account.sign_invoke_v1([call], max_fee=int(4e13))
    #print(invoke)

    result = await account.client.send_transaction(invoke)
    print(result)
    print(f'Sent transaction 0x{result.transaction_hash:02x}. Awaiting acceptance..')
    result = await account.client.wait_for_tx(result.transaction_hash)
    if result.execution_status == TransactionExecutionStatus.SUCCEEDED:
        print(f'Transaction succeeded, cost={result.actual_fee.amount}')
    else:
        print(f'Transaction reverted: {result.revert_reason}, cost={result.actual_fee.amount}')

if __name__ == '__main__':
    client, account, dispatcher_contract = setup_starknet_context()
    #for id in [1213508]:
    for id in [941295, 1194632, 1191438, 1188244, 1193035, 1186647, 1189841, 1219896, 1215715, 1217312]:
        asyncio.run(transfer_lot_lease(Lot(id, 1), Crew(4367), Crew(4373)))

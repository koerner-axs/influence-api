import asyncio

from starknet_py.net.account.account import Account

from influencepy.starknet.net.constants import DISPATCHER_ADDRESS
from influencepy.starknet.net.contract_call import SwayTransferWithConfirmation
from influencepy.starknet.net.struct import Crew, Entity, EntityId
from influencepy.starknet.net.system import AcceptPrepaidAgreement
from influencepy.starknet.net.transaction import MultiInvocationTransaction
from influencepy.starknet.util.rpc import setup_starknet_context


async def transfer(account: Account):
    """
    [
  "0x5acb0547f4b06e5db4f73f5b6ea7425e9b59b6adc885ed8ecc4baeefae8b8d8",
  "0x1ad274800",
  "0x298a8ad77e6872cb28971826af4dd3b187248afd88cdd9b268f3534ba95c9ad",
  "0x517567ac7026ce129c950e6e113e437aa3c83716cd61481c6bb8c5057e6923e"
]
    [
  "0x4163636570745072657061696441677265656d656e74",
  "0x8",
  "0x4",
  "0x14474b00000001",
  "0x1",
  "0x1",
  "0x1115",
  "0x278d00",
  "0x1",
  "0x1115"
]
    """
    tx = MultiInvocationTransaction()
    tx.append_contract_call(SwayTransferWithConfirmation(
        recipient=0x5acb0547f4b06e5db4f73f5b6ea7425e9b59b6adc885ed8ecc4baeefae8b8d8,
        amount=0x01ad274800,
        memo=0x479b25328ea539f7fd805d5e7f5f1929319ecb22d68400da2cae45d0032eb6c,
        consumer=DISPATCHER_ADDRESS
    ))
    tx.append_contract_call(AcceptPrepaidAgreement(
        target=Entity(EntityId.LOT, 1121017 * 2**32 + 1),
        permission=0x1,
        permitted=Crew(3369),
        term=0x278d00,  # 30 days
        caller_crew=Crew(3369)
    ))
    calldata = tx.to_calldata()
    print(calldata)

    result = await account.execute_v1(calls=[
        c.to_call() for c in tx.invocations
    ], max_fee=int(1e14))

    print(result)

    recovered_tx = MultiInvocationTransaction.from_calldata(calldata)
    print(recovered_tx)


if __name__ == '__main__':
    client, account, dispatcher_contract = setup_starknet_context(prod=False)
    asyncio.run(transfer(account))

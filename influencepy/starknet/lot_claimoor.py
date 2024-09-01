import asyncio

from influencepy.starknet.net.contract_call import SwayTransferWithConfirmation
from influencepy.starknet.net.structs import Crew, Entity, EntityId
from influencepy.starknet.net.system import AcceptPrepaidAgreement
from influencepy.starknet.net.transaction import MultiInvocationTransaction
from influencepy.starknet.util.rpc import setup_starknet


async def transfer():
    """
    [
  "0x795a0690f51905f34f2d52b482e18ebc39b87638e30eb4bd4fc65ff67a7beec",
  "0xaba95000",
  "0x479b25328ea539f7fd805d5e7f5f1929319ecb22d68400da2cae45d0032eb6c",
  "0x422d33a3638dcc4c62e72e1d6942cd31eb643ef596ccac2351e0e21f6cd4bf4"
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
        recipient=0x795a0690f51905f34f2d52b482e18ebc39b87638e30eb4bd4fc65ff67a7beec,
        amount=0xaba95000,
        memo=0x479b25328ea539f7fd805d5e7f5f1929319ecb22d68400da2cae45d0032eb6c,
        consumer=0x422d33a3638dcc4c62e72e1d6942cd31eb643ef596ccac2351e0e21f6cd4bf4
    ))
    tx.append_contract_call(AcceptPrepaidAgreement(
        target=Entity(EntityId.LOT, 0x145889_00000001),
        permission=0x1,
        permitted=Crew(4373),
        term=0x278d00,  # 30 days
        caller_crew=Crew(4373)
    ))
    calldata = tx.to_calldata()
    print(calldata)

    recovered_tx = MultiInvocationTransaction.from_calldata(calldata)
    print(recovered_tx)


if __name__ == '__main__':
    client, account, dispatcher_contract = setup_starknet()
    asyncio.run(transfer())

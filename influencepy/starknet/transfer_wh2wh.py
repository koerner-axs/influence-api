import asyncio

from influencepy.starknet.net.struct import Building, Crew, InventoryItem
from influencepy.starknet.net.system import SendDelivery, ResolveRandomEvent
from influencepy.starknet.net.transaction import MultiInvocationTransaction
from influencepy.starknet.util.rpc import setup_starknet_context


async def transfer():
    """
    First run_system calldata:
    [
      "0x5265736f6c766552616e646f6d4576656e74",
      "0x3",
      "0x0",
      "0x1",
      "0x1300"
    ]
    Second run_system calldata:
    [
      "0x53656e6444656c6976657279",
      "0xb",
      "0x5",
      "0x32ab",
      "0x2",
      "0x1",
      "0x13",
      "0x125a9ca",
      "0x5",
      "0x43dd",
      "0x2",
      "0x1",
      "0x1300"
    ]
    """
    tx = MultiInvocationTransaction()
    tx.append_contract_call(ResolveRandomEvent(choice=0, caller_crew=Crew(0x1300)))
    tx.append_contract_call(SendDelivery(
        origin=Building(0x32ab),
        origin_slot=0x2,
        products=[InventoryItem(0x13, 0x125a9ca)],
        dest=Building(0x43dd),
        dest_slot=0x2,
        caller_crew=Crew(0x1300)
    ))
    calldata = tx.to_calldata()
    print(calldata)

    recovered_tx = MultiInvocationTransaction.from_calldata(calldata)
    print(recovered_tx)


if __name__ == '__main__':
    client, account, dispatcher_contract = setup_starknet_context()
    asyncio.run(transfer())

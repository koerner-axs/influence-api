import asyncio
import os

from starknet_py.contract import Contract
from starknet_py.net.account.account import Account
from starknet_py.net.full_node_client import FullNodeClient
from starknet_py.net.models import StarknetChainId
from starknet_py.net.signer.stark_curve_signer import KeyPair

from influencepy.starknet.net.constants import DISPATCHER_ADDRESS
from influencepy.starknet.net.schema import MultiInvocationTransaction
from influencepy.starknet.net.structs import Building, Crew, InventoryItem
from influencepy.starknet.net.system import SendDelivery, ResolveRandomEvent

full_node_address = 'https://starknet-mainnet.g.alchemy.com/starknet/version/rpc/v0_7/Dx_Csa1pBUwBeP3qSu5UnzC882cfOE5d'

MAIN_ACCOUNT = '0x00780f5ab2151d7c46a08a87c445a1012fa376a9c0e1df22e949d3d32740710f'
MAIN_ACCOUNT_PRIVATE_KEY = os.environ.get('INFLUENCE_MAIN_KEY')
if MAIN_ACCOUNT_PRIVATE_KEY is None:
    raise ValueError('INFLUENCE_MAIN_KEY environment variable not set')


async def setup_starknet():
    client = FullNodeClient(node_url=full_node_address)
    account = Account(
        address=MAIN_ACCOUNT,
        client=client,
        key_pair=KeyPair.from_private_key(MAIN_ACCOUNT_PRIVATE_KEY),
        chain=StarknetChainId.MAINNET
    )
    dispatcher_contract = await Contract.from_address(
        provider=account,
        address=DISPATCHER_ADDRESS
    )
    return client, account, dispatcher_contract


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
    client, account, dispatcher_contract = asyncio.run(setup_starknet())
    asyncio.run(transfer())

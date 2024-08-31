import asyncio
import os

from starknet_py.contract import Contract
from starknet_py.net.account.account import Account
from starknet_py.net.client_models import InvokeTransactionV1
from starknet_py.net.full_node_client import FullNodeClient
from starknet_py.net.models import StarknetChainId
from starknet_py.net.signer.stark_curve_signer import KeyPair

from influencepy.starknet.net.constants import DISPATCHER_ADDRESS
from influencepy.starknet.net.datatypes import Calldata
from influencepy.starknet.net.transaction import MultiInvocationTransaction

full_node_address = 'https://starknet-mainnet.g.alchemy.com/starknet/version/rpc/v0_7/Dx_Csa1pBUwBeP3qSu5UnzC882cfOE5d'

FILL_SELL_ORDER_TX = 0x05ab19f45ab1cb4ac3db28eae249a4546f684781b1904fc3f21f4b083e1feb85
PROCESS_PROUCTS_FINISH_TX = 0x02fe36eea7dc3628c9c6385f5935737b784008555168a9b9291b08fca6bc6ecd

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


async def read_transaction(client: FullNodeClient):
    tx = await client.get_transaction('0x019ef3f6f03b280f7d48b2c896f4a833a318e04850fea15d9ba992e86e220577')
    #tx = await client.get_transaction('0x01f5b7e92b51ec6492b6645bbea8fe098d2f156083ef5cc3cad3f878fb876025')
    #tx = await client.get_transaction('0x293357fb4f6d2f63e008939c84abcf7d4f3e5a73dab47ccf8da56776fbf6b6a')
    if not isinstance(tx, InvokeTransactionV1):
        raise ValueError('Transaction is not an InvokeTransactionV1')
    calldata = Calldata(tx.calldata)
    #for i in range(45):
    #    x = calldata.pop_int()
    #    if x < 2 ** 250:
    #        print(f'{i}: {x} = {felt.decode_shortstring(x)}')
    #    else:
    #        print(f'{i}: {x}')
    multi_invocation = MultiInvocationTransaction.from_calldata(calldata)
    print(multi_invocation)


if __name__ == '__main__':
    client, account, dispatcher_contract = asyncio.run(setup_starknet())
    asyncio.run(read_transaction(client))

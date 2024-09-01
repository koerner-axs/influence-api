import asyncio

from starknet_py.net.client_models import InvokeTransactionV1
from starknet_py.net.full_node_client import FullNodeClient

from influencepy.starknet.net.datatypes import Calldata
from influencepy.starknet.net.transaction import MultiInvocationTransaction
from influencepy.starknet.util.rpc import setup_starknet

FILL_SELL_ORDER_TX = 0x05ab19f45ab1cb4ac3db28eae249a4546f684781b1904fc3f21f4b083e1feb85
PROCESS_PROUCTS_FINISH_TX = 0x02fe36eea7dc3628c9c6385f5935737b784008555168a9b9291b08fca6bc6ecd


async def read_transaction(client: FullNodeClient):
    tx = await client.get_transaction('0x019ef3f6f03b280f7d48b2c896f4a833a318e04850fea15d9ba992e86e220577')
    # tx = await client.get_transaction('0x01f5b7e92b51ec6492b6645bbea8fe098d2f156083ef5cc3cad3f878fb876025')
    # tx = await client.get_transaction('0x293357fb4f6d2f63e008939c84abcf7d4f3e5a73dab47ccf8da56776fbf6b6a')
    if not isinstance(tx, InvokeTransactionV1):
        raise ValueError('Transaction is not an InvokeTransactionV1')
    calldata = Calldata(tx.calldata)
    multi_invocation = MultiInvocationTransaction.from_calldata(calldata)
    print(multi_invocation)


if __name__ == '__main__':
    client, account, dispatcher_contract = setup_starknet(prod=True)
    asyncio.run(read_transaction(client))

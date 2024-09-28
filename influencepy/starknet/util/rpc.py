import os

from starknet_py.net.account.account import Account
from starknet_py.net.full_node_client import FullNodeClient
from starknet_py.net.models import StarknetChainId
from starknet_py.net.signer.stark_curve_signer import KeyPair

from influencepy.starknet.util.contract import DispatcherContract


def _get_account(prod: bool):
    var_name = 'INFLUENCE_PROD_ACCOUNT' if prod else 'INFLUENCE_TEST_ACCOUNT'
    account_address = os.environ.get(var_name)
    if account_address is None:
        raise ValueError(f'{var_name} environment variable not set')
    return account_address


def _get_account_private_key(prod: bool):
    var_name = 'INFLUENCE_PROD_PRIVATE_KEY' if prod else 'INFLUENCE_TEST_PRIVATE_KEY'
    private_key = os.environ.get(var_name)
    if private_key is None:
        raise ValueError(f'{var_name} environment variable not set')
    return private_key


def setup_account(client: FullNodeClient, prod: bool = True, account_address: str = None,
                  private_key: str = None) -> Account:
    if account_address is None:
        account_address = _get_account(prod)
    if private_key is None:
        private_key = _get_account_private_key(prod)
    return Account(
        address=account_address,
        client=client,
        key_pair=KeyPair.from_private_key(private_key),
        chain=StarknetChainId.MAINNET if prod else StarknetChainId.SEPOLIA
    )


def _get_full_node_address(prod: bool = True):
    var_name = 'STARKNET_PROD_RPC_NODE' if prod else 'STARKNET_TEST_RPC_NODE'
    full_node_address = os.environ.get(var_name)
    if full_node_address is None:
        raise ValueError(f'{var_name} environment variable not set')
    return full_node_address


class StarknetContext:
    def __init__(self, client: FullNodeClient, account: Account, dispatcher_contract: DispatcherContract):
        self.client = client
        self.account = account
        self.dispatcher_contract = dispatcher_contract


def setup_starknet_context(prod: bool = True, full_node_address: str = None):
    if full_node_address is None:
        full_node_address = _get_full_node_address(prod)
    client = FullNodeClient(node_url=full_node_address)

    account = setup_account(client, prod)

    dispatcher_contract = DispatcherContract(account)
    return client, account, dispatcher_contract

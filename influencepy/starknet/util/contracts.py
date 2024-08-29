import json
import os
import tempfile

from starknet_py.contract import Contract
from starknet_py.contract_utils import _unpack_provider
from starknet_py.net.account.account import Account
from starknet_py.net.client import Client
from starknet_py.proxy.contract_abi_resolver import ContractAbiResolver, ProxyConfig

from influencepy.starknet.net.constants import DISPATCHER_ADDRESS

TEMP_BASE_DIR = os.path.join(tempfile.gettempdir(), 'influencepy')
DISPATCHER_ABI = os.path.join(TEMP_BASE_DIR, 'dispatcher_abi.json')


def _get_dispatcher_abi():
    if not os.path.exists(DISPATCHER_ABI):
        return None
    with open(DISPATCHER_ABI, 'r') as f:
        return json.load(f)


def _set_dispatcher_abi(abi):
    os.makedirs(TEMP_BASE_DIR, exist_ok=True)
    with open(DISPATCHER_ABI, 'w') as f:
        json.dump(abi, f)


async def get_dispatcher_contract(provider: Client | Account, address: int = DISPATCHER_ADDRESS):
    abi = _get_dispatcher_abi()
    if abi is None:
        client, _ = _unpack_provider(provider)
        print('Resolving dispatcher contract ABI..')
        abi, cairo_version = await ContractAbiResolver(
            address=address, client=client, proxy_config=ProxyConfig()
        ).resolve()
        _set_dispatcher_abi(abi)
    return Contract(address=address, abi=abi, provider=provider)

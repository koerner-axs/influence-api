import asyncio
import json
import os
import tempfile
import time
from typing import Any, List

from starknet_py.contract import Contract
from starknet_py.hash.selector import get_selector_from_name
from starknet_py.net.account.account import Account
from starknet_py.net.client import Client
from starknet_py.net.client_models import Call
from starknet_py.proxy.contract_abi_resolver import ContractAbiResolver, ProxyConfig

from influencepy.starknet.net.constants import DISPATCHER_ADDRESS
from influencepy.starknet.net.schema import SystemCall

TEMP_BASE_DIR = os.path.join(tempfile.gettempdir(), 'influencepy')
DISPATCHER_ABI = os.path.join(TEMP_BASE_DIR, 'dispatcher_abi.json')


def _unpack_provider(provider: Client | Account) -> tuple[Client, Account | None]:
    if isinstance(provider, Account):
        return provider.client, provider
    return provider, None


def _get_dispatcher_abi():
    if not os.path.exists(DISPATCHER_ABI):
        return None
    created_at = os.stat(DISPATCHER_ABI).st_ctime
    if created_at < (time.time() - 72 * 3600):
        os.remove(DISPATCHER_ABI)
        return None
    print('Using cached dispatcher contract ABI..')
    with open(DISPATCHER_ABI, 'r') as f:
        return json.load(f)


def _set_dispatcher_abi(abi):
    os.makedirs(TEMP_BASE_DIR, exist_ok=True)
    with open(DISPATCHER_ABI, 'w') as f:
        json.dump(abi, f)


def get_dispatcher_contract(provider: Client | Account, address: int = DISPATCHER_ADDRESS,
                            reload_abi: bool = False):
    abi = _get_dispatcher_abi()
    if abi is None or reload_abi:
        client, _ = _unpack_provider(provider)
        print('Resolving dispatcher contract ABI..')
        abi, cairo_version = asyncio.run(ContractAbiResolver(
            address=address, client=client, proxy_config=ProxyConfig()
        ).resolve())
        _set_dispatcher_abi(abi)
    return Contract(address=address, abi=abi, provider=provider)


class DispatcherContract:
    def __init__(self, provider: Client | Account, address: int = DISPATCHER_ADDRESS, reload_abi: bool = False):
        self.client, _ = _unpack_provider(provider)
        self.contract = get_dispatcher_contract(self.client, address, reload_abi)

    async def run_system(self, system_call: SystemCall) -> List[int]:
        return await self.client.call_contract(system_call.to_call())

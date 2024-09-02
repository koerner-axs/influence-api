import asyncio
import json
import os
import tempfile
import time
from typing import Any, List, Dict

from starknet_py.contract import Contract
from starknet_py.net.account.account import Account
from starknet_py.net.client import Client
from starknet_py.proxy.contract_abi_resolver import ContractAbiResolver, ProxyConfig

from influencepy.starknet.net.constants import DISPATCHER_ADDRESS

TEMP_BASE_DIR = os.path.join(tempfile.gettempdir(), 'influencepy')
DISPATCHER_ABI = os.path.join(TEMP_BASE_DIR, 'dispatcher_abi.json')
SWAY_ABI = os.path.join(TEMP_BASE_DIR, 'sway_abi.json')


def _unpack_provider(provider: Client | Account) -> tuple[Client, Account | None]:
    if isinstance(provider, Account):
        return provider.client, provider
    return provider, None


def _get_abi(file):
    if not os.path.exists(file):
        return None
    created_at = os.stat(file).st_ctime
    if created_at < (time.time() - 72 * 3600):
        os.remove(file)
        return None
    print('Using cached dispatcher contract ABI..')
    with open(file, 'r') as f:
        return json.load(f)


def _store_abi(abi):
    os.makedirs(TEMP_BASE_DIR, exist_ok=True)
    with open(DISPATCHER_ABI, 'w') as f:
        json.dump(abi, f)


def get_dispatcher_contract(provider: Client | Account, address: int = DISPATCHER_ADDRESS,
                            reload_abi: bool = False) -> Contract:
    abi = _get_dispatcher_abi(DISPATCHER_ABI)
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

    async def run_system(self, system_call: "SystemCall") -> List[int]:
        return await self.client.call_contract(system_call.to_call())


class SwayContract:
    def __init__(self, provider: Client | Account, address: int, selectors: Dict[str, int]):
        self.client, _ = _unpack_provider(provider)
        self.contract = get_dispatcher_contract(self.client, address, reload_abi)
        self.selectors = selectors

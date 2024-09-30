import asyncio
from typing import List

from influencepy.starknet.net.struct import Crew
from influencepy.starknet.net.system import ResolveRandomEvent, CheckForRandomEvent
from influencepy.starknet.net.transaction import MultiInvocationTransaction
from influencepy.starknet.util.contract import DispatcherContract


async def check_needs_resolve_random_event(dispatcher: DispatcherContract, crew: Crew) -> bool:
    return await CheckForRandomEvent(crew).query(dispatcher)


async def handle_random_events(dispatcher: DispatcherContract, tx: MultiInvocationTransaction,
                               crews: Crew | List[Crew]):
    if isinstance(crews, Crew):
        crews = [crews]
    for crew in crews:
        needs_resolution = await check_needs_resolve_random_event(dispatcher, crew)
        if needs_resolution:
            tx.prepend_contract_call(ResolveRandomEvent(choice=0, caller_crew=crew))

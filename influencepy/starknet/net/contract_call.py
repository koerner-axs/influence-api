from dataclasses import dataclass
from typing import List

from starknet_py.net.client_models import Call

from influencepy.starknet.net.constants import SWAY_TOKEN_ADDRESS, SWAY_TRANSFER_WITH_CONFIRMATION_SELECTOR
from influencepy.starknet.net.datatypes import Calldata, ContractAddress, u128, felt252
from influencepy.starknet.net.schema import Schema


class ContractCall(Schema):
    _contract_address: int
    _selector: int

    def _to_callargs(self, calldata: Calldata | None = None) -> Calldata:
        return super().to_calldata(calldata)

    def to_calldata(self, calldata: Calldata = None) -> Calldata:
        if calldata is None:
            calldata = Calldata([])
        calldata.push_int(self.__class__._contract_address)
        calldata.push_int(self.__class__._selector)
        # TODO: missing the function name and arg count
        calldata.count_push_len_extend(self._to_callargs())
        return calldata

    def to_call(self) -> Call:
        calldata = self._to_callargs()
        return Call(
            to_addr=self.__class__._contract_address,
            selector=self.__class__._selector,
            calldata=calldata.data
        )


class UnknownContractCall(ContractCall):
    def __init__(self, calldata: List[int], contract_address: int | str, selector: int | str):
        self.calldata = calldata
        self.contract_address = contract_address
        self.selector = selector

    @classmethod
    def from_calldata(cls, calldata: Calldata, **kwargs) -> "UnknownContractCall":
        """ Pops the argument length and all arguments from the calldata and stores it.
        No further parsing is done. """
        data = []
        for _ in range(kwargs['arg_count']):
            data.append(calldata.pop_int())
        return UnknownContractCall(calldata=data, contract_address=kwargs['contract_address'],
                                   selector=kwargs['selector'])

    def __repr__(self):
        return f'UnknownContractCall(to={hex(self.contract_address)}, selector={hex(self.selector)}, calldata={self.calldata})'

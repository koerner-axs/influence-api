from dataclasses import dataclass  # noqa: F401
from typing import List  # noqa: F401

from starknet_py.hash.selector import get_selector_from_name
from starknet_py.net.client_models import Call

from influencepy.starknet.net.constants import DISPATCHER_ADDRESS
from influencepy.starknet.net.contract_call import ContractCall
from influencepy.starknet.net.datatypes import *
from influencepy.starknet.net.structs import *
from influencepy.starknet.util.contract import DispatcherContract  # noqa: F401


class RunSystem(ContractCall):
    _contract_address: int = DISPATCHER_ADDRESS  # TODO: maybe remove
    _selector: int = get_selector_from_name('run_system')  # TODO: maybe remove
    _function_name: str

    def to_calldata(self, calldata: Calldata = None) -> Calldata:
        if calldata is None:
            calldata = Calldata([])
        calldata.push_int(self.__class__._contract_address)
        calldata.push_int(self.__class__._selector)
        args_calldata = super(ContractCall, self).to_calldata(None)
        args_calldata.count_prepend_len()
        args_calldata.prepend_string(self.__class__._function_name)
        calldata.count_push_len_extend(args_calldata)
        return calldata

    def to_call(self) -> Call:
        calldata = Calldata([])
        calldata.push_string(self.__class__._function_name)
        calldata.count_push_len_extend(self._to_callargs())
        return Call(
            to_addr=self.__class__._contract_address,
            selector=self.__class__._selector,
            calldata=calldata.data
        )


### GENERATED BLOCK ###


class UnknownSystemCall(RunSystem):
    def __init__(self, calldata: List[int], function_name: str):
        self.calldata = calldata
        self.function_name = function_name

    @classmethod
    def from_calldata(cls, calldata: Calldata, **kwargs) -> "UnknownSystemCall":
        """ Pops the argument length and all arguments from the calldata and stores it.
        No further parsing is done. """
        data = []
        for _ in range(kwargs['arg_count']):
            data.append(calldata.pop_int())
        return UnknownSystemCall(calldata=data, function_name=kwargs['function_name'])

    def __repr__(self):
        return f'UnknownSystemCall(function_name={self.function_name}, calldata={self.calldata})'

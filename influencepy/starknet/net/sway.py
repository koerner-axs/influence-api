from dataclasses import dataclass

from starknet_py.hash.selector import get_selector_from_name
from starknet_py.net.client_models import Call

from influencepy.starknet.net.constants import SWAY_TOKEN_ADDRESS_PROD
from influencepy.starknet.net.contract_call import ContractCall
from influencepy.starknet.net.datatypes import Calldata, ContractAddress, u128, felt252


class SwayTokenContractCall(ContractCall):
    _contract_address: int = SWAY_TOKEN_ADDRESS_PROD
    _selector: int

    def to_calldata(self, calldata: Calldata = None) -> Calldata:
        # TODO: fix
        if calldata is None:
            calldata = Calldata([])
        calldata.push_int(self.__class__._contract_address)
        args_calldata = super(ContractCall, self).to_calldata(None)
        args_calldata.count_prepend_len()
        calldata.count_push_len_extend(args_calldata)
        return calldata

    def to_call(self) -> Call:
        # TODO: fix
        calldata = Calldata([])
        calldata.count_push_len_extend(self._to_callargs())
        return Call(
            to_addr=self.__class__._contract_address,
            selector=self.__class__._selector,
            calldata=calldata.data
        )


@dataclass
class SwayTransferWithConfirmation(SwayTokenContractCall):
    recipient: ContractAddress
    amount: u128
    memo: felt252
    consumer: ContractAddress
    _selector: int = get_selector_from_name('transfer_with_confirmation')


@dataclass
class SwayTransferFromWithConfirmation(SwayTokenContractCall):
    sender: ContractAddress
    recipient: ContractAddress
    amount: u128
    memo: felt252
    consumer: ContractAddress
    _selector: int = get_selector_from_name('transfer_from_with_confirmation')


@dataclass
class SwayConfirmReceipt(SwayTokenContractCall):
    sender: ContractAddress
    recipient: ContractAddress
    amount: u128
    memo: felt252
    _selector: int = get_selector_from_name('confirm_receipt')


@dataclass
class SwayAllowance(SwayTokenContractCall):
    owner: ContractAddress
    spender: ContractAddress
    # TODO: declare output type of u256
    _selector: int = get_selector_from_name('allowance')


@dataclass
class SwayApprove(SwayTokenContractCall):
    spender: ContractAddress
    amount: u128
    # TODO: declare output type of bool
    _selector: int = get_selector_from_name('approve')


@dataclass
class SwayBalanceOf(SwayTokenContractCall):
    account: ContractAddress
    # TODO: declare output type of u256
    _selector: int = get_selector_from_name('balance_of')


@dataclass
class DecreaseAllowance(SwayTokenContractCall):
    spender: ContractAddress
    subtracted_value: u128
    _selector: int = get_selector_from_name('decrease_allowance')


@dataclass
class IncreaseAllowance(SwayTokenContractCall):
    spender: ContractAddress
    added_value: u128
    _selector: int = get_selector_from_name('increase_allowance')


@dataclass
class SwayTransfer(SwayTokenContractCall):
    recipient: ContractAddress
    amount: u128
    # TODO: declare output type of bool
    _selector: int = get_selector_from_name('transfer')


@dataclass
class SwayTransferFrom(SwayTokenContractCall):
    sender: ContractAddress
    recipient: ContractAddress
    amount: u128
    # TODO: declare output type of bool
    _selector: int = get_selector_from_name('transfer_from')

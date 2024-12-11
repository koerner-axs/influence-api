from influencepy.starknet.net.contract_call import UnknownContractCall
from influencepy.starknet.net.event import *
from influencepy.starknet.net.parser.component_updated import ComponentUpdatedEventParser
from influencepy.starknet.net.sway import *
from influencepy.starknet.net.system import *


class RunSystemDispatcher(Schema):
    _contract_address: int = DISPATCHER_ADDRESS  # TODO: maybe remove
    _selector: int = get_selector_from_name('run_system')
    _variants: Dict[str, RunSystem | List[RunSystem]] = ALL_SYSTEMS

    @classmethod
    def from_calldata(cls, calldata: Calldata, **kwargs) -> Schema:
        function_name = calldata.pop_string()
        arg_count = calldata.pop_int()
        variant: Schema = cls._variants.get(function_name, UnknownSystemCall)
        kwargs.update({'function_name': function_name, 'arg_count': arg_count})
        return variant.from_calldata(calldata, **kwargs)


class DispatcherContractCallDispatcher(Schema):
    _contract_address: int = DISPATCHER_ADDRESS
    _variants: Dict[int, Schema] = {
        RunSystemDispatcher._selector: RunSystemDispatcher
    }

    @classmethod
    def from_calldata(cls, calldata: Calldata, **kwargs) -> Schema:
        selector = calldata.pop_int()
        arg_count = calldata.pop_int()
        variant: Schema = cls._variants.get(selector, UnknownContractCall)
        kwargs.update({'selector': selector, 'arg_count': arg_count})
        return variant.from_calldata(calldata, **kwargs)


class SwayTokenContractCallDispatcher(Schema):
    _contract_address: int = SwayTokenContractCall._contract_address
    _variants: Dict[int, SwayTokenContractCall] = {
        SwayTransferWithConfirmation._selector: SwayTransferWithConfirmation,
        SwayTransferFromWithConfirmation._selector: SwayTransferFromWithConfirmation,
        SwayConfirmReceipt._selector: SwayConfirmReceipt,
        SwayAllowance._selector: SwayAllowance,
        SwayApprove._selector: SwayApprove,
        SwayBalanceOf._selector: SwayBalanceOf,
        DecreaseAllowance._selector: DecreaseAllowance,
        IncreaseAllowance._selector: IncreaseAllowance,
        SwayTransfer._selector: SwayTransfer,
        SwayTransferFrom._selector: SwayTransferFrom
    }

    @classmethod
    def from_calldata(cls, calldata: Calldata, **kwargs) -> ContractCall:
        selector = calldata.pop_int()
        arg_count = calldata.pop_int()
        variant: ContractCall = cls._variants.get(selector, UnknownContractCall)
        kwargs.update({'selector': selector, 'arg_count': arg_count})
        return variant.from_calldata(calldata, **kwargs)


class ContractCallDispatcher(Schema):
    _variants: Dict[int, Schema] = {
        DispatcherContractCallDispatcher._contract_address: DispatcherContractCallDispatcher,
        SwayTokenContractCall._contract_address: SwayTokenContractCallDispatcher
    }

    @classmethod
    def from_calldata(cls, calldata: Calldata, **kwargs) -> Schema:
        contract_address = calldata.pop_int()
        if contract_address in cls._variants:
            variant: Schema = cls._variants[contract_address]
            kwargs.update({'contract_address': contract_address})
            return variant.from_calldata(calldata, **kwargs)
        else:
            selector = calldata.pop_int()
            arg_count = calldata.pop_int()
            kwargs.update({'contract_address': contract_address, 'selector': selector, 'arg_count': arg_count})
            return UnknownContractCall.from_calldata(calldata, **kwargs)


class SystemEventDispatcher:
    _variants: Dict[int, SystemEvent] = ALL_SYSTEM_EVENTS

    @classmethod
    def from_calldata(cls, key: int, calldata: Calldata, **kwargs) -> SystemEvent:
        if key not in cls._variants:
            return UnknownSystemEvent([key], calldata)
        return cls._variants[key].from_calldata(calldata, **kwargs)


class ComponentUpdatedDispatcher:
    _variants: Dict[str, ComponentUpdated | List[ComponentUpdated]] = ALL_COMPONENT_UPDATED

    @classmethod
    def from_calldata(cls, keys: List[int], calldata: Calldata, **kwargs) -> "ComponentUpdated":
        return ComponentUpdatedEventParser()(keys, calldata, **kwargs)


class EventDispatcher:
    @classmethod
    def from_calldata(cls, keys: List[int], calldata: Calldata, **kwargs):
        # TODO: does this if make sense?
        if len(keys) == 1:
            return SystemEventDispatcher.from_calldata(keys[0], calldata, **kwargs)
        if keys[0] == ComponentUpdated._key:
            return ComponentUpdatedDispatcher.from_calldata(keys, calldata)
        return UnknownEvent(keys, calldata)

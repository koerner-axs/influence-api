from dataclasses import dataclass
from typing import List, get_origin, get_args, Any, Dict, Tuple

from influencepy.starknet.net.constants import DISPATCHER_ADDRESS, DISPATCHER_RUN_SYSTEM_SELECTOR, SWAY_TOKEN_ADDRESS, \
    SWAY_TRANSFER_WITH_CONFIRMATION_SELECTOR
from influencepy.starknet.net.datatypes import Calldata, ContractAddress, u128, felt252, BasicType, is_auto_convertible


class Schema(BasicType):
    def to_calldata(self, calldata: Calldata = None) -> Calldata:
        if calldata is None:
            calldata = Calldata([])
        for key, field_type in self.__annotations__.items():
            value = getattr(self, key)
            if isinstance(field_type, type) and issubclass(field_type, BasicType):
                field_type.to_calldata(value, calldata)
            elif get_origin(field_type) == list:
                field_type = get_args(field_type)[0]
                self._list_to_calldata(value, field_type, calldata)
            else:
                raise NotImplementedError(f'Unsupported field type "{field_type}" for field "{key}"')
        return calldata

    @classmethod
    def from_calldata(cls, calldata: Calldata, **kwargs) -> "Schema":
        instance = cls.__new__(cls)
        for key, field_type in cls.__annotations__.items():
            if isinstance(field_type, type) and issubclass(field_type, BasicType):
                setattr(instance, key, field_type.from_calldata(calldata))
            elif get_origin(field_type) == list:
                field_type = get_args(field_type)[0]
                setattr(instance, key, cls._list_from_calldata(field_type, calldata))
            else:
                raise NotImplementedError(f'Unsupported field type "{field_type}" for field "{key}"')
        if '__post_init__' in cls.__dict__:
            instance.__post_init__(instance)
        return instance

    @staticmethod
    def _list_to_calldata(list_: list, element_type, calldata: Calldata):
        calldata.push_int(len(list_))
        for index in range(len(list_)):
            try:
                list_[index].to_calldata(calldata)
            except Exception as e:
                raise ValueError(f"Error while serializing List[{element_type}] at index {index}: {e}")

    @staticmethod
    def _list_from_calldata(element_type, calldata: Calldata) -> List:
        num_elements = calldata.pop_int()
        new_list = []
        for index in range(num_elements):
            try:
                element = element_type.from_calldata(calldata)
                new_list.append(element)
            except Exception as e:
                raise ValueError(f"Error while deserializing List[{element_type}] at index {index}: {e}")
        return new_list

    def __post_init__(self):
        for key, field_type in self.__annotations__.items():
            value = getattr(self, key)
            if isinstance(field_type, type) and not isinstance(value, field_type):
                if not is_auto_convertible(field_type):
                    raise ValueError(f'Field "{key}" is not of type "{field_type}"')
                try:
                    converted = field_type(value)
                except Exception as e:
                    raise ValueError(
                        f'Error while auto converting field "{key}" (="{value}) to proper type "{field_type}": {e}')
                setattr(self, key, converted)

    def __str__(self):
        return str(self.__dict__)


class OneOfSchema(Schema):
    @classmethod
    def register_subtype(cls, subtype_class, **kwargs):
        raise NotImplementedError('register_subtype must be implemented in subclasses of OneOfSchema')


class OneOf:
    @classmethod
    def __class_getitem__(cls, dispatcher_class):
        class OneOfMeta(type):
            def __new__(cls, name, bases, dct, **kwargs):
                if len(bases) == 0:
                    bases = (Schema,)
                new_class = super().__new__(cls, name, bases, dct)
                dispatcher_class.register_subtype(new_class, **kwargs)
                return new_class

        return OneOfMeta


class ContractCall(OneOfSchema):
    default: "ContractCall" = None
    subtype_map: Dict[Tuple[int, int], "ContractCall"] = {}

    @classmethod
    def register_subtype(cls, subtype_class, **kwargs):
        if kwargs.get('default', False):
            cls.default = subtype_class
        elif 'contract_address' in kwargs and 'selector' in kwargs:
            cls.subtype_map[(kwargs['contract_address'], kwargs['selector'])] = subtype_class
        else:
            raise ValueError('Subtype class must define "contract_address" and "selector" attributes')

    @classmethod
    def from_calldata(cls, calldata: Calldata, **kwargs) -> "ContractCall":
        contract_address = calldata.pop_int()
        selector = calldata.pop_int()
        arg_count = calldata.pop_int()
        subtype_class = cls.subtype_map.get((contract_address, selector), cls.default)
        return subtype_class.from_calldata(calldata, contract_address=contract_address, selector=selector,
                                           arg_count=arg_count, **kwargs)


class UnknownContractCall(metaclass=OneOf[ContractCall], default=True):
    """ This class represents a contract call where the contract address or selector is unknown.
    It stores the calldata that was consumed during the parsing of the contract call.
    """

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


class SystemCall(OneOfSchema, metaclass=OneOf[ContractCall],
                 contract_address=DISPATCHER_ADDRESS,
                 selector=DISPATCHER_RUN_SYSTEM_SELECTOR):
    subtype_map: Dict[str, "SystemCall"] = {}

    @classmethod
    def register_subtype(cls, subtype_class, **kwargs):
        if 'function_name' in kwargs:
            cls.subtype_map[kwargs['function_name']] = subtype_class
        else:
            raise ValueError('Subtype class must define "function_name" attribute')

    @classmethod
    def from_calldata(cls, calldata: Calldata, **kwargs) -> Schema | Any:
        function_name = calldata.pop_string()
        _arg_count = calldata.pop_int()
        if function_name in cls.subtype_map:
            return cls.subtype_map[function_name].from_calldata(calldata)
        else:
            raise ValueError(f'Unknown function name {function_name}')


@dataclass
class SwayTransferWithConfirmation(metaclass=OneOf[ContractCall],
                                   contract_address=SWAY_TOKEN_ADDRESS,
                                   selector=SWAY_TRANSFER_WITH_CONFIRMATION_SELECTOR):
    recipient: ContractAddress
    amount: u128
    memo: felt252
    consumer: ContractAddress


@dataclass
class MultiInvocationTransaction(Schema):
    invocations: List[ContractCall]

    def __init__(self):
        self.invocations = []

    def append_contract_call(self, contract_call: ContractCall | Any):
        self.invocations.append(contract_call)

from dataclasses import dataclass
from typing import List, get_origin, get_args, Any

from influencepy.starknet.net.constants import DISPATCHER_ADDRESS, DISPATCHER_RUN_SYSTEM_SELECTOR, SWAY_TOKEN_ADDRESS, \
    SWAY_TRANSFER_WITH_CONFIRMATION_SELECTOR
from influencepy.starknet.net.datatypes import Calldata, ContractAddress, u128, felt252, BasicType


class Schema(BasicType):
    @classmethod
    def to_calldata(cls, instance, calldata: Calldata = None) -> Calldata:
        if calldata is None:
            calldata = Calldata([])
        for key, field_type in cls.__annotations__.items():
            value = getattr(instance, key)
            if issubclass(field_type, Schema):
                field_type.to_calldata(value, calldata)
            else:
                raise NotImplementedError
        return calldata

    @classmethod
    def from_calldata(cls, calldata: Calldata) -> "Schema":
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

    def __str__(self):
        return str(self.__dict__)


class Subtype:
    def __init__(self, key: dict, schema: Schema):
        self.key = key
        self.schema = schema

    def is_matching(self, key: dict) -> bool:
        return self.key == key

    def get_schema(self) -> Schema:
        return self.schema


class OneOfSchema(Schema):
    @classmethod
    def from_calldata(cls, calldata: Calldata) -> Schema | Any:
        key = cls.get_subtype_key(calldata)
        for subtype in cls.subtypes:
            if subtype.is_matching(key):
                _arg_count = calldata.pop_int()
                return subtype.get_schema().from_calldata(calldata)
        if hasattr(cls, 'default'):
            return cls.default.from_calldata(calldata, key)
        raise ValueError(f'Unknown subtype {key}')

    @classmethod
    def get_subtype_key(cls, calldata: Calldata) -> dict:
        raise NotImplementedError('get_subtype_key must be implemented in subclasses of OneOfSchema')


class OneOf:
    @classmethod
    def __class_getitem__(cls, dispatcher):
        class OneOfMeta(type):
            def __new__(cls, name, bases, dct, **kwargs):
                new_class = super().__new__(cls, name, bases, dct)
                if 'default' in kwargs and kwargs['default'] is True:
                    dispatcher.default = new_class
                else:
                    if 'subtypes' not in dispatcher.__dict__:
                        dispatcher.subtypes = []
                    dispatcher.subtypes.append(Subtype(kwargs, new_class))
                return new_class

        return OneOfMeta


class ContractCall(OneOfSchema):
    @classmethod
    def get_subtype_key(cls, calldata: Calldata) -> dict:
        to_addr = calldata.pop_int()
        selector = calldata.pop_int()
        return {'contract_address': to_addr, 'selector': selector}


class UnknownContractCall(metaclass=OneOf[ContractCall], default=True):
    """ This class represents a contract call where the contract address or selector is unknown.
    It stores the calldata that was consumed during the parsing of the contract call.
    """

    def __init__(self, calldata: List[int], contract_address: int, selector: int):
        self.calldata = calldata
        self.contract_address = contract_address
        self.selector = selector

    @classmethod
    def from_calldata(cls, calldata: Calldata, key: dict) -> "UnknownContractCall":
        """ Pops the argument length and all arguments from the calldata and stores it.
        No further parsing is done. """
        arg_count = calldata.pop_int()
        data = []
        for _ in range(arg_count):
            data.append(calldata.pop_int())
        return UnknownContractCall(calldata=data, contract_address=key['contract_address'], selector=key['selector'])

    def __repr__(self):
        return f'UnknownContractCall(to={hex(self.contract_address)}, selector={hex(self.selector)}, calldata={self.calldata})'


class SystemCall(OneOfSchema, metaclass=OneOf[ContractCall],
                 contract_address=DISPATCHER_ADDRESS,
                 selector=DISPATCHER_RUN_SYSTEM_SELECTOR):
    @classmethod
    def get_subtype_key(cls, calldata: Calldata) -> dict:
        function_name = calldata.pop_string()
        return {'function_name': function_name}


@dataclass
class SwayTransferWithConfirmation(Schema, metaclass=OneOf[ContractCall],
                                   contract_address=SWAY_TOKEN_ADDRESS,
                                   selector=SWAY_TRANSFER_WITH_CONFIRMATION_SELECTOR):
    recipient: ContractAddress
    amount: u128
    memo: felt252
    consumer: ContractAddress


class MultiInvocationTransaction(Schema):
    invocations: List[ContractCall]

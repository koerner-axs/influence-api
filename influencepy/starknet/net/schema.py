from dataclasses import dataclass
from typing import List, get_origin, get_args

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
                raise NotImplementedError
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
    def from_calldata(cls, calldata: Calldata) -> "Schema":
        key = cls.get_subtype_key(calldata)
        for subtype in cls.subtypes:
            if subtype.is_matching(key):
                return subtype.get_schema().from_calldata(calldata)
        raise ValueError(f"Unknown subtype {key}")

    @classmethod
    def get_subtype_key(cls, calldata: Calldata) -> dict:
        raise NotImplementedError


class OneOf:
    @classmethod
    def __class_getitem__(cls, dispatcher):
        class OneOfMeta(type):
            def __new__(cls, name, bases, dct, **kwargs):
                new_class = super().__new__(cls, name, bases, dct)
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
        _arg_count = calldata.pop_int()
        return {'contract_address': to_addr, 'selector': selector}


class SystemCall(OneOfSchema, metaclass=OneOf[ContractCall],
                 contract_address=DISPATCHER_ADDRESS,
                 selector=DISPATCHER_RUN_SYSTEM_SELECTOR):
    @classmethod
    def get_subtype_key(cls, calldata: Calldata) -> dict:
        function_name = calldata.pop_string()
        _arg_count = calldata.pop_int()
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

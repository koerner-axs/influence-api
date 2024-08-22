from dataclasses import dataclass
from typing import List, get_origin, get_args

from influencepy.starknet.net.datatypes import Calldata, shortstr


class Schema:
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
            if isinstance(field_type, type) and issubclass(field_type, Schema):
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


class SubSchemaRegistry(type):
    def __new__(cls, name, bases, dct, **kwargs):
        new_class = super().__new__(cls, name, bases, dct)
        if name == 'OneOfSchema':
            return new_class
        superclass = bases[0]
        if superclass.__name__ == 'OneOfSchema':
            superclass.subclass_mapping = {}
            return new_class

        if 'identifier' not in kwargs:
            raise KeyError(f"Class {name} must define an identifier in its class definition")
        identifier = kwargs['identifier']
        if identifier in superclass.subclass_mapping:
            other_class = superclass.subclass_mapping[identifier]
            raise ValueError(f"Identifier {identifier} is already in use, defined by {other_class}")
        superclass.subclass_mapping[identifier] = new_class
        return new_class


class OneOfSchema(Schema, metaclass=SubSchemaRegistry):
    subclass_mapping = {}

    @classmethod
    def from_calldata(cls, calldata: Calldata) -> "Schema":
        subclass_identifier = calldata.pop_string()
        if subclass_identifier not in cls.subclass_mapping:
            raise ValueError(f"Unknown subclass identifier \"{subclass_identifier}\"")
        subclass = cls.subclass_mapping[subclass_identifier]
        return subclass.from_calldata(calldata)


class System(OneOfSchema):
    pass


class MultiInvocationTransaction(Schema):
    invocations: List[System]

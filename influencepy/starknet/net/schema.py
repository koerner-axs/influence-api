from typing import get_origin, get_args, List

from influencepy.starknet.net.datatypes import BasicType, is_auto_convertible, Calldata


class Schema(BasicType):
    def to_calldata(self, calldata: Calldata | None = None) -> Calldata:
        if calldata is None:
            calldata = Calldata([])
        for key, field_type in self.__annotations__.items():
            if key.startswith('_'):
                continue
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
        annotations = {}
        for base in cls.__mro__[-2::-1]:  # Skip the last element (object) and reverse
            annotations.update(base.__annotations__)
        for key, field_type in annotations.items():
            if key.startswith('_'):
                continue
            if isinstance(field_type, type) and issubclass(field_type, BasicType):
                try:
                    setattr(instance, key, field_type.from_calldata(calldata))
                except Exception as e:
                    raise ValueError(
                        f'Error while deserializing {cls.__name__}: at field "{key}" of type {field_type.__name__}') from e
            elif get_origin(field_type) == list:
                try:
                    field_type = get_args(field_type)[0]
                    setattr(instance, key, cls._list_from_calldata(field_type, calldata))
                except Exception as e:
                    raise ValueError(
                        f'Error while deserializing {cls.__name__}: at List[{field_type.__name__}] field "{key}"') from e
            else:
                raise NotImplementedError(
                    f'Unsupported field type {field_type.__name__} for field "{key}" in {cls.__name__}')
        if '__post_init__' in cls.__dict__:
            instance.__post_init__()
        return instance

    @staticmethod
    def _list_to_calldata(list_: list, element_type, calldata: Calldata):
        calldata.push_int(len(list_))
        for index in range(len(list_)):
            try:
                list_[index].to_calldata(calldata)
            except Exception as e:
                raise ValueError(f'Error while serializing List[{element_type.__name__}] at index {index}') from e

    @staticmethod
    def _list_from_calldata(element_type, calldata: Calldata) -> List:
        num_elements = calldata.pop_int()
        new_list = []
        for index in range(num_elements):
            try:
                new_list.append(element_type.from_calldata(calldata))
            except Exception as e:
                raise ValueError(f'Error while deserializing List[{element_type.__name__}] at index {index}') from e
        return new_list

    def __post_init__(self):
        for key, field_type in self.__annotations__.items():
            value = getattr(self, key)
            if isinstance(field_type, type) and not isinstance(value, field_type):
                if not is_auto_convertible(field_type):
                    raise ValueError(
                        f'Field "{key}" is not of type {field_type.__name__} and is not auto-convertible')
                try:
                    converted = field_type(value)
                except Exception as e:
                    raise ValueError(
                        f'Error while auto converting field "{key}" (="{value}) to proper type {field_type.__name__}') \
                        from e
                setattr(self, key, converted)

    def __str__(self):
        return str(self.__dict__)

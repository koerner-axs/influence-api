from dataclasses import dataclass, fields
from typing import List

from starknet_py.cairo import felt


class Calldata:
    def __init__(self, calldata: List[int]):
        self.data = calldata

    def __len__(self):
        return len(self.data)

    def pop_int(self) -> int:
        return self.data.pop(0)

    def pop_string(self) -> str:
        return felt.decode_shortstring(self.pop_int())

    def push_int(self, value: int):
        self.data.append(value)

    def push_string(self, value: str):
        self.push_int(felt.encode_shortstring(value))

    def prepend_int(self, value: int):
        self.data.insert(0, value)

    def prepend_string(self, value: str):
        self.prepend_int(felt.encode_shortstring(value))

    def count_push_len_extend(self, other: "Calldata"):
        self.push_int(len(other))
        self.data.extend(other.data)

    def count_prepend_len(self):
        self.prepend_int(len(self))

    def __str__(self):
        return '[\n  ' + ',\n  '.join(f'"0x{x:02x}"' for x in self.data) + '\n]'


class BasicType:
    def to_calldata(self, calldata: Calldata | None) -> Calldata:
        raise NotImplementedError('to_calldata not implemented')

    @staticmethod
    def from_calldata(calldata: Calldata) -> "BasicType":
        raise NotImplementedError('from_calldata not implemented')


def autoconvert(cls):
    cls.__auto_convert__ = True
    return cls


def is_auto_convertible(cls):
    return getattr(cls, '__auto_convert__', False)


def _make_uint_type(bits: int) -> type:
    @autoconvert
    class UnsignedInt(BasicType):
        def __init__(self, value: int):
            if not 0 <= value < 2 ** bits:
                raise ValueError(f"Value {value} is not in the range [0, 2**{bits})")
            self.value = value

        def to_calldata(self, calldata: Calldata) -> Calldata:
            calldata.push_int(self.value)
            return calldata

        @staticmethod
        def from_calldata(calldata: Calldata) -> "UnsignedInt":
            return UnsignedInt(calldata.pop_int())

    return UnsignedInt


@autoconvert
class UnsignedInt256(BasicType):
    def __init__(self, value: int):
        if not 0 <= value < 2 ** 256:
            raise ValueError(f"Value {value} is not in the range [0, 2**256)")
        self.value = value

    def to_calldata(self, calldata: Calldata) -> Calldata:
        calldata.push_int(self.value & (2 ** 128 - 1))
        calldata.push_int(self.value >> 128)
        return calldata

    @staticmethod
    def from_calldata(calldata: Calldata) -> "UnsignedInt256":
        low = calldata.pop_int()
        high = calldata.pop_int()
        return UnsignedInt256(low + (high << 128))


u64 = _make_uint_type(64)
u128 = _make_uint_type(128)
u256 = UnsignedInt256
felt252 = _make_uint_type(252)
shortstr = felt252
ContractAddress = felt252
AccountAddress = felt252


@dataclass
class CubitFixedPoint64(BasicType):
    mag: u64
    sign: bool


@dataclass
class CubitFixedPoint128(BasicType):
    mag: u128
    sign: bool

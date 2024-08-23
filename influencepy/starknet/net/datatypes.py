from dataclasses import dataclass
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


class BasicType:
    def to_calldata(self, calldata: Calldata) -> Calldata:
        raise NotImplementedError

    @staticmethod
    def from_calldata(calldata: Calldata) -> "BasicType":
        raise NotImplementedError


def _make_uint_type(bits: int) -> type:
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

from dataclasses import dataclass
from decimal import Decimal
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
    """Annotation to allow automatic conversion of a field parameter to the correct type from a simple type such as int
    when building dataclasses."""
    cls.__auto_convert__ = True
    return cls


def is_auto_convertible(cls):
    return getattr(cls, '__auto_convert__', False)


def _make_uint_type(bits: int, type_name: str, repr_hex: bool) -> type:
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

        def __repr__(self, as_hex=repr_hex):
            return f'{type_name}{bits}(0x{self.value:02x})' if as_hex else f'{type_name}{bits}({self.value})'

    return UnsignedInt


@autoconvert
class UnsignedInt256(BasicType):
    def __init__(self, value: int):
        if not 0 <= value < 2 ** 256:
            raise ValueError(f'Value {value} is not in the range [0, 2**256)')
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

    def __repr__(self, as_hex=True):
        return f'uint256(0x{self.value:02x})' if as_hex else f'uint256({self.value})'


@autoconvert
class ShortString(BasicType):
    def __init__(self, value: str):
        if len(value) > 31:
            raise ValueError(f'String {value} is too long')
        self.value = value

    def to_calldata(self, calldata: Calldata) -> Calldata:
        calldata.push_string(self.value)
        return calldata

    @staticmethod
    def from_calldata(calldata: Calldata) -> "ShortString":
        return ShortString(calldata.pop_string())

    def encode(self) -> int:
        return felt.encode_shortstring(self.value)

    @staticmethod
    def decode(int_repr: int) -> "ShortString":
        return ShortString(felt.decode_shortstring(int_repr))

    def __repr__(self):
        return f'"{self.value}"'


@autoconvert
class Bool(BasicType):
    def __init__(self, value: bool):
        self.value = value

    def to_calldata(self, calldata: Calldata) -> Calldata:
        calldata.push_int(self.value)
        return calldata

    @staticmethod
    def from_calldata(calldata: Calldata) -> "Bool":
        return Bool(bool(calldata.pop_int()))

    def __repr__(self):
        return f'{self.value}'


u64 = _make_uint_type(64, 'uint', False)
u128 = _make_uint_type(128, 'uint', False)
felt252 = _make_uint_type(252, 'felt', True)
ContractAddress = _make_uint_type(252, 'contract', True)
AccountAddress = _make_uint_type(252, 'account', True)
ClassHash = _make_uint_type(252, 'class', True)
u256 = UnsignedInt256
shortstr = ShortString


@dataclass
class CubitFixedPoint64(BasicType):
    # TODO: Add __repr__
    mag: u64
    sign: bool  # TODO: does sign == False really mean positive?

    def to_calldata(self, calldata: Calldata) -> Calldata:
        self.mag.to_calldata(calldata)
        calldata.push_int(self.sign)
        return calldata

    @staticmethod
    def from_calldata(calldata: Calldata) -> "CubitFixedPoint64":
        mag = u64.from_calldata(calldata)
        sign = bool(calldata.pop_int())
        return CubitFixedPoint64(mag, sign)

    def to_decimal(self):
        unscaled = -Decimal(self.mag.value) if self.sign else Decimal(self.mag.value)
        return Decimal(2) ** -32 * unscaled

    @staticmethod
    def from_decimal(value: Decimal) -> "CubitFixedPoint64":
        sign = value < 0
        scaled = -value if sign else value
        mag = u64(int(round((scaled * 2 ** 32))))
        return CubitFixedPoint64(mag, sign)

    def to_float(self):
        return float(self.to_decimal())

    @staticmethod
    def from_float(value: float) -> "CubitFixedPoint64":
        return CubitFixedPoint64.from_decimal(Decimal(value))

    def __repr__(self):
        return f'fixed64({self.to_float()})'


@dataclass
class CubitFixedPoint128(BasicType):
    # TODO: Add __repr__
    mag: u128
    sign: bool  # TODO: does sign == False really mean positive?

    def to_calldata(self, calldata: Calldata) -> Calldata:
        self.mag.to_calldata(calldata)
        calldata.push_int(self.sign)
        return calldata

    @staticmethod
    def from_calldata(calldata: Calldata) -> "CubitFixedPoint128":
        mag = u128.from_calldata(calldata)
        sign = bool(calldata.pop_int())
        return CubitFixedPoint128(mag, sign)

    def to_decimal(self):
        unscaled = -Decimal(self.mag.value) if self.sign else Decimal(self.mag.value)
        return Decimal(2) ** -64 * unscaled

    @staticmethod
    def from_decimal(value: Decimal) -> "CubitFixedPoint128":
        sign = value < 0
        scaled = -value if sign else value
        mag = u128(int(round((scaled * 2 ** 64))))
        return CubitFixedPoint128(mag, sign)

    def to_float(self):
        return float(self.to_decimal())

    @staticmethod
    def from_float(value: float) -> "CubitFixedPoint128":
        return CubitFixedPoint128.from_decimal(Decimal(value))

    def __repr__(self):
        return f'fixed128({self.to_float()})'

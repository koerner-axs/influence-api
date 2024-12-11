from dataclasses import dataclass

from influencepy.starknet.net.datatypes import felt252, u64, Calldata, ShortString, Bool, AccountAddress
from influencepy.starknet.net.event import UniqueUpdated
from influencepy.starknet.net.structs import PackedEntity, EntityType, PackedLotIdentifier


class UniqueEntityNameEvent(UniqueUpdated):
    entity_type: EntityType
    # unknown: felt252
    name: ShortString
    used: Bool


class UniquePrepareForLaunchRewardClaimedEvent(UniqueUpdated):
    entity: PackedEntity
    claimed: Bool

    def to_calldata(self, calldata: Calldata) -> Calldata:
        self.entity.to_calldata(calldata)
        calldata.push_string("PrepareForLaunchRewardClaimed")
        self.claimed.to_calldata(calldata)
        return calldata

    @classmethod
    def from_calldata(cls, calldata: Calldata, **kwargs) -> "UniquePrepareForLaunchRewardClaimedEvent":
        instance = cls.__new__(cls)
        instance.entity = PackedEntity.from_calldata(calldata)
        calldata.pop_int()  # drop string "PrepareForLaunchRewardClaimed"
        instance.claimed = Bool.from_calldata(calldata)
        return instance


class UniqueArrivalRewardClaimedEvent(UniqueUpdated):
    entity: PackedEntity
    claimed: Bool

    def to_calldata(self, calldata: Calldata) -> Calldata:
        self.entity.to_calldata(calldata)
        calldata.push_string("ArrivalRewardClaimed")
        self.claimed.to_calldata(calldata)
        return calldata

    @classmethod
    def from_calldata(cls, calldata: Calldata, **kwargs) -> "UniqueArrivalRewardClaimedEvent":
        instance = cls.__new__(cls)
        instance.entity = PackedEntity.from_calldata(calldata)
        calldata.pop_int()  # drop string "ArrivalRewardClaimed"
        instance.claimed = Bool.from_calldata(calldata)
        return instance


class UniqueTestnetSwayWhitelistEvent(UniqueUpdated):
    address: AccountAddress
    used: Bool  # used meaning claimable reward was created


class UniqueTestnetSwayClaimedEvent(UniqueUpdated):
    address: AccountAddress
    claimed: Bool


class UniqueBuildingNameEvent(UniqueUpdated):
    # TODO: fix name
    entity_type: EntityType
    unknown: felt252
    name: ShortString
    used: Bool


class UniqueLotUseEvent(UniqueUpdated):
    lot: PackedLotIdentifier
    user: PackedEntity

    @classmethod
    def parse_legacy_0(cls, calldata: Calldata) -> "UniqueLotUseEvent":
        # Handle Unique events with version 2 and subtype LotUse
        lot = calldata.data[0]
        if lot == 0x1872d600000001:
            # There is exactly one early event that has a different format. It was apparently manually written
            # WriteComponent.
            # It is in tx 0x5c5b088f133f5961c952d2e31be2fcbdc89a4c1b04d87d007afa67f9afd6a54
            calldata.pop_int()
            instance = cls.__new__(cls)
            instance.lot = PackedLotIdentifier(lot >> 32, lot & 0xFFFFFFFF, EntityType.LOT)
            instance.user = PackedEntity.from_calldata(calldata)
            return instance
        return UniqueLotUseEvent.from_calldata(calldata)


class UniqueAnnotateEventEvent(UniqueUpdated):
    transaction_hash: felt252
    log_index: u64
    content_hash_1: felt252
    content_hash_2: felt252
    caller_crew: PackedEntity
    used: Bool


def parse_unique_updated_event(calldata: Calldata) -> UniqueUpdated:
    subtype = calldata.pop_int()
    if subtype == 2 and len(calldata) == 3:
        subtype2 = calldata.data[0]
        subtype2_str = ShortString.decode(subtype2).value
        if subtype2_str in ('LotUse', 'UseLot'):
            calldata.pop_int()  # ignore subtype2
            return UniqueLotUseEvent.parse_legacy_0(calldata)
        elif subtype2_str == 'TestnetSwayWhitelist':
            calldata.pop_int()
            return UniqueTestnetSwayWhitelistEvent.from_calldata(calldata)
        elif subtype2_str == 'TestnetSwayClaimed':
            calldata.pop_int()
            return UniqueTestnetSwayClaimedEvent.from_calldata(calldata)
        subtype3 = calldata.data[1]
        if ShortString.in_range(subtype3):
            subtype3_str = ShortString.decode(subtype3).value
            if subtype3_str == 'PrepareForLaunchRewardClaimed':
                return UniquePrepareForLaunchRewardClaimedEvent.from_calldata(calldata)
            elif subtype3_str == 'ArrivalRewardClaimed':
                return UniqueArrivalRewardClaimedEvent.from_calldata(calldata)
        return UniqueEntityNameEvent.from_calldata(calldata)
    elif subtype == 3 and len(calldata) == 4:
        subtype2 = ShortString.decode(calldata.data[0]).value
        if subtype2 == 'Name':
            calldata.pop_int()  # ignore subtype2
            return UniqueEntityNameEvent.from_calldata(calldata)
        elif subtype2 == 'LotUse':
            calldata.pop_int()  # ignore subtype2
            return UniqueLotUseEvent.from_calldata(calldata)
    elif subtype == 4 and len(calldata) == 5:
        subtype2 = ShortString.decode(calldata.data[0]).value
        if subtype2 == 'Name':
            calldata.pop_int()  # ignore subtype2
            return UniqueBuildingNameEvent.from_calldata(calldata)
    elif subtype == 5 and len(calldata) == 6:
        return UniqueAnnotateEventEvent.from_calldata(calldata)
    raise ValueError(f'Unknown uniqueness group subtype {subtype}')

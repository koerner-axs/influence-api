from dataclasses import dataclass  # noqa: F401
from typing import Dict, List  # noqa: F401

from starknet_py.hash.utils import _starknet_keccak

from influencepy.starknet.net.datatypes import *
from influencepy.starknet.net.schema import Schema
from influencepy.starknet.net.structs import Entity, InventoryItem  # noqa: F401


class SystemEvent(Schema):
    _key: int


@dataclass
class AddedAccountToWhitelist(SystemEvent):
    target: Entity
    permission: u64
    permitted: ContractAddress
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'AddedAccountToWhitelist')


@dataclass
class AddedToWhitelist(SystemEvent):
    entity: Entity
    permission: u64
    target: Entity
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'AddedToWhitelist')


@dataclass
class AddedToWhitelistV1(SystemEvent):
    target: Entity
    permission: u64
    permitted: Entity
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'AddedToWhitelistV1')


@dataclass
class ArrivalRewardClaimed(SystemEvent):
    asteroid: Entity
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'ArrivalRewardClaimed')


@dataclass
class AsteroidInitialized(SystemEvent):
    asteroid: Entity
    _key: int = _starknet_keccak(b'AsteroidInitialized')


@dataclass
class AsteroidManaged(SystemEvent):
    asteroid: Entity
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'AsteroidManaged')


@dataclass
class AsteroidPurchased(SystemEvent):
    asteroid: Entity
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'AsteroidPurchased')


@dataclass
class BuildingRepossessed(SystemEvent):
    building: Entity
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'BuildingRepossessed')


@dataclass
class BuyOrderCancelled(SystemEvent):
    buyer_crew: Entity
    exchange: Entity
    product: u64
    amount: u64
    price: u64
    storage: Entity
    storage_slot: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'BuyOrderCancelled')


@dataclass
class BuyOrderCreated(SystemEvent):
    exchange: Entity
    product: u64
    amount: u64
    price: u64
    storage: Entity
    storage_slot: u64
    valid_time: u64
    maker_fee: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'BuyOrderCreated')


@dataclass
class BuyOrderFilled(SystemEvent):
    buyer_crew: Entity
    exchange: Entity
    product: u64
    amount: u64
    price: u64
    storage: Entity
    storage_slot: u64
    origin: Entity
    origin_slot: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'BuyOrderFilled')


@dataclass
class ConstructionAbandoned(SystemEvent):
    building: Entity
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'ConstructionAbandoned')


@dataclass
class ConstructionDeconstructed(SystemEvent):
    building: Entity
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'ConstructionDeconstructed')


@dataclass
class ConstructionFinished(SystemEvent):
    building: Entity
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'ConstructionFinished')


@dataclass
class ConstructionPlanned(SystemEvent):
    building: Entity
    building_type: u64
    asteroid: Entity
    lot: Entity
    grace_period_end: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'ConstructionPlanned')


@dataclass
class ConstructionStarted(SystemEvent):
    building: Entity
    finish_time: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'ConstructionStarted')


@dataclass
class ContractAgreementAccepted(SystemEvent):
    target: Entity
    permission: u64
    permitted: Entity
    contract: ContractAddress
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'ContractAgreementAccepted')


@dataclass
class ContractPolicyAssigned(SystemEvent):
    entity: Entity
    permission: u64
    contract: ContractAddress
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'ContractPolicyAssigned')


@dataclass
class ContractPolicyRemoved(SystemEvent):
    entity: Entity
    permission: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'ContractPolicyRemoved')


@dataclass
class CrewDelegated(SystemEvent):
    delegated_to: ContractAddress
    crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'CrewDelegated')


@dataclass
class CrewEjected(SystemEvent):
    station: Entity
    ejected_crew: Entity
    finish_time: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'CrewEjected')


@dataclass
class CrewStationed(SystemEvent):
    station: Entity
    finish_time: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'CrewStationed')


@dataclass
class CrewStationedV1(SystemEvent):
    origin_station: Entity
    destination_station: Entity
    finish_time: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'CrewStationedV1')


@dataclass
class CrewmatePurchased(SystemEvent):
    crewmate: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'CrewmatePurchased')


@dataclass
class CrewmateRecruited(SystemEvent):
    crewmate: Entity
    collection: u64
    class_: u64
    title: u64
    impactful: List[u64]
    cosmetic: List[u64]
    gender: u64
    body: u64
    face: u64
    hair: u64
    hair_color: u64
    clothes: u64
    head: u64
    item: u64
    station: Entity
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'CrewmateRecruited')


@dataclass
class CrewmateRecruitedV1(SystemEvent):
    crewmate: Entity
    collection: u64
    class_: u64
    title: u64
    impactful: List[u64]
    cosmetic: List[u64]
    gender: u64
    body: u64
    face: u64
    hair: u64
    hair_color: u64
    clothes: u64
    head: u64
    item: u64
    name: felt252
    station: Entity
    composition: List[u64]
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'CrewmateRecruitedV1')


@dataclass
class CrewmatesArranged(SystemEvent):
    composition: List[u64]
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'CrewmatesArranged')


@dataclass
class CrewmatesArrangedV1(SystemEvent):
    composition_old: List[u64]
    composition_new: List[u64]
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'CrewmatesArrangedV1')


@dataclass
class CrewmatesExchanged(SystemEvent):
    crew1: Entity
    crew1_composition_old: List[u64]
    crew1_composition_new: List[u64]
    crew2: Entity
    crew2_composition_old: List[u64]
    crew2_composition_new: List[u64]
    caller: ContractAddress
    _key: int = _starknet_keccak(b'CrewmatesExchanged')


@dataclass
class Debug_DepositBounds(SystemEvent):
    lot_abundance: CubitFixedPoint64
    initial_yield: u64
    lower_bound: CubitFixedPoint64
    upper_bound: CubitFixedPoint64
    _key: int = _starknet_keccak(b'Debug_DepositBounds')


@dataclass
class DeliveryCancelled(SystemEvent):
    origin: Entity
    origin_slot: u64
    products: List[InventoryItem]
    dest: Entity
    dest_slot: u64
    delivery: Entity
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'DeliveryCancelled')


@dataclass
class DeliveryDumped(SystemEvent):
    origin: Entity
    origin_slot: u64
    products: List[InventoryItem]
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'DeliveryDumped')


@dataclass
class DeliveryPackaged(SystemEvent):
    origin: Entity
    origin_slot: u64
    products: List[InventoryItem]
    dest: Entity
    dest_slot: u64
    delivery: Entity
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'DeliveryPackaged')


@dataclass
class DeliveryPackagedV1(SystemEvent):
    origin: Entity
    origin_slot: u64
    products: List[InventoryItem]
    dest: Entity
    dest_slot: u64
    price: u64
    delivery: Entity
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'DeliveryPackagedV1')


@dataclass
class DeliveryReceived(SystemEvent):
    origin: Entity
    origin_slot: u64
    products: List[InventoryItem]
    dest: Entity
    dest_slot: u64
    delivery: Entity
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'DeliveryReceived')


@dataclass
class DeliverySent(SystemEvent):
    origin: Entity
    origin_slot: u64
    products: List[InventoryItem]
    dest: Entity
    dest_slot: u64
    delivery: Entity
    finish_time: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'DeliverySent')


@dataclass
class DepositListedForSale(SystemEvent):
    deposit: Entity
    price: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'DepositListedForSale')


@dataclass
class DepositPurchased(SystemEvent):
    deposit: Entity
    price: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'DepositPurchased')


@dataclass
class DepositPurchasedV1(SystemEvent):
    deposit: Entity
    price: u64
    seller_crew: Entity
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'DepositPurchasedV1')


@dataclass
class DepositUnlistedForSale(SystemEvent):
    deposit: Entity
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'DepositUnlistedForSale')


@dataclass
class DirectMessageSent(SystemEvent):
    recipient: ContractAddress
    content_hash: List[felt252]
    caller: ContractAddress
    _key: int = _starknet_keccak(b'DirectMessageSent')


@dataclass
class EmergencyActivated(SystemEvent):
    ship: Entity
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'EmergencyActivated')


@dataclass
class EmergencyDeactivated(SystemEvent):
    ship: Entity
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'EmergencyDeactivated')


@dataclass
class EmergencyPropellantCollected(SystemEvent):
    ship: Entity
    amount: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'EmergencyPropellantCollected')


@dataclass
class EventAnnotated(SystemEvent):
    transaction_hash: felt252
    log_index: u64
    content_hash: List[felt252]
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'EventAnnotated')


@dataclass
class ExchangeConfigured(SystemEvent):
    exchange: Entity
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'ExchangeConfigured')


@dataclass
class FoodSupplied(SystemEvent):
    food: u64
    last_fed: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'FoodSupplied')


@dataclass
class FoodSuppliedV1(SystemEvent):
    food: u64
    last_fed: u64
    origin: Entity
    origin_slot: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'FoodSuppliedV1')


@dataclass
class MaterialProcessingFinished(SystemEvent):
    processor: Entity
    processor_slot: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'MaterialProcessingFinished')


@dataclass
class MaterialProcessingStartedV1(SystemEvent):
    processor: Entity
    processor_slot: u64
    process: u64
    inputs: List[InventoryItem]
    origin: Entity
    origin_slot: u64
    outputs: List[InventoryItem]
    destination: Entity
    destination_slot: u64
    finish_time: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'MaterialProcessingStartedV1')


@dataclass
class NameChanged(SystemEvent):
    entity: Entity
    name: ShortString
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'NameChanged')


@dataclass
class PrepaidAgreementAccepted(SystemEvent):
    target: Entity
    permission: u64
    permitted: Entity
    term: u64
    rate: u64
    initial_term: u64
    notice_period: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'PrepaidAgreementAccepted')


@dataclass
class PrepaidAgreementCancelled(SystemEvent):
    target: Entity
    permission: u64
    permitted: Entity
    eviction_time: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'PrepaidAgreementCancelled')


@dataclass
class PrepaidAgreementExtended(SystemEvent):
    target: Entity
    permission: u64
    permitted: Entity
    term: u64
    rate: u64
    initial_term: u64
    notice_period: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'PrepaidAgreementExtended')


@dataclass
class PrepaidAgreementTransferred(SystemEvent):
    target: Entity
    permission: u64
    permitted: Entity
    old_permitted: Entity
    term: u64
    rate: u64
    initial_term: u64
    notice_period: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'PrepaidAgreementTransferred')


@dataclass
class PrepaidMerkleAgreementAccepted(SystemEvent):
    target: Entity
    permission: u64
    permitted: Entity
    term: u64
    rate: u64
    initial_term: u64
    notice_period: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'PrepaidMerkleAgreementAccepted')


@dataclass
class PrepaidMerklePolicyAssigned(SystemEvent):
    entity: Entity
    permission: u64
    rate: u64
    initial_term: u64
    notice_period: u64
    merkle_root: felt252
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'PrepaidMerklePolicyAssigned')


@dataclass
class PrepaidMerklePolicyRemoved(SystemEvent):
    entity: Entity
    permission: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'PrepaidMerklePolicyRemoved')


@dataclass
class PrepaidPolicyAssigned(SystemEvent):
    entity: Entity
    permission: u64
    rate: u64
    initial_term: u64
    notice_period: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'PrepaidPolicyAssigned')


@dataclass
class PrepaidPolicyRemoved(SystemEvent):
    entity: Entity
    permission: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'PrepaidPolicyRemoved')


@dataclass
class PrepareForLaunchRewardClaimed(SystemEvent):
    asteroid: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'PrepareForLaunchRewardClaimed')


@dataclass
class PublicPolicyAssigned(SystemEvent):
    entity: Entity
    permission: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'PublicPolicyAssigned')


@dataclass
class PublicPolicyRemoved(SystemEvent):
    entity: Entity
    permission: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'PublicPolicyRemoved')


@dataclass
class RandomEventResolved(SystemEvent):
    random_event: u64
    choice: u64
    action_type: u64
    action_target: Entity
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'RandomEventResolved')


@dataclass
class RekeyedInbox(SystemEvent):
    messaging_key_x: u256
    messaging_key_y: u256
    caller: ContractAddress
    _key: int = _starknet_keccak(b'RekeyedInbox')


@dataclass
class RemovedAccountFromWhitelist(SystemEvent):
    target: Entity
    permission: u64
    permitted: ContractAddress
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'RemovedAccountFromWhitelist')


@dataclass
class RemovedFromWhitelist(SystemEvent):
    entity: Entity
    permission: u64
    target: Entity
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'RemovedFromWhitelist')


@dataclass
class RemovedFromWhitelistV1(SystemEvent):
    target: Entity
    permission: u64
    permitted: Entity
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'RemovedFromWhitelistV1')


@dataclass
class ResourceExtractionFinished(SystemEvent):
    extractor: Entity
    extractor_slot: u64
    resource: u64
    yield_: u64
    destination: Entity
    destination_slot: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'ResourceExtractionFinished')


@dataclass
class ResourceExtractionStarted(SystemEvent):
    deposit: Entity
    resource: u64
    yield_: u64
    extractor: Entity
    extractor_slot: u64
    destination: Entity
    destination_slot: u64
    finish_time: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'ResourceExtractionStarted')


@dataclass
class ResourceScanFinished(SystemEvent):
    asteroid: Entity
    abundances: List[u128]
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'ResourceScanFinished')


@dataclass
class ResourceScanStarted(SystemEvent):
    asteroid: Entity
    finish_time: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'ResourceScanStarted')


@dataclass
class SamplingDepositFinished(SystemEvent):
    deposit: Entity
    initial_yield: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'SamplingDepositFinished')


@dataclass
class SamplingDepositStarted(SystemEvent):
    deposit: Entity
    lot: Entity
    resource: u64
    finish_time: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'SamplingDepositStarted')


@dataclass
class SamplingDepositStartedV1(SystemEvent):
    deposit: Entity
    lot: Entity
    resource: u64
    improving: Bool
    origin: Entity
    origin_slot: u64
    finish_time: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'SamplingDepositStartedV1')


@dataclass
class SellOrderCancelled(SystemEvent):
    seller_crew: Entity
    exchange: Entity
    product: u64
    price: u64
    storage: Entity
    storage_slot: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'SellOrderCancelled')


@dataclass
class SellOrderCreated(SystemEvent):
    exchange: Entity
    product: u64
    amount: u64
    price: u64
    storage: Entity
    storage_slot: u64
    valid_time: u64
    maker_fee: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'SellOrderCreated')


@dataclass
class SellOrderFilled(SystemEvent):
    seller_crew: Entity
    exchange: Entity
    product: u64
    amount: u64
    price: u64
    storage: Entity
    storage_slot: u64
    destination: Entity
    destination_slot: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'SellOrderFilled')


@dataclass
class ShipAssemblyFinished(SystemEvent):
    ship: Entity
    dry_dock: Entity
    dry_dock_slot: u64
    destination: Entity
    finish_time: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'ShipAssemblyFinished')


@dataclass
class ShipAssemblyStarted(SystemEvent):
    ship: Entity
    dry_dock: Entity
    dry_dock_slot: u64
    ship_type: u64
    finish_time: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'ShipAssemblyStarted')


@dataclass
class ShipAssemblyStartedV1(SystemEvent):
    ship: Entity
    ship_type: u64
    dry_dock: Entity
    dry_dock_slot: u64
    origin: Entity
    origin_slot: u64
    finish_time: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'ShipAssemblyStartedV1')


@dataclass
class ShipCommandeered(SystemEvent):
    ship: Entity
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'ShipCommandeered')


@dataclass
class ShipDocked(SystemEvent):
    ship: Entity
    dock: Entity
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'ShipDocked')


@dataclass
class ShipUndocked(SystemEvent):
    ship: Entity
    dock: Entity
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'ShipUndocked')


@dataclass
class SurfaceScanFinished(SystemEvent):
    asteroid: Entity
    bonuses: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'SurfaceScanFinished')


@dataclass
class SurfaceScanStarted(SystemEvent):
    asteroid: Entity
    finish_time: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'SurfaceScanStarted')


@dataclass
class TestnetSwayClaimed(SystemEvent):
    amount: u256
    caller: ContractAddress
    _key: int = _starknet_keccak(b'TestnetSwayClaimed')


@dataclass
class TransitFinished(SystemEvent):
    ship: Entity
    origin: Entity
    destination: Entity
    departure: u64
    arrival: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'TransitFinished')


@dataclass
class TransitStarted(SystemEvent):
    ship: Entity
    origin: Entity
    destination: Entity
    departure: u64
    arrival: u64
    finish_time: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak(b'TransitStarted')


class UnknownSystemEvent(SystemEvent):
    def __init__(self, keys: List[int], data: Calldata):
        self.keys = keys
        self.data = data


# Begin unofficial events. The ABIs for these events are not available in the Influence SDK and are inferred manually or
# with the help of StarkNet block explorers.
class ContractRegisteredEvent(SystemEvent):
    # TODO: This is an event the Dispatcher emits when register_contract is successful. It does not represent an event
    #  emitted by a system, so it might need to inherit from a different class and be renamed accordingly.
    name: ShortString
    address: ContractAddress
    _key: int = _starknet_keccak(b'ContractRegistered')


class SystemRegisteredEvent(SystemEvent):
    # TODO: This is an event the Dispatcher emits when register_system is successful. It does not represent an event
    #  emitted by a system, so it might need to inherit from a different class and be renamed accordingly.
    name: ShortString
    class_hash: ClassHash
    _key: int = _starknet_keccak(b'SystemRegistered')


class UnknownEvent:
    def __init__(self, keys: List[int], data: Calldata):
        self.keys = keys
        self.data = data


ALL_SYSTEM_EVENTS: Dict[int, SystemEvent] = {
    AddedAccountToWhitelist._key: AddedAccountToWhitelist,
    AddedToWhitelist._key: AddedToWhitelist,
    AddedToWhitelistV1._key: AddedToWhitelistV1,
    ArrivalRewardClaimed._key: ArrivalRewardClaimed,
    AsteroidInitialized._key: AsteroidInitialized,
    AsteroidManaged._key: AsteroidManaged,
    AsteroidPurchased._key: AsteroidPurchased,
    BuildingRepossessed._key: BuildingRepossessed,
    BuyOrderCancelled._key: BuyOrderCancelled,
    BuyOrderCreated._key: BuyOrderCreated,
    BuyOrderFilled._key: BuyOrderFilled,
    ConstructionAbandoned._key: ConstructionAbandoned,
    ConstructionDeconstructed._key: ConstructionDeconstructed,
    ConstructionFinished._key: ConstructionFinished,
    ConstructionPlanned._key: ConstructionPlanned,
    ConstructionStarted._key: ConstructionStarted,
    ContractAgreementAccepted._key: ContractAgreementAccepted,
    ContractPolicyAssigned._key: ContractPolicyAssigned,
    ContractPolicyRemoved._key: ContractPolicyRemoved,
    CrewDelegated._key: CrewDelegated,
    CrewEjected._key: CrewEjected,
    CrewStationed._key: CrewStationed,
    CrewStationedV1._key: CrewStationedV1,
    CrewmatePurchased._key: CrewmatePurchased,
    CrewmateRecruited._key: CrewmateRecruited,
    CrewmateRecruitedV1._key: CrewmateRecruitedV1,
    CrewmatesArranged._key: CrewmatesArranged,
    CrewmatesArrangedV1._key: CrewmatesArrangedV1,
    CrewmatesExchanged._key: CrewmatesExchanged,
    Debug_DepositBounds._key: Debug_DepositBounds,
    DeliveryCancelled._key: DeliveryCancelled,
    DeliveryDumped._key: DeliveryDumped,
    DeliveryPackaged._key: DeliveryPackaged,
    DeliveryPackagedV1._key: DeliveryPackagedV1,
    DeliveryReceived._key: DeliveryReceived,
    DeliverySent._key: DeliverySent,
    DepositListedForSale._key: DepositListedForSale,
    DepositPurchased._key: DepositPurchased,
    DepositPurchasedV1._key: DepositPurchasedV1,
    DepositUnlistedForSale._key: DepositUnlistedForSale,
    DirectMessageSent._key: DirectMessageSent,
    EmergencyActivated._key: EmergencyActivated,
    EmergencyDeactivated._key: EmergencyDeactivated,
    EmergencyPropellantCollected._key: EmergencyPropellantCollected,
    EventAnnotated._key: EventAnnotated,
    ExchangeConfigured._key: ExchangeConfigured,
    FoodSupplied._key: FoodSupplied,
    FoodSuppliedV1._key: FoodSuppliedV1,
    MaterialProcessingFinished._key: MaterialProcessingFinished,
    MaterialProcessingStartedV1._key: MaterialProcessingStartedV1,
    NameChanged._key: NameChanged,
    PrepaidAgreementAccepted._key: PrepaidAgreementAccepted,
    PrepaidAgreementCancelled._key: PrepaidAgreementCancelled,
    PrepaidAgreementExtended._key: PrepaidAgreementExtended,
    PrepaidAgreementTransferred._key: PrepaidAgreementTransferred,
    PrepaidMerkleAgreementAccepted._key: PrepaidMerkleAgreementAccepted,
    PrepaidMerklePolicyAssigned._key: PrepaidMerklePolicyAssigned,
    PrepaidMerklePolicyRemoved._key: PrepaidMerklePolicyRemoved,
    PrepaidPolicyAssigned._key: PrepaidPolicyAssigned,
    PrepaidPolicyRemoved._key: PrepaidPolicyRemoved,
    PrepareForLaunchRewardClaimed._key: PrepareForLaunchRewardClaimed,
    PublicPolicyAssigned._key: PublicPolicyAssigned,
    PublicPolicyRemoved._key: PublicPolicyRemoved,
    RandomEventResolved._key: RandomEventResolved,
    RekeyedInbox._key: RekeyedInbox,
    RemovedAccountFromWhitelist._key: RemovedAccountFromWhitelist,
    RemovedFromWhitelist._key: RemovedFromWhitelist,
    RemovedFromWhitelistV1._key: RemovedFromWhitelistV1,
    ResourceExtractionFinished._key: ResourceExtractionFinished,
    ResourceExtractionStarted._key: ResourceExtractionStarted,
    ResourceScanFinished._key: ResourceScanFinished,
    ResourceScanStarted._key: ResourceScanStarted,
    SamplingDepositFinished._key: SamplingDepositFinished,
    SamplingDepositStarted._key: SamplingDepositStarted,
    SamplingDepositStartedV1._key: SamplingDepositStartedV1,
    SellOrderCancelled._key: SellOrderCancelled,
    SellOrderCreated._key: SellOrderCreated,
    SellOrderFilled._key: SellOrderFilled,
    ShipAssemblyFinished._key: ShipAssemblyFinished,
    ShipAssemblyStarted._key: ShipAssemblyStarted,
    ShipAssemblyStartedV1._key: ShipAssemblyStartedV1,
    ShipCommandeered._key: ShipCommandeered,
    ShipDocked._key: ShipDocked,
    ShipUndocked._key: ShipUndocked,
    SurfaceScanFinished._key: SurfaceScanFinished,
    SurfaceScanStarted._key: SurfaceScanStarted,
    TestnetSwayClaimed._key: TestnetSwayClaimed,
    TransitFinished._key: TransitFinished,
    TransitStarted._key: TransitStarted,
    # Begin unofficial events
    ContractRegisteredEvent._key: ContractRegisteredEvent,
    SystemRegisteredEvent._key: SystemRegisteredEvent,
}

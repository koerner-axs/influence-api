from typing import List
from dataclasses import dataclass

from starknet_py.hash.utils import _starknet_keccak

from influencepy.starknet.net.datatypes import u64, u128, u256, felt252, shortstr, CubitFixedPoint64, ContractAddress
from influencepy.starknet.net.schema import Schema
from influencepy.starknet.net.structs import Entity, InventoryItem


class SystemEvent(Schema):
    _key: int


@dataclass
class AddedAccountToWhitelist(SystemEvent):
    target: Entity
    permission: u64
    permitted: ContractAddress
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('AddedAccountToWhitelist')


@dataclass
class AddedToWhitelist(SystemEvent):
    entity: Entity
    permission: u64
    target: Entity
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('AddedToWhitelist')


@dataclass
class AddedToWhitelistV1(SystemEvent):
    target: Entity
    permission: u64
    permitted: Entity
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('AddedToWhitelistV1')


@dataclass
class ArrivalRewardClaimed(SystemEvent):
    asteroid: Entity
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('ArrivalRewardClaimed')


@dataclass
class AsteroidInitialized(SystemEvent):
    asteroid: Entity
    _key: int = _starknet_keccak('AsteroidInitialized')


@dataclass
class AsteroidManaged(SystemEvent):
    asteroid: Entity
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('AsteroidManaged')


@dataclass
class AsteroidPurchased(SystemEvent):
    asteroid: Entity
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('AsteroidPurchased')


@dataclass
class BuildingRepossessed(SystemEvent):
    building: Entity
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('BuildingRepossessed')


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
    _key: int = _starknet_keccak('BuyOrderCancelled')


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
    _key: int = _starknet_keccak('BuyOrderCreated')


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
    _key: int = _starknet_keccak('BuyOrderFilled')


@dataclass
class ConstructionAbandoned(SystemEvent):
    building: Entity
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('ConstructionAbandoned')


@dataclass
class ConstructionDeconstructed(SystemEvent):
    building: Entity
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('ConstructionDeconstructed')


@dataclass
class ConstructionFinished(SystemEvent):
    building: Entity
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('ConstructionFinished')


@dataclass
class ConstructionPlanned(SystemEvent):
    building: Entity
    building_type: u64
    asteroid: Entity
    lot: Entity
    grace_period_end: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('ConstructionPlanned')


@dataclass
class ConstructionStarted(SystemEvent):
    building: Entity
    finish_time: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('ConstructionStarted')


@dataclass
class ContractAgreementAccepted(SystemEvent):
    target: Entity
    permission: u64
    permitted: Entity
    contract: ContractAddress
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('ContractAgreementAccepted')


@dataclass
class ContractPolicyAssigned(SystemEvent):
    entity: Entity
    permission: u64
    contract: ContractAddress
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('ContractPolicyAssigned')


@dataclass
class ContractPolicyRemoved(SystemEvent):
    entity: Entity
    permission: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('ContractPolicyRemoved')


@dataclass
class CrewDelegated(SystemEvent):
    delegated_to: ContractAddress
    crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('CrewDelegated')


@dataclass
class CrewEjected(SystemEvent):
    station: Entity
    ejected_crew: Entity
    finish_time: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('CrewEjected')


@dataclass
class CrewStationed(SystemEvent):
    station: Entity
    finish_time: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('CrewStationed')


@dataclass
class CrewStationedV1(SystemEvent):
    origin_station: Entity
    destination_station: Entity
    finish_time: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('CrewStationedV1')


@dataclass
class CrewmatePurchased(SystemEvent):
    crewmate: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('CrewmatePurchased')


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
    _key: int = _starknet_keccak('CrewmateRecruited')


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
    _key: int = _starknet_keccak('CrewmateRecruitedV1')


@dataclass
class CrewmatesArranged(SystemEvent):
    composition: List[u64]
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('CrewmatesArranged')


@dataclass
class CrewmatesArrangedV1(SystemEvent):
    composition_old: List[u64]
    composition_new: List[u64]
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('CrewmatesArrangedV1')


@dataclass
class CrewmatesExchanged(SystemEvent):
    crew1: Entity
    crew1_composition_old: List[u64]
    crew1_composition_new: List[u64]
    crew2: Entity
    crew2_composition_old: List[u64]
    crew2_composition_new: List[u64]
    caller: ContractAddress
    _key: int = _starknet_keccak('CrewmatesExchanged')


@dataclass
class Debug_DepositBounds(SystemEvent):
    lot_abundance: CubitFixedPoint64
    initial_yield: u64
    lower_bound: CubitFixedPoint64
    upper_bound: CubitFixedPoint64
    _key: int = _starknet_keccak('Debug_DepositBounds')


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
    _key: int = _starknet_keccak('DeliveryCancelled')


@dataclass
class DeliveryDumped(SystemEvent):
    origin: Entity
    origin_slot: u64
    products: List[InventoryItem]
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('DeliveryDumped')


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
    _key: int = _starknet_keccak('DeliveryPackaged')


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
    _key: int = _starknet_keccak('DeliveryPackagedV1')


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
    _key: int = _starknet_keccak('DeliveryReceived')


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
    _key: int = _starknet_keccak('DeliverySent')


@dataclass
class DepositListedForSale(SystemEvent):
    deposit: Entity
    price: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('DepositListedForSale')


@dataclass
class DepositPurchased(SystemEvent):
    deposit: Entity
    price: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('DepositPurchased')


@dataclass
class DepositPurchasedV1(SystemEvent):
    deposit: Entity
    price: u64
    seller_crew: Entity
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('DepositPurchasedV1')


@dataclass
class DepositUnlistedForSale(SystemEvent):
    deposit: Entity
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('DepositUnlistedForSale')


@dataclass
class EmergencyActivated(SystemEvent):
    ship: Entity
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('EmergencyActivated')


@dataclass
class EmergencyDeactivated(SystemEvent):
    ship: Entity
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('EmergencyDeactivated')


@dataclass
class EmergencyPropellantCollected(SystemEvent):
    ship: Entity
    amount: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('EmergencyPropellantCollected')


@dataclass
class EventAnnotated(SystemEvent):
    transaction_hash: felt252
    log_index: u64
    content_hash: List[felt252]
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('EventAnnotated')


@dataclass
class ExchangeConfigured(SystemEvent):
    exchange: Entity
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('ExchangeConfigured')


@dataclass
class FoodSupplied(SystemEvent):
    food: u64
    last_fed: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('FoodSupplied')


@dataclass
class FoodSuppliedV1(SystemEvent):
    food: u64
    last_fed: u64
    origin: Entity
    origin_slot: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('FoodSuppliedV1')


@dataclass
class MaterialProcessingFinished(SystemEvent):
    processor: Entity
    processor_slot: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('MaterialProcessingFinished')


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
    _key: int = _starknet_keccak('MaterialProcessingStartedV1')


@dataclass
class NameChanged(SystemEvent):
    entity: Entity
    name: shortstr
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('NameChanged')


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
    _key: int = _starknet_keccak('PrepaidAgreementAccepted')


@dataclass
class PrepaidAgreementCancelled(SystemEvent):
    target: Entity
    permission: u64
    permitted: Entity
    eviction_time: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('PrepaidAgreementCancelled')


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
    _key: int = _starknet_keccak('PrepaidAgreementExtended')


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
    _key: int = _starknet_keccak('PrepaidMerkleAgreementAccepted')


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
    _key: int = _starknet_keccak('PrepaidMerklePolicyAssigned')


@dataclass
class PrepaidMerklePolicyRemoved(SystemEvent):
    entity: Entity
    permission: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('PrepaidMerklePolicyRemoved')


@dataclass
class PrepaidPolicyAssigned(SystemEvent):
    entity: Entity
    permission: u64
    rate: u64
    initial_term: u64
    notice_period: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('PrepaidPolicyAssigned')


@dataclass
class PrepaidPolicyRemoved(SystemEvent):
    entity: Entity
    permission: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('PrepaidPolicyRemoved')


@dataclass
class PrepareForLaunchRewardClaimed(SystemEvent):
    asteroid: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('PrepareForLaunchRewardClaimed')


@dataclass
class PublicPolicyAssigned(SystemEvent):
    entity: Entity
    permission: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('PublicPolicyAssigned')


@dataclass
class PublicPolicyRemoved(SystemEvent):
    entity: Entity
    permission: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('PublicPolicyRemoved')


@dataclass
class RandomEventResolved(SystemEvent):
    random_event: u64
    choice: u64
    action_type: u64
    action_target: Entity
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('RandomEventResolved')


@dataclass
class RemovedAccountFromWhitelist(SystemEvent):
    target: Entity
    permission: u64
    permitted: ContractAddress
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('RemovedAccountFromWhitelist')


@dataclass
class RemovedFromWhitelist(SystemEvent):
    entity: Entity
    permission: u64
    target: Entity
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('RemovedFromWhitelist')


@dataclass
class RemovedFromWhitelistV1(SystemEvent):
    target: Entity
    permission: u64
    permitted: Entity
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('RemovedFromWhitelistV1')


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
    _key: int = _starknet_keccak('ResourceExtractionFinished')


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
    _key: int = _starknet_keccak('ResourceExtractionStarted')


@dataclass
class ResourceScanFinished(SystemEvent):
    asteroid: Entity
    abundances: List[u128]
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('ResourceScanFinished')


@dataclass
class ResourceScanStarted(SystemEvent):
    asteroid: Entity
    finish_time: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('ResourceScanStarted')


@dataclass
class SamplingDepositFinished(SystemEvent):
    deposit: Entity
    initial_yield: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('SamplingDepositFinished')


@dataclass
class SamplingDepositStarted(SystemEvent):
    deposit: Entity
    lot: Entity
    resource: u64
    finish_time: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('SamplingDepositStarted')


@dataclass
class SamplingDepositStartedV1(SystemEvent):
    deposit: Entity
    lot: Entity
    resource: u64
    improving: bool
    origin: Entity
    origin_slot: u64
    finish_time: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('SamplingDepositStartedV1')


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
    _key: int = _starknet_keccak('SellOrderCancelled')


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
    _key: int = _starknet_keccak('SellOrderCreated')


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
    _key: int = _starknet_keccak('SellOrderFilled')


@dataclass
class ShipAssemblyFinished(SystemEvent):
    ship: Entity
    dry_dock: Entity
    dry_dock_slot: u64
    destination: Entity
    finish_time: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('ShipAssemblyFinished')


@dataclass
class ShipAssemblyStarted(SystemEvent):
    ship: Entity
    dry_dock: Entity
    dry_dock_slot: u64
    ship_type: u64
    finish_time: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('ShipAssemblyStarted')


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
    _key: int = _starknet_keccak('ShipAssemblyStartedV1')


@dataclass
class ShipCommandeered(SystemEvent):
    ship: Entity
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('ShipCommandeered')


@dataclass
class ShipDocked(SystemEvent):
    ship: Entity
    dock: Entity
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('ShipDocked')


@dataclass
class ShipUndocked(SystemEvent):
    ship: Entity
    dock: Entity
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('ShipUndocked')


@dataclass
class SurfaceScanFinished(SystemEvent):
    asteroid: Entity
    bonuses: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('SurfaceScanFinished')


@dataclass
class SurfaceScanStarted(SystemEvent):
    asteroid: Entity
    finish_time: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('SurfaceScanStarted')


@dataclass
class TestnetSwayClaimed(SystemEvent):
    amount: u256
    caller: ContractAddress
    _key: int = _starknet_keccak('TestnetSwayClaimed')


@dataclass
class TransitFinished(SystemEvent):
    ship: Entity
    origin: Entity
    destination: Entity
    departure: u64
    arrival: u64
    caller_crew: Entity
    caller: ContractAddress
    _key: int = _starknet_keccak('TransitFinished')


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
    _key: int = _starknet_keccak('TransitStarted')

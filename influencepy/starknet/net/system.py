from dataclasses import dataclass
from typing import List

from influencepy.starknet.net.datatypes import ContractAddress, CubitFixedPoint64, CubitFixedPoint128, u256, felt252
from influencepy.starknet.net.schema import System
from influencepy.starknet.net.structs import Entity, InventoryItem, Withdrawal, SeededAsteroid, SeededCrewmate


@dataclass
class AcceptContractAgreement(System, identifier='AcceptContractAgreement'):
    target: Entity
    permission: int
    permitted: Entity
    caller_crew: Entity


@dataclass
class AcceptPrepaidMerkleAgreement(System, identifier='AcceptPrepaidMerkleAgreement'):
    target: Entity
    permission: int
    permitted: Entity
    term: int
    merkle_proof: List[felt252]
    caller_crew: Entity


@dataclass
class AcceptPrepaidAgreement(System, identifier='AcceptPrepaidAgreement'):
    target: Entity
    permission: int
    permitted: Entity
    term: int
    caller_crew: Entity


@dataclass
class ExtendPrepaidAgreement(System, identifier='ExtendPrepaidAgreement'):
    target: Entity
    permission: int
    permitted: Entity
    added_term: int
    caller_crew: Entity


@dataclass
class CancelPrepaidAgreement(System, identifier='CancelPrepaidAgreement'):
    target: Entity
    permission: int
    permitted: Entity
    caller_crew: Entity


@dataclass
class RemoveFromWhitelist(System, identifier='RemoveFromWhitelist'):
    target: Entity
    permission: int
    permitted: Entity
    caller_crew: Entity


@dataclass
class RemoveAccountFromWhiteList(System, identifier='RemoveAccountFromWhiteList'):
    target: Entity
    permission: int
    permitted: ContractAddress
    caller_crew: Entity


@dataclass
class Whitelist(System, identifier='Whitelist'):
    target: Entity
    permission: int
    permitted: Entity
    caller_crew: Entity


@dataclass
class WhitelistAccount(System, identifier='WhitelistAccount'):
    target: Entity
    permission: int
    permitted: ContractAddress
    caller_crew: Entity


@dataclass
class ConstructionAbandon(System, identifier='ConstructionAbandon'):
    building: Entity
    caller_crew: Entity


@dataclass
class ConstructionDeconstruct(System, identifier='ConstructionDeconstruct'):
    building: Entity
    caller_crew: Entity


@dataclass
class ConstructionFinish(System, identifier='ConstructionFinish'):
    building: Entity
    caller_crew: Entity


@dataclass
class ConstructionPlan(System, identifier='ConstructionPlan'):
    building_type: int
    lot: Entity
    caller_crew: Entity


@dataclass
class ConstructionStart(System, identifier='ConstructionStart'):
    building: Entity
    caller_crew: Entity


@dataclass
class CommandeerShip(System, identifier='CommandeerShip'):
    ship: Entity
    caller_crew: Entity


@dataclass
class ManageAsteroid(System, identifier='ManageAsteroid'):
    asteroid: Entity
    caller_crew: Entity


@dataclass
class RepossessBuilding(System, identifier='RepossessBuilding'):
    building: Entity
    caller_crew: Entity


@dataclass
class ArrangeCrew(System, identifier='ArrangeCrew'):
    composition: List[int]
    caller_crew: Entity


@dataclass
class DelegateCrew(System, identifier='DelegateCrew'):
    delegated_to: ContractAddress
    caller_crew: Entity


@dataclass
class EjectCrew(System, identifier='EjectCrew'):
    ejected_crew: Entity
    caller_crew: Entity


@dataclass
class ExchangeCrew(System, identifier='ExchangeCrew'):
    crew1: Entity
    comp1: List[int]
    _crew2: Entity  # underscore as per the ABI
    comp2: List[int]


@dataclass
class InitializeArvadian(System, identifier='InitializeArvadian'):
    crewmate: Entity
    impactful: List[int]
    cosmetic: List[int]
    name: str
    station: Entity
    caller_crew: Entity


@dataclass
class RecruitAdalian(System, identifier='RecruitAdalian'):
    crewmate: Entity
    class_: int  # class is a reserved keyword
    impactful: List[int]
    cosmetic: List[int]
    gender: int
    body: int
    face: int
    hair: int
    hair_color: int
    clothes: int
    name: str
    station: Entity
    caller_crew: Entity


@dataclass
class ResupplyFood(System, identifier='ResupplyFood'):
    origin: Entity
    origin_slot: int
    food: int
    caller_crew: Entity


@dataclass
class ResupplyFoodFromExchange(System, identifier='ResupplyFoodFromExchange'):
    seller_crew: Entity
    exchange: Entity
    amount: int
    price: int
    storage: Entity
    storage_slot: int
    caller_crew: Entity


@dataclass
class StationCrew(System, identifier='StationCrew'):
    destination: Entity
    caller_crew: Entity


@dataclass
class AcceptDelivery(System, identifier='AcceptDelivery'):
    delivery: Entity
    caller_crew: Entity


@dataclass
class DumpDelivery(System, identifier='DumpDelivery'):
    origin: Entity
    origin_slot: int
    products: List[InventoryItem]
    caller_crew: Entity


@dataclass
class CancelDelivery(System, identifier='CancelDelivery'):
    delivery: Entity
    caller_crew: Entity


@dataclass
class PackageDelivery(System, identifier='PackageDelivery'):
    origin: Entity
    origin_slot: int
    products: List[InventoryItem]
    dest: Entity
    dest_slot: int
    price: int
    caller_crew: Entity


@dataclass
class ReceiveDelivery(System, identifier='ReceiveDelivery'):
    delivery: Entity
    caller_crew: Entity


@dataclass
class SendDelivery(System, identifier='SendDelivery'):
    origin: Entity
    origin_slot: int
    products: List[InventoryItem]
    dest: Entity
    dest_slot: int
    caller_crew: Entity


@dataclass
class SampleDepositStart(System, identifier='SampleDepositStart'):
    lot: Entity
    resource: int
    origin: Entity
    origin_slot: int
    caller_crew: Entity


@dataclass
class SampleDepositImprove(System, identifier='SampleDepositImprove'):
    deposit: Entity
    origin: Entity
    origin_slot: int
    caller_crew: Entity


@dataclass
class SampleDepositFinish(System, identifier='SampleDepositFinish'):
    deposit: Entity
    caller_crew: Entity


@dataclass
class ListDepositForSale(System, identifier='ListDepositForSale'):
    deposit: Entity
    price: int
    caller_crew: Entity


@dataclass
class PurchaseDeposit(System, identifier='PurchaseDeposit'):
    deposit: Entity
    caller_crew: Entity


@dataclass
class UnlistDepositForSale(System, identifier='UnlistDepositForSale'):
    deposit: Entity
    caller_crew: Entity


@dataclass
class ActivateEmergency(System, identifier='ActivateEmergency'):
    caller_crew: Entity


@dataclass
class CollectEmergencyPropellant(System, identifier='CollectEmergencyPropellant'):
    caller_crew: Entity


@dataclass
class DeactivateEmergency(System, identifier='DeactivateEmergency'):
    caller_crew: Entity


@dataclass
class CreateSellOrder(System, identifier='CreateSellOrder'):
    exchange: Entity
    product: int
    amount: int
    price: int
    storage: Entity
    storage_slot: int
    caller_crew: Entity


@dataclass
class FillSellOrder(System, identifier='FillSellOrder'):
    seller_crew: Entity
    exchange: Entity
    product: int
    amount: int
    price: int
    storage: Entity
    storage_slot: int
    destination: Entity
    destination_slot: int
    caller_crew: Entity


@dataclass
class CancelSellOrder(System, identifier='CancelSellOrder'):
    seller_crew: Entity
    exchange: Entity
    product: int
    price: int
    storage: Entity
    storage_slot: int
    caller_crew: Entity


@dataclass
class CreateBuyOrder(System, identifier='CreateBuyOrder'):
    exchange: Entity
    product: int
    amount: int
    price: int
    storage: Entity
    storage_slot: int
    caller_crew: Entity
    escrow_caller: ContractAddress
    escrow_type: int
    escrow_token: ContractAddress
    escrow_amount: int


@dataclass
class FillBuyOrder(System, identifier='FillBuyOrder'):
    buyer_crew: Entity
    exchange: Entity
    product: int
    price: int
    storage: Entity
    storage_slot: int
    amount: int
    origin: Entity
    origin_slot: int
    caller_crew: Entity
    escrow_caller: ContractAddress
    escrow_type: int
    escrow_token: ContractAddress
    escrow_withdrawals: List[Withdrawal]


@dataclass
class AssignContractPolicy(System, identifier='AssignContractPolicy'):
    target: Entity
    permission: int
    contract: ContractAddress
    caller_crew: Entity


@dataclass
class AssignPrepaidMerklePolicy(System, identifier='AssignPrepaidMerklePolicy'):
    target: Entity
    permission: int
    rate: int
    initial_term: int
    notice_period: int
    merkle_root: felt252
    caller_crew: Entity


@dataclass
class AssignPrepaidPolicy(System, identifier='AssignPrepaidPolicy'):
    target: Entity
    permission: int
    rate: int
    initial_term: int
    notice_period: int
    caller_crew: Entity


@dataclass
class AssignPublicPolicy(System, identifier='AssignPublicPolicy'):
    target: Entity
    permission: int
    caller_crew: Entity


@dataclass
class RemoveContractPolicy(System, identifier='RemoveContractPolicy'):
    target: Entity
    permission: int
    caller_crew: Entity


@dataclass
class RemovePrepaidPolicy(System, identifier='RemovePrepaidPolicy'):
    target: Entity
    permission: int
    caller_crew: Entity


@dataclass
class RemovePrepaidMerklePolicy(System, identifier='RemovePrepaidMerklePolicy'):
    target: Entity
    permission: int
    caller_crew: Entity


@dataclass
class RemovePublicPolicy(System, identifier='RemovePublicPolicy'):
    target: Entity
    permission: int
    caller_crew: Entity


@dataclass
class AssembleShipFinish(System, identifier='AssembleShipFinish'):
    dry_dock: Entity
    dry_dock_slot: int
    destination: Entity
    caller_crew: Entity


@dataclass
class AssembleShipStart(System, identifier='AssembleShipStart'):
    dry_dock: Entity
    dry_dock_slot: int
    ship_type: int
    origin: Entity
    origin_slot: int
    caller_crew: Entity


@dataclass
class ExtractResourceFinish(System, identifier='ExtractResourceFinish'):
    extractor: Entity
    extractor_slot: int
    caller_crew: Entity


@dataclass
class ExtractResourceStart(System, identifier='ExtractResourceStart'):
    deposit: Entity
    yield_: int  # yield is a reserved keyword
    extractor: Entity
    extractor_slot: int
    destination: Entity
    destination_slot: int
    caller_crew: Entity


@dataclass
class ProcessProductsFinish(System, identifier='ProcessProductsFinish'):
    processor: Entity
    processor_slot: int
    caller_crew: Entity


@dataclass
class ProcessProductsStart(System, identifier='ProcessProductsStart'):
    processor: Entity
    processor_slot: int
    process: int
    target_output: int
    recipes: CubitFixedPoint64
    origin: Entity
    origin_slot: int
    destination: Entity
    destination_slot: int
    caller_crew: Entity


@dataclass
class ResolveRandomEvent(System, identifier='ResolveRandomEvent'):
    choice: int
    caller_crew: Entity


@dataclass
class CheckForRandomEvent(System, identifier='CheckForRandomEvent'):
    # TODO: this is a 'view' function, so it should not be a System
    caller_crew: Entity


@dataclass
class ClaimArrivalReward(System, identifier='ClaimArrivalReward'):
    asteroid: Entity
    caller_crew: Entity


@dataclass
class ClaimPrepareForLaunchReward(System, identifier='ClaimPrepareForLaunchReward'):
    asteroid: Entity


@dataclass
class ClaimTestnetSway(System, identifier='ClaimTestnetSway'):
    proof: List[felt252]
    caller_crew: Entity


@dataclass
class PurchaseAdalian(System, identifier='PurchaseAdalian'):
    collection: int


@dataclass
class PurchaseAsteroid(System, identifier='PurchaseAsteroid'):
    asteroid: Entity
    caller_crew: Entity


@dataclass
class ScanResourcesFinish(System, identifier='ScanResourcesFinish'):
    asteroid: Entity
    caller_crew: Entity


@dataclass
class ScanResourcesStart(System, identifier='ScanResourcesStart'):
    asteroid: Entity
    caller_crew: Entity


@dataclass
class ScanSurfaceFinish(System, identifier='ScanSurfaceFinish'):
    asteroid: Entity
    caller_crew: Entity


@dataclass
class ScanSurfaceStart(System, identifier='ScanSurfaceStart'):
    asteroid: Entity
    caller_crew: Entity


@dataclass
class InitializeAsteroid(System, identifier='InitializeAsteroid'):
    asteroid: Entity
    celestial_type: int
    mass: int
    radius: int
    a: int
    ecc: int
    inc: int
    raan: int
    argp: int
    m: int
    purchase_order: int
    scan_status: int
    bonuses: int
    merkle_proof: List[felt252]


@dataclass
class SeedAsteroids(System, identifier='SeedAsteroids'):
    asteroids: List[SeededAsteroid]


@dataclass
class SeedCrewmates(System, identifier='SeedCrewmates'):
    crewmates: List[SeededCrewmate]


# NOTE: This is according to the system ABI, but it seems to be incorrect or incomplete
@dataclass
class SeedColony(System, identifier='SeedColony'):
    colony: int
    building_type: int


# NOTE: This is according to the system ABI, but it seems to be incorrect or incomplete
@dataclass
class SeedHabitat(System, identifier='SeedHabitat'):
    pass


# NOTE: This is according to the system ABI, but it seems to be incorrect or incomplete
@dataclass
class SeedOrders(System, identifier='SeedOrders'):
    market_lot: int
    warehouse_lot: int


@dataclass
class DockShip(System, identifier='DockShip'):
    target: Entity
    powered: bool
    caller_crew: Entity


@dataclass
class TransitBetweenFinish(System, identifier='TransitBetweenFinish'):
    caller_crew: Entity


@dataclass
class TransitBetweenStart(System, identifier='TransitBetweenStart'):
    origin: Entity
    destination: Entity
    departure_time: int
    arrival_time: int
    transit_p: CubitFixedPoint128
    transit_ecc: CubitFixedPoint128
    transit_inc: CubitFixedPoint128
    transit_raan: CubitFixedPoint128
    transit_argp: CubitFixedPoint128
    transit_nu_start: CubitFixedPoint128
    transit_nu_end: CubitFixedPoint128
    caller_crew: Entity


@dataclass
class UndockShip(System, identifier='UndockShip'):
    ship: Entity
    powered: bool
    caller_crew: Entity


@dataclass
class AnnotateEvent(System, identifier='AnnotateEvent'):
    transaction_hash: felt252
    log_index: int
    content_hash: List[felt252]
    caller_crew: Entity


@dataclass
class ChangeName(System, identifier='ChangeName'):
    entity: Entity
    name: u256
    caller_crew: Entity


@dataclass
class ConfigureExchange(System, identifier='ConfigureExchange'):
    exchange: Entity
    maker_fee: int
    taker_fee: int
    allowed_products: List[int]
    caller_crew: Entity


@dataclass
class ReadComponent(System, identifier='ReadComponent'):
    name: felt252
    path: List[felt252]
    # TODO: output is of type Span<felt252>, need to declare this somewhere?


@dataclass
class WriteComponent(System, identifier='WriteComponent'):
    name: felt252
    path: List[felt252]
    data: List[felt252]
    # TODO: state_mutability is 'view' which doesn't make sense for a write operation

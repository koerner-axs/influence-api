from dataclasses import dataclass
from typing import List

from influencepy.starknet.net.datatypes import ContractAddress, CubitFixedPoint64, CubitFixedPoint128, u256, felt252, \
    u64, shortstr, u128
from influencepy.starknet.net.schema import SystemCall, OneOf
from influencepy.starknet.net.structs import Entity, InventoryItem, Withdrawal, SeededAsteroid, SeededCrewmate


@dataclass
class AcceptContractAgreement(metaclass=OneOf[SystemCall], function_name='AcceptContractAgreement'):
    target: Entity
    permission: u64
    permitted: Entity
    caller_crew: Entity


@dataclass
class AcceptPrepaidMerkleAgreement(metaclass=OneOf[SystemCall], function_name='AcceptPrepaidMerkleAgreement'):
    target: Entity
    permission: u64
    permitted: Entity
    term: u64
    merkle_proof: List[felt252]
    caller_crew: Entity


@dataclass
class AcceptPrepaidAgreement(metaclass=OneOf[SystemCall], function_name='AcceptPrepaidAgreement'):
    target: Entity
    permission: u64
    permitted: Entity
    term: u64
    caller_crew: Entity


@dataclass
class ExtendPrepaidAgreement(metaclass=OneOf[SystemCall], function_name='ExtendPrepaidAgreement'):
    target: Entity
    permission: u64
    permitted: Entity
    added_term: u64
    caller_crew: Entity


@dataclass
class CancelPrepaidAgreement(metaclass=OneOf[SystemCall], function_name='CancelPrepaidAgreement'):
    target: Entity
    permission: u64
    permitted: Entity
    caller_crew: Entity


@dataclass
class RemoveFromWhitelist(metaclass=OneOf[SystemCall], function_name='RemoveFromWhitelist'):
    target: Entity
    permission: u64
    permitted: Entity
    caller_crew: Entity


@dataclass
class RemoveAccountFromWhiteList(metaclass=OneOf[SystemCall], function_name='RemoveAccountFromWhiteList'):
    target: Entity
    permission: u64
    permitted: ContractAddress
    caller_crew: Entity


@dataclass
class Whitelist(metaclass=OneOf[SystemCall], function_name='Whitelist'):
    target: Entity
    permission: u64
    permitted: Entity
    caller_crew: Entity


@dataclass
class WhitelistAccount(metaclass=OneOf[SystemCall], function_name='WhitelistAccount'):
    target: Entity
    permission: u64
    permitted: ContractAddress
    caller_crew: Entity


@dataclass
class ConstructionAbandon(metaclass=OneOf[SystemCall], function_name='ConstructionAbandon'):
    building: Entity
    caller_crew: Entity


@dataclass
class ConstructionDeconstruct(metaclass=OneOf[SystemCall], function_name='ConstructionDeconstruct'):
    building: Entity
    caller_crew: Entity


@dataclass
class ConstructionFinish(metaclass=OneOf[SystemCall], function_name='ConstructionFinish'):
    building: Entity
    caller_crew: Entity


@dataclass
class ConstructionPlan(metaclass=OneOf[SystemCall], function_name='ConstructionPlan'):
    building_type: u64
    lot: Entity
    caller_crew: Entity


@dataclass
class ConstructionStart(metaclass=OneOf[SystemCall], function_name='ConstructionStart'):
    building: Entity
    caller_crew: Entity


@dataclass
class CommandeerShip(metaclass=OneOf[SystemCall], function_name='CommandeerShip'):
    ship: Entity
    caller_crew: Entity


@dataclass
class ManageAsteroid(metaclass=OneOf[SystemCall], function_name='ManageAsteroid'):
    asteroid: Entity
    caller_crew: Entity


@dataclass
class RepossessBuilding(metaclass=OneOf[SystemCall], function_name='RepossessBuilding'):
    building: Entity
    caller_crew: Entity


@dataclass
class ArrangeCrew(metaclass=OneOf[SystemCall], function_name='ArrangeCrew'):
    composition: List[u64]
    caller_crew: Entity


@dataclass
class DelegateCrew(metaclass=OneOf[SystemCall], function_name='DelegateCrew'):
    delegated_to: ContractAddress
    caller_crew: Entity


@dataclass
class EjectCrew(metaclass=OneOf[SystemCall], function_name='EjectCrew'):
    ejected_crew: Entity
    caller_crew: Entity


@dataclass
class ExchangeCrew(metaclass=OneOf[SystemCall], function_name='ExchangeCrew'):
    crew1: Entity
    comp1: List[u64]
    crew2: Entity  # ABI specifies a leading _
    comp2: List[u64]


@dataclass
class InitializeArvadian(metaclass=OneOf[SystemCall], function_name='InitializeArvadian'):
    crewmate: Entity
    impactful: List[u64]
    cosmetic: List[u64]
    name: shortstr
    station: Entity
    caller_crew: Entity


@dataclass
class RecruitAdalian(metaclass=OneOf[SystemCall], function_name='RecruitAdalian'):
    crewmate: Entity
    class_: u64  # class is a reserved keyword
    impactful: List[u64]
    cosmetic: List[u64]
    gender: u64
    body: u64
    face: u64
    hair: u64
    hair_color: u64
    clothes: u64
    name: shortstr
    station: Entity
    caller_crew: Entity


@dataclass
class ResupplyFood(metaclass=OneOf[SystemCall], function_name='ResupplyFood'):
    origin: Entity
    origin_slot: u64
    food: u64
    caller_crew: Entity


@dataclass
class ResupplyFoodFromExchange(metaclass=OneOf[SystemCall], function_name='ResupplyFoodFromExchange'):
    seller_crew: Entity
    exchange: Entity
    amount: u64
    price: u64
    storage: Entity
    storage_slot: u64
    caller_crew: Entity


@dataclass
class StationCrew(metaclass=OneOf[SystemCall], function_name='StationCrew'):
    destination: Entity
    caller_crew: Entity


@dataclass
class AcceptDelivery(metaclass=OneOf[SystemCall], function_name='AcceptDelivery'):
    delivery: Entity
    caller_crew: Entity


@dataclass
class DumpDelivery(metaclass=OneOf[SystemCall], function_name='DumpDelivery'):
    origin: Entity
    origin_slot: u64
    products: List[InventoryItem]
    caller_crew: Entity


@dataclass
class CancelDelivery(metaclass=OneOf[SystemCall], function_name='CancelDelivery'):
    delivery: Entity
    caller_crew: Entity


@dataclass
class PackageDelivery(metaclass=OneOf[SystemCall], function_name='PackageDelivery'):
    origin: Entity
    origin_slot: u64
    products: List[InventoryItem]
    dest: Entity
    dest_slot: u64
    price: u64
    caller_crew: Entity


@dataclass
class ReceiveDelivery(metaclass=OneOf[SystemCall], function_name='ReceiveDelivery'):
    delivery: Entity
    caller_crew: Entity


@dataclass
class SendDelivery(metaclass=OneOf[SystemCall], function_name='SendDelivery'):
    origin: Entity
    origin_slot: u64
    products: List[InventoryItem]
    dest: Entity
    dest_slot: u64
    caller_crew: Entity


@dataclass
class SampleDepositStart(metaclass=OneOf[SystemCall], function_name='SampleDepositStart'):
    lot: Entity
    resource: u64
    origin: Entity
    origin_slot: u64
    caller_crew: Entity


@dataclass
class SampleDepositImprove(metaclass=OneOf[SystemCall], function_name='SampleDepositImprove'):
    deposit: Entity
    origin: Entity
    origin_slot: u64
    caller_crew: Entity


@dataclass
class SampleDepositFinish(metaclass=OneOf[SystemCall], function_name='SampleDepositFinish'):
    deposit: Entity
    caller_crew: Entity


@dataclass
class ListDepositForSale(metaclass=OneOf[SystemCall], function_name='ListDepositForSale'):
    deposit: Entity
    price: u64
    caller_crew: Entity


@dataclass
class PurchaseDeposit(metaclass=OneOf[SystemCall], function_name='PurchaseDeposit'):
    deposit: Entity
    caller_crew: Entity


@dataclass
class UnlistDepositForSale(metaclass=OneOf[SystemCall], function_name='UnlistDepositForSale'):
    deposit: Entity
    caller_crew: Entity


@dataclass
class ActivateEmergency(metaclass=OneOf[SystemCall], function_name='ActivateEmergency'):
    caller_crew: Entity


@dataclass
class CollectEmergencyPropellant(metaclass=OneOf[SystemCall], function_name='CollectEmergencyPropellant'):
    caller_crew: Entity


@dataclass
class DeactivateEmergency(metaclass=OneOf[SystemCall], function_name='DeactivateEmergency'):
    caller_crew: Entity


@dataclass
class CreateSellOrder(metaclass=OneOf[SystemCall], function_name='CreateSellOrder'):
    exchange: Entity
    product: u64
    amount: u64
    price: u64
    storage: Entity
    storage_slot: u64
    caller_crew: Entity


@dataclass
class FillSellOrder(metaclass=OneOf[SystemCall], function_name='FillSellOrder'):
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


@dataclass
class CancelSellOrder(metaclass=OneOf[SystemCall], function_name='CancelSellOrder'):
    seller_crew: Entity
    exchange: Entity
    product: u64
    price: u64
    storage: Entity
    storage_slot: u64
    caller_crew: Entity


@dataclass
class CreateBuyOrder(metaclass=OneOf[SystemCall], function_name='CreateBuyOrder'):
    exchange: Entity
    product: u64
    amount: u64
    price: u64
    storage: Entity
    storage_slot: u64
    caller_crew: Entity
    escrow_caller: ContractAddress
    escrow_type: u64
    escrow_token: ContractAddress
    escrow_amount: u256


@dataclass
class FillBuyOrder(metaclass=OneOf[SystemCall], function_name='FillBuyOrder'):
    buyer_crew: Entity
    exchange: Entity
    product: u64
    price: u64
    storage: Entity
    storage_slot: u64
    amount: u64
    origin: Entity
    origin_slot: u64
    caller_crew: Entity
    escrow_caller: ContractAddress
    escrow_type: u64
    escrow_token: ContractAddress
    escrow_withdrawals: List[Withdrawal]


@dataclass
class AssignContractPolicy(metaclass=OneOf[SystemCall], function_name='AssignContractPolicy'):
    target: Entity
    permission: u64
    contract: ContractAddress
    caller_crew: Entity


@dataclass
class AssignPrepaidMerklePolicy(metaclass=OneOf[SystemCall], function_name='AssignPrepaidMerklePolicy'):
    target: Entity
    permission: u64
    rate: u64
    initial_term: u64
    notice_period: u64
    merkle_root: felt252
    caller_crew: Entity


@dataclass
class AssignPrepaidPolicy(metaclass=OneOf[SystemCall], function_name='AssignPrepaidPolicy'):
    target: Entity
    permission: u64
    rate: u64
    initial_term: u64
    notice_period: u64
    caller_crew: Entity


@dataclass
class AssignPublicPolicy(metaclass=OneOf[SystemCall], function_name='AssignPublicPolicy'):
    target: Entity
    permission: u64
    caller_crew: Entity


@dataclass
class RemoveContractPolicy(metaclass=OneOf[SystemCall], function_name='RemoveContractPolicy'):
    target: Entity
    permission: u64
    caller_crew: Entity


@dataclass
class RemovePrepaidPolicy(metaclass=OneOf[SystemCall], function_name='RemovePrepaidPolicy'):
    target: Entity
    permission: u64
    caller_crew: Entity


@dataclass
class RemovePrepaidMerklePolicy(metaclass=OneOf[SystemCall], function_name='RemovePrepaidMerklePolicy'):
    target: Entity
    permission: u64
    caller_crew: Entity


@dataclass
class RemovePublicPolicy(metaclass=OneOf[SystemCall], function_name='RemovePublicPolicy'):
    target: Entity
    permission: u64
    caller_crew: Entity


@dataclass
class AssembleShipFinish(metaclass=OneOf[SystemCall], function_name='AssembleShipFinish'):
    dry_dock: Entity
    dry_dock_slot: u64
    destination: Entity
    caller_crew: Entity


@dataclass
class AssembleShipStart(metaclass=OneOf[SystemCall], function_name='AssembleShipStart'):
    dry_dock: Entity
    dry_dock_slot: u64
    ship_type: u64
    origin: Entity
    origin_slot: u64
    caller_crew: Entity


@dataclass
class ExtractResourceFinish(metaclass=OneOf[SystemCall], function_name='ExtractResourceFinish'):
    extractor: Entity
    extractor_slot: u64
    caller_crew: Entity


@dataclass
class ExtractResourceStart(metaclass=OneOf[SystemCall], function_name='ExtractResourceStart'):
    deposit: Entity
    yield_: u64  # yield is a reserved keyword
    extractor: Entity
    extractor_slot: u64
    destination: Entity
    destination_slot: u64
    caller_crew: Entity


@dataclass
class ProcessProductsFinish(metaclass=OneOf[SystemCall], function_name='ProcessProductsFinish'):
    processor: Entity
    processor_slot: u64
    caller_crew: Entity


@dataclass
class ProcessProductsStart(metaclass=OneOf[SystemCall], function_name='ProcessProductsStart'):
    processor: Entity
    processor_slot: u64
    process: u64
    target_output: u64
    recipes: CubitFixedPoint64
    origin: Entity
    origin_slot: u64
    destination: Entity
    destination_slot: u64
    caller_crew: Entity


@dataclass
class ResolveRandomEvent(metaclass=OneOf[SystemCall], function_name='ResolveRandomEvent'):
    choice: u64
    caller_crew: Entity


@dataclass
class CheckForRandomEvent(metaclass=OneOf[SystemCall], function_name='CheckForRandomEvent'):
    # TODO: this is a 'view' function, so it should not be a System
    caller_crew: Entity
    # TODO: output is of type u64, need to declare this somewhere?


@dataclass
class ClaimArrivalReward(metaclass=OneOf[SystemCall], function_name='ClaimArrivalReward'):
    asteroid: Entity
    caller_crew: Entity


@dataclass
class ClaimPrepareForLaunchReward(metaclass=OneOf[SystemCall], function_name='ClaimPrepareForLaunchReward'):
    asteroid: Entity


@dataclass
class ClaimTestnetSway(metaclass=OneOf[SystemCall], function_name='ClaimTestnetSway'):
    proof: List[felt252]
    amount: u256


@dataclass
class PurchaseAdalian(metaclass=OneOf[SystemCall], function_name='PurchaseAdalian'):
    collection: u64


@dataclass
class PurchaseAsteroid(metaclass=OneOf[SystemCall], function_name='PurchaseAsteroid'):
    asteroid: Entity
    caller_crew: Entity


@dataclass
class ScanResourcesFinish(metaclass=OneOf[SystemCall], function_name='ScanResourcesFinish'):
    asteroid: Entity
    caller_crew: Entity


@dataclass
class ScanResourcesStart(metaclass=OneOf[SystemCall], function_name='ScanResourcesStart'):
    asteroid: Entity
    caller_crew: Entity


@dataclass
class ScanSurfaceFinish(metaclass=OneOf[SystemCall], function_name='ScanSurfaceFinish'):
    asteroid: Entity
    caller_crew: Entity


@dataclass
class ScanSurfaceStart(metaclass=OneOf[SystemCall], function_name='ScanSurfaceStart'):
    asteroid: Entity
    caller_crew: Entity


@dataclass
class InitializeAsteroid(metaclass=OneOf[SystemCall], function_name='InitializeAsteroid'):
    asteroid: Entity
    celestial_type: u64
    mass: u128
    radius: u64
    a: u128
    ecc: u128
    inc: u128
    raan: u128
    argp: u128
    m: u128
    purchase_order: u64
    scan_status: u64
    bonuses: u64
    merkle_proof: List[felt252]


@dataclass
class SeedAsteroids(metaclass=OneOf[SystemCall], function_name='SeedAsteroids'):
    asteroids: List[SeededAsteroid]


@dataclass
class SeedCrewmates(metaclass=OneOf[SystemCall], function_name='SeedCrewmates'):
    crewmates: List[SeededCrewmate]


# NOTE: This is according to the system ABI, but it seems to be incorrect or incomplete
@dataclass
class SeedColony(metaclass=OneOf[SystemCall], function_name='SeedColony'):
    colony: u64
    building_type: u64


# NOTE: This is according to the system ABI, but it seems to be incorrect or incomplete
@dataclass
class SeedHabitat(metaclass=OneOf[SystemCall], function_name='SeedHabitat'):
    pass


# NOTE: This is according to the system ABI, but it seems to be incorrect or incomplete
@dataclass
class SeedOrders(metaclass=OneOf[SystemCall], function_name='SeedOrders'):
    market_lot: u64
    warehouse_lot: u64


@dataclass
class DockShip(metaclass=OneOf[SystemCall], function_name='DockShip'):
    target: Entity
    powered: bool
    caller_crew: Entity


@dataclass
class TransitBetweenFinish(metaclass=OneOf[SystemCall], function_name='TransitBetweenFinish'):
    caller_crew: Entity


@dataclass
class TransitBetweenStart(metaclass=OneOf[SystemCall], function_name='TransitBetweenStart'):
    origin: Entity
    destination: Entity
    departure_time: u64
    arrival_time: u64
    transit_p: CubitFixedPoint128
    transit_ecc: CubitFixedPoint128
    transit_inc: CubitFixedPoint128
    transit_raan: CubitFixedPoint128
    transit_argp: CubitFixedPoint128
    transit_nu_start: CubitFixedPoint128
    transit_nu_end: CubitFixedPoint128
    caller_crew: Entity


@dataclass
class UndockShip(metaclass=OneOf[SystemCall], function_name='UndockShip'):
    ship: Entity
    powered: bool
    caller_crew: Entity


@dataclass
class AnnotateEvent(metaclass=OneOf[SystemCall], function_name='AnnotateEvent'):
    transaction_hash: felt252
    log_index: u64
    content_hash: List[felt252]
    caller_crew: Entity


@dataclass
class ChangeName(metaclass=OneOf[SystemCall], function_name='ChangeName'):
    entity: Entity
    name: shortstr
    caller_crew: Entity


@dataclass
class ConfigureExchange(metaclass=OneOf[SystemCall], function_name='ConfigureExchange'):
    exchange: Entity
    maker_fee: u64
    taker_fee: u64
    allowed_products: List[u64]
    caller_crew: Entity


@dataclass
class ReadComponent(metaclass=OneOf[SystemCall], function_name='ReadComponent'):
    name: felt252  # TODO: could also be a shortstr
    path: List[felt252]
    # TODO: output is of type Span<felt252>, need to declare this somewhere?


@dataclass
class WriteComponent(metaclass=OneOf[SystemCall], function_name='WriteComponent'):
    name: felt252  # TODO: could also be a shortstr
    path: List[felt252]
    data: List[felt252]
    # TODO: state_mutability is 'view' which doesn't make sense for a write operation

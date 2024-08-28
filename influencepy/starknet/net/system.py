from dataclasses import dataclass
from typing import List

from influencepy.starknet.net.datatypes import ContractAddress, CubitFixedPoint64, CubitFixedPoint128, u256, felt252, \
    u64, shortstr, u128
from influencepy.starknet.net.schema import SystemCallDispatcher, OneOf, SystemCall
from influencepy.starknet.net.structs import Entity, InventoryItem, Withdrawal, SeededAsteroid, SeededCrewmate


@dataclass
class AcceptContractAgreement(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='AcceptContractAgreement'):
    target: Entity
    permission: u64
    permitted: Entity
    caller_crew: Entity


@dataclass
class AcceptPrepaidMerkleAgreement(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='AcceptPrepaidMerkleAgreement'):
    target: Entity
    permission: u64
    permitted: Entity
    term: u64
    merkle_proof: List[felt252]
    caller_crew: Entity


@dataclass
class AcceptPrepaidAgreement(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='AcceptPrepaidAgreement'):
    target: Entity
    permission: u64
    permitted: Entity
    term: u64
    caller_crew: Entity


@dataclass
class ExtendPrepaidAgreement(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='ExtendPrepaidAgreement'):
    target: Entity
    permission: u64
    permitted: Entity
    added_term: u64
    caller_crew: Entity


@dataclass
class CancelPrepaidAgreement(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='CancelPrepaidAgreement'):
    target: Entity
    permission: u64
    permitted: Entity
    caller_crew: Entity


@dataclass
class RemoveFromWhitelist(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='RemoveFromWhitelist'):
    target: Entity
    permission: u64
    permitted: Entity
    caller_crew: Entity


@dataclass
class RemoveAccountFromWhiteList(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='RemoveAccountFromWhiteList'):
    target: Entity
    permission: u64
    permitted: ContractAddress
    caller_crew: Entity


@dataclass
class Whitelist(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='Whitelist'):
    target: Entity
    permission: u64
    permitted: Entity
    caller_crew: Entity


@dataclass
class WhitelistAccount(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='WhitelistAccount'):
    target: Entity
    permission: u64
    permitted: ContractAddress
    caller_crew: Entity


@dataclass
class ConstructionAbandon(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='ConstructionAbandon'):
    building: Entity
    caller_crew: Entity


@dataclass
class ConstructionDeconstruct(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='ConstructionDeconstruct'):
    building: Entity
    caller_crew: Entity


@dataclass
class ConstructionFinish(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='ConstructionFinish'):
    building: Entity
    caller_crew: Entity


@dataclass
class ConstructionPlan(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='ConstructionPlan'):
    building_type: u64
    lot: Entity
    caller_crew: Entity


@dataclass
class ConstructionStart(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='ConstructionStart'):
    building: Entity
    caller_crew: Entity


@dataclass
class CommandeerShip(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='CommandeerShip'):
    ship: Entity
    caller_crew: Entity


@dataclass
class ManageAsteroid(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='ManageAsteroid'):
    asteroid: Entity
    caller_crew: Entity


@dataclass
class RepossessBuilding(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='RepossessBuilding'):
    building: Entity
    caller_crew: Entity


@dataclass
class ArrangeCrew(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='ArrangeCrew'):
    composition: List[u64]
    caller_crew: Entity


@dataclass
class DelegateCrew(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='DelegateCrew'):
    delegated_to: ContractAddress
    caller_crew: Entity


@dataclass
class EjectCrew(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='EjectCrew'):
    ejected_crew: Entity
    caller_crew: Entity


@dataclass
class ExchangeCrew(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='ExchangeCrew'):
    crew1: Entity
    comp1: List[u64]
    crew2: Entity  # ABI specifies a leading _
    comp2: List[u64]


@dataclass
class InitializeArvadian(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='InitializeArvadian'):
    crewmate: Entity
    impactful: List[u64]
    cosmetic: List[u64]
    name: shortstr
    station: Entity
    caller_crew: Entity


@dataclass
class RecruitAdalian(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='RecruitAdalian'):
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
class ResupplyFood(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='ResupplyFood'):
    origin: Entity
    origin_slot: u64
    food: u64
    caller_crew: Entity


@dataclass
class ResupplyFoodFromExchange(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='ResupplyFoodFromExchange'):
    seller_crew: Entity
    exchange: Entity
    amount: u64
    price: u64
    storage: Entity
    storage_slot: u64
    caller_crew: Entity


@dataclass
class StationCrew(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='StationCrew'):
    destination: Entity
    caller_crew: Entity


@dataclass
class AcceptDelivery(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='AcceptDelivery'):
    delivery: Entity
    caller_crew: Entity


@dataclass
class DumpDelivery(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='DumpDelivery'):
    origin: Entity
    origin_slot: u64
    products: List[InventoryItem]
    caller_crew: Entity


@dataclass
class CancelDelivery(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='CancelDelivery'):
    delivery: Entity
    caller_crew: Entity


@dataclass
class PackageDelivery(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='PackageDelivery'):
    origin: Entity
    origin_slot: u64
    products: List[InventoryItem]
    dest: Entity
    dest_slot: u64
    price: u64
    caller_crew: Entity


@dataclass
class ReceiveDelivery(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='ReceiveDelivery'):
    delivery: Entity
    caller_crew: Entity


@dataclass
class SendDelivery(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='SendDelivery'):
    origin: Entity
    origin_slot: u64
    products: List[InventoryItem]
    dest: Entity
    dest_slot: u64
    caller_crew: Entity


@dataclass
class SampleDepositStart(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='SampleDepositStart'):
    lot: Entity
    resource: u64
    origin: Entity
    origin_slot: u64
    caller_crew: Entity


@dataclass
class SampleDepositImprove(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='SampleDepositImprove'):
    deposit: Entity
    origin: Entity
    origin_slot: u64
    caller_crew: Entity


@dataclass
class SampleDepositFinish(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='SampleDepositFinish'):
    deposit: Entity
    caller_crew: Entity


@dataclass
class ListDepositForSale(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='ListDepositForSale'):
    deposit: Entity
    price: u64
    caller_crew: Entity


@dataclass
class PurchaseDeposit(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='PurchaseDeposit'):
    deposit: Entity
    caller_crew: Entity


@dataclass
class UnlistDepositForSale(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='UnlistDepositForSale'):
    deposit: Entity
    caller_crew: Entity


@dataclass
class ActivateEmergency(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='ActivateEmergency'):
    caller_crew: Entity


@dataclass
class CollectEmergencyPropellant(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='CollectEmergencyPropellant'):
    caller_crew: Entity


@dataclass
class DeactivateEmergency(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='DeactivateEmergency'):
    caller_crew: Entity


@dataclass
class CreateSellOrder(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='CreateSellOrder'):
    exchange: Entity
    product: u64
    amount: u64
    price: u64
    storage: Entity
    storage_slot: u64
    caller_crew: Entity


@dataclass
class FillSellOrder(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='FillSellOrder'):
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
class CancelSellOrder(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='CancelSellOrder'):
    seller_crew: Entity
    exchange: Entity
    product: u64
    price: u64
    storage: Entity
    storage_slot: u64
    caller_crew: Entity


@dataclass
class CreateBuyOrder(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='CreateBuyOrder'):
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
class FillBuyOrder(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='FillBuyOrder'):
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
class AssignContractPolicy(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='AssignContractPolicy'):
    target: Entity
    permission: u64
    contract: ContractAddress
    caller_crew: Entity


@dataclass
class AssignPrepaidMerklePolicy(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='AssignPrepaidMerklePolicy'):
    target: Entity
    permission: u64
    rate: u64
    initial_term: u64
    notice_period: u64
    merkle_root: felt252
    caller_crew: Entity


@dataclass
class AssignPrepaidPolicy(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='AssignPrepaidPolicy'):
    target: Entity
    permission: u64
    rate: u64
    initial_term: u64
    notice_period: u64
    caller_crew: Entity


@dataclass
class AssignPublicPolicy(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='AssignPublicPolicy'):
    target: Entity
    permission: u64
    caller_crew: Entity


@dataclass
class RemoveContractPolicy(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='RemoveContractPolicy'):
    target: Entity
    permission: u64
    caller_crew: Entity


@dataclass
class RemovePrepaidPolicy(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='RemovePrepaidPolicy'):
    target: Entity
    permission: u64
    caller_crew: Entity


@dataclass
class RemovePrepaidMerklePolicy(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='RemovePrepaidMerklePolicy'):
    target: Entity
    permission: u64
    caller_crew: Entity


@dataclass
class RemovePublicPolicy(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='RemovePublicPolicy'):
    target: Entity
    permission: u64
    caller_crew: Entity


@dataclass
class AssembleShipFinish(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='AssembleShipFinish'):
    dry_dock: Entity
    dry_dock_slot: u64
    destination: Entity
    caller_crew: Entity


@dataclass
class AssembleShipStart(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='AssembleShipStart'):
    dry_dock: Entity
    dry_dock_slot: u64
    ship_type: u64
    origin: Entity
    origin_slot: u64
    caller_crew: Entity


@dataclass
class ExtractResourceFinish(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='ExtractResourceFinish'):
    extractor: Entity
    extractor_slot: u64
    caller_crew: Entity


@dataclass
class ExtractResourceStart(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='ExtractResourceStart'):
    deposit: Entity
    yield_: u64  # yield is a reserved keyword
    extractor: Entity
    extractor_slot: u64
    destination: Entity
    destination_slot: u64
    caller_crew: Entity


@dataclass
class ProcessProductsFinish(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='ProcessProductsFinish'):
    processor: Entity
    processor_slot: u64
    caller_crew: Entity


@dataclass
class ProcessProductsStart(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='ProcessProductsStart'):
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
class ResolveRandomEvent(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='ResolveRandomEvent'):
    choice: u64
    caller_crew: Entity


@dataclass
class CheckForRandomEvent(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='CheckForRandomEvent'):
    # TODO: this is a 'view' function, so it should not be a System
    caller_crew: Entity
    # TODO: output is of type u64, need to declare this somewhere?


@dataclass
class ClaimArrivalReward(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='ClaimArrivalReward'):
    asteroid: Entity
    caller_crew: Entity


@dataclass
class ClaimPrepareForLaunchReward(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='ClaimPrepareForLaunchReward'):
    asteroid: Entity


@dataclass
class ClaimTestnetSway(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='ClaimTestnetSway'):
    proof: List[felt252]
    amount: u256


@dataclass
class PurchaseAdalian(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='PurchaseAdalian'):
    collection: u64


@dataclass
class PurchaseAsteroid(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='PurchaseAsteroid'):
    asteroid: Entity
    caller_crew: Entity


@dataclass
class ScanResourcesFinish(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='ScanResourcesFinish'):
    asteroid: Entity
    caller_crew: Entity


@dataclass
class ScanResourcesStart(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='ScanResourcesStart'):
    asteroid: Entity
    caller_crew: Entity


@dataclass
class ScanSurfaceFinish(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='ScanSurfaceFinish'):
    asteroid: Entity
    caller_crew: Entity


@dataclass
class ScanSurfaceStart(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='ScanSurfaceStart'):
    asteroid: Entity
    caller_crew: Entity


@dataclass
class InitializeAsteroid(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='InitializeAsteroid'):
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
class SeedAsteroids(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='SeedAsteroids'):
    asteroids: List[SeededAsteroid]


@dataclass
class SeedCrewmates(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='SeedCrewmates'):
    crewmates: List[SeededCrewmate]


# NOTE: This is according to the system ABI, but it seems to be incorrect or incomplete
@dataclass
class SeedColony(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='SeedColony'):
    colony: u64
    building_type: u64


# NOTE: This is according to the system ABI, but it seems to be incorrect or incomplete
@dataclass
class SeedHabitat(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='SeedHabitat'):
    pass


# NOTE: This is according to the system ABI, but it seems to be incorrect or incomplete
@dataclass
class SeedOrders(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='SeedOrders'):
    market_lot: u64
    warehouse_lot: u64


@dataclass
class DockShip(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='DockShip'):
    target: Entity
    powered: bool
    caller_crew: Entity


@dataclass
class TransitBetweenFinish(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='TransitBetweenFinish'):
    caller_crew: Entity


@dataclass
class TransitBetweenStart(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='TransitBetweenStart'):
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
class UndockShip(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='UndockShip'):
    ship: Entity
    powered: bool
    caller_crew: Entity


@dataclass
class AnnotateEvent(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='AnnotateEvent'):
    transaction_hash: felt252
    log_index: u64
    content_hash: List[felt252]
    caller_crew: Entity


@dataclass
class ChangeName(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='ChangeName'):
    entity: Entity
    name: shortstr
    caller_crew: Entity


@dataclass
class ConfigureExchange(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='ConfigureExchange'):
    exchange: Entity
    maker_fee: u64
    taker_fee: u64
    allowed_products: List[u64]
    caller_crew: Entity


@dataclass
class ReadComponent(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='ReadComponent'):
    name: felt252  # TODO: could also be a shortstr
    path: List[felt252]
    # TODO: output is of type Span<felt252>, need to declare this somewhere?


@dataclass
class WriteComponent(SystemCall, metaclass=OneOf[SystemCallDispatcher], function_name='WriteComponent'):
    name: felt252  # TODO: could also be a shortstr
    path: List[felt252]
    data: List[felt252]
    # TODO: state_mutability is 'view' which doesn't make sense for a write operation

from dataclasses import dataclass

from influencepy.starknet.net.datatypes import Entity


@dataclass
class Syscall:
    functionName: str


@dataclass
class AcceptContractAgreement(Syscall):
    target: Entity
    permission: int
    permitted: Entity
    caller_crew: Entity


@dataclass
class AcceptPrepaidMerkleAgreement(Syscall):
    target: Entity
    permission: int
    permitted: Entity
    term: int
    merkle_proof: Span<Felt> ????
    caller_crew: Entity


@dataclass
class AcceptPrepaidAgreement(Syscall):
    target: Entity
    permission: int
    permitted: Entity
    term: int
    caller_crew: Entity


@dataclass
class ExtendPrepaidAgreement(Syscall):
    target: Entity
    permission: int
    permitted: Entity
    added_term: int
    caller_crew: Entity


@dataclass
class CancelPrepaidAgreement(Syscall):
    target: Entity
    permission: int
    permitted: Entity
    caller_crew: Entity


@dataclass
class RemoveFromWhitelist(Syscall):
    target: Entity
    permission: int
    permitted: Entity
    caller_crew: Entity


@dataclass
class RemoveAccountFromWhiteList(Syscall):
    target: Entity
    permission: int
    permitted: ContractAddress ????
    caller_crew: Entity


@dataclass
class Whitelist(Syscall):
    target: Entity
    permission: int
    permitted: Entity
    caller_crew: Entity


@dataclass
class WhitelistAccount(Syscall):
    target: Entity
    permission: int
    permitted: ContractAddress ????
    caller_crew: Entity


@dataclass
class ConstructionAbandon(Syscall):
    building: Entity
    caller_crew: Entity


@dataclass
class ConstructionDeconstruct(Syscall):
    building: Entity
    caller_crew: Entity


@dataclass
class ConstructionFinish(Syscall):
    building: Entity
    caller_crew: Entity


@dataclass
class ConstructionPlan(Syscall):
    building_type: int
    lot: Entity
    caller_crew: Entity


@dataclass
class ConstructionStart(Syscall):
    building: Entity
    caller_crew: Entity


@dataclass
class CommandeerShip(Syscall):
    ship: Entity
    caller_crew: Entity


@dataclass
class ManageAsteroid(Syscall):
    asteroid: Entity
    caller_crew: Entity


@dataclass
class RepossessBuilding(Syscall):
    building: Entity
    caller_crew: Entity


@dataclass
class ArrangeCrew(Syscall):
    composition: Span<Int> ????
    caller_crew: Entity


@dataclass
class DelegateCrew(Syscall):
    delegated_to: ContractAddress ????
    caller_crew: Entity


@dataclass
class EjectCrew(Syscall):
    ejected_crew: Entity
    caller_crew: Entity


@dataclass
class ExchangeCrew(Syscall):
    crew1: Entity
    comp1: Span<Int> ????
    _crew2: Entity
    comp2: Span<Int> ????


@dataclass
class InitializeArvadian(Syscall):
    crewmate: Entity
    impactful: Span<Int> ????
    cosmetic: Span<Int> ????
    name: Felt oder str ????
    station: Entity
    caller_crew: Entity


@dataclass
class RecruitAdalian(Syscall):
    crewmate: Entity
    class: int
    impactful: Span<Int> ????
    cosmetic: Span<Int> ????
    gender: int
    body: int
    face: int
    hair: int
    hair_color: int
    clothes: int
    name: Felt oder str ????
    station: Entity
    caller_crew: Entity


@dataclass
class ResupplyFood(Syscall):
    origin: Entity
    origin_slot: int
    food: int
    caller_crew: Entity


@dataclass
class ResupplyFoodFromExchange(Syscall):
    seller_crew: Entity
    exchange: Entity
    amount: int
    price: int
    storage: Entity
    storage_slot: int
    caller_crew: Entity


@dataclass
class StationCrew(Syscall):
    destination: Entity
    caller_crew: Entity


@dataclass
class AcceptDelivery(Syscall):
    delivery: Entity
    caller_crew: Entity


@dataclass
class DumpDelivery(Syscall):
    origin: Entity
    origin_slot: int
    products: Span<InventoryItem> ????
    caller_crew: Entity


@dataclass
class CancelDelivery(Syscall):
    delivery: Entity
    caller_crew: Entity


@dataclass
class PackageDelivery(Syscall):
    origin: Entity
    origin_slot: int
    products: Span<InventoryItem> ????
    dest: Entity
    dest_slot: int
    price: int
    caller_crew: Entity


@dataclass
class ReceiveDelivery(Syscall):
    delivery: Entity
    caller_crew: Entity


@dataclass
class SendDelivery(Syscall):
    origin: Entity
    origin_slot: int
    products: Span<InventoryItem> ????
    dest: Entity
    dest_slot: int
    caller_crew: Entity


@dataclass
class SampleDepositStart(Syscall):
    lot: Entity
    resource: int
    origin: Entity
    origin_slot: int
    caller_crew: Entity


@dataclass
class SampleDepositImprove(Syscall):
    deposit: Entity
    origin: Entity
    origin_slot: int
    caller_crew: Entity


@dataclass
class SampleDepositFinish(Syscall):
    deposit: Entity
    caller_crew: Entity


@dataclass
class ListDepositForSale(Syscall):
    deposit: Entity
    price: int
    caller_crew: Entity


@dataclass
class PurchaseDeposit(Syscall):
    deposit: Entity
    caller_crew: Entity


@dataclass
class UnlistDepositForSale(Syscall):
    deposit: Entity
    caller_crew: Entity


@dataclass
class ActivateEmergency(Syscall):
    caller_crew: Entity


@dataclass
class CollectEmergencyPropellant(Syscall):
    caller_crew: Entity


@dataclass
class DeactivateEmergency(Syscall):
    caller_crew: Entity


@dataclass
class CreateSellOrder(Syscall):
    exchange: Entity
    product: int
    amount: int
    price: int
    storage: Entity
    storage_slot: int
    caller_crew: Entity


@dataclass
class FillSellOrder(Syscall):
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
class CancelSellOrder(Syscall):
    seller_crew: Entity
    exchange: Entity
    product: int
    price: int
    storage: Entity
    storage_slot: int
    caller_crew: Entity


@dataclass
class CreateBuyOrder(Syscall):
    exchange: Entity
    product: int
    amount: int
    price: int
    storage: Entity
    storage_slot: int
    caller_crew: Entity
    escrow_caller: ContractAddress ????
    escrow_type: int
    escrow_token: ContractAddress ????
    escrow_amount: int


@dataclass
class FillBuyOrder(Syscall):
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
    escrow_caller: ContractAddress ????
    escrow_type: int
    escrow_token: ContractAddress ????
    escrow_withdrawals: Span<Withdrawal> ????


@dataclass
class AssignContractPolicy(Syscall):
    target: Entity
    permission: int
    contract: ContractAddress ????
    caller_crew: Entity


@dataclass
class AssignPrepaidMerklePolicy(Syscall):
    target: Entity
    permission: int
    rate: int
    initial_term: int
    notice_period: int
    merkle_root: Felt | str ????
    caller_crew: Entity


@dataclass
class AssignPrepaidPolicy(Syscall):
    target: Entity
    permission: int
    rate: int
    initial_term: int
    notice_period: int
    caller_crew: Entity


@dataclass
class AssignPublicPolicy(Syscall):
    target: Entity
    permission: int
    caller_crew: Entity


@dataclass
class RemoveContractPolicy(Syscall):
    target: Entity
    permission: int
    caller_crew: Entity


@dataclass
class RemovePrepaidPolicy(Syscall):
    target: Entity
    permission: int
    caller_crew: Entity


@dataclass
class RemovePrepaidMerklePolicy(Syscall):
    target: Entity
    permission: int
    caller_crew: Entity


@dataclass
class RemovePublicPolicy(Syscall):
    target: Entity
    permission: int
    caller_crew: Entity


@dataclass
class AssembleShipFinish(Syscall):
    dry_dock: Entity
    dry_dock_slot: int
    destination: Entity
    caller_crew: Entity


@dataclass
class AssembleShipStart(Syscall):
    dry_dock: Entity
    dry_dock_slot: int
    ship_type: int
    origin: Entity
    origin_slot: int
    caller_crew: Entity


@dataclass
class ExtractResourceFinish(Syscall):
    extractor: Entity
    extractor_slot: int
    caller_crew: Entity


@dataclass
class ExtractResourceStart(Syscall):
    deposit: Entity
    yield_: int  # yield is a reserved keyword
    extractor: Entity
    extractor_slot: int
    destination: Entity
    destination_slot: int
    caller_crew: Entity


@dataclass
class ProcessProductsFinish(Syscall):
    processor: Entity
    processor_slot: int
    caller_crew: Entity


@dataclass
class ProcessProductsStart(Syscall):
    processor: Entity
    processor_slot: int
    process: int
    target_output: int
    recipes: CubitFixedFloat ????
    origin: Entity
    origin_slot: int
    destination: Entity
    destination_slot: int
    caller_crew: Entity


@dataclass
class ResolveRandomEvent(Syscall):
    choice: int
    caller_crew: Entity


@dataclass
class CheckForRandomEvent(Syscall):
    # TODO: this is a 'view' function, so it should not be a syscall
    caller_crew: Entity


@dataclass
class ClaimArrivalReward(Syscall):
    asteroid: Entity
    caller_crew: Entity


@dataclass
class ClaimPrepareForLaunchReward(Syscall):
    asteroid: Entity


@dataclass
class ClaimTestnetSway(Syscall):
    proof: Span<Felt> ????
    caller_crew: Entity


@dataclass
class PurchaseAdalian(Syscall):
    collection: int


@dataclass
class PurchaseAsteroid(Syscall):
    asteroid: Entity
    caller_crew: Entity


@dataclass
class ScanResourcesFinish(Syscall):
    asteroid: Entity
    caller_crew: Entity


@dataclass
class ScanResourcesStart(Syscall):
    asteroid: Entity
    caller_crew: Entity


@dataclass
class ScanSurfaceFinish(Syscall):
    asteroid: Entity
    caller_crew: Entity


@dataclass
class ScanSurfaceStart(Syscall):
    asteroid: Entity
    caller_crew: Entity


@dataclass
class InitializeAsteroid(Syscall):
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
    merkle_proof: Span<Felt> ????


@dataclass
class SeedAsteroids(Syscall):
    asteroids: Span<SeededAsteroid> ????


@dataclass
class SeedCrewmates(Syscall):
    crewmates: Span<SeededCrewmate> ????


# NOTE: This is according to the system ABI, but it seems to be incorrect or incomplete
@dataclass
class SeedColony(Syscall):
    colony: int
    building_type: int


# NOTE: This is according to the system ABI, but it seems to be incorrect or incomplete
@dataclass
class SeedHabitat(Syscall):
    pass


# NOTE: This is according to the system ABI, but it seems to be incorrect or incomplete
@dataclass
class SeedOrders(Syscall):
    market_lot: int
    warehouse_lot: int


@dataclass
class DockShip(Syscall):
    target: Entity
    powered: bool
    caller_crew: Entity


@dataclass
class TransitBetweenFinish(Syscall):
    caller_crew: Entity


@dataclass
class TransitBetweenStart(Syscall):
    origin: Entity
    destination: Entity
    departure_time: int
    arrival_time: int
    transit_p: CubitFixedFloat ????
    transit_ecc: CubitFixedFloat ????
    transit_inc: CubitFixedFloat ????
    transit_raan: CubitFixedFloat ????
    transit_argp: CubitFixedFloat ????
    transit_nu_start: CubitFixedFloat ????
    transit_nu_end: CubitFixedFloat ????
    caller_crew: Entity


@dataclass
class UndockShip(Syscall):
    ship: Entity
    powered: bool
    caller_crew: Entity


@dataclass
class AnnotateEvent(Syscall):
    transaction_hash: Felt ????
    log_index: int
    content_hash: Span<Felt> ????
    caller_crew: Entity


@dataclass
class ChangeName(Syscall):
    entity: Entity
    name: InfluenceString ????
    caller_crew: Entity


@dataclass
class ConfigureExchange(Syscall):
    exchange: Entity
    maker_fee: int
    taker_fee: int
    allowed_products: Span<int> ????
    caller_crew: Entity


@dataclass
class ReadComponent(Syscall):
    name: Felt ????
    path: Span<Felt> ????
    # TODO: output is of type Span<Felt>, declare this


@dataclass
class WriteComponent(Syscall):
    name: Felt ????
    path: Span<Felt> ????
    data: Span<Felt> ????
    # TODO: state_mutability is 'view' which doesn't make sense for a write operation

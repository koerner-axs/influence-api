from typing import List

from influencepy.starknet.net.constants import DISPATCHER_ADDRESS, DISPATCHER_RUN_SYSTEM_SELECTOR
from influencepy.starknet.net.contract_call import ContractCall
from influencepy.starknet.net.datatypes import ContractAddress, CubitFixedPoint64, CubitFixedPoint128, u256, felt252, \
    u64, shortstr, u128, Calldata
from influencepy.starknet.net.structs import Entity, InventoryItem, Withdrawal, SeededAsteroid, SeededCrewmate
from influencepy.starknet.util.contract import DispatcherContract


class SystemCall(ContractCall):
    _contract_address: int = DISPATCHER_ADDRESS
    _selector: int = DISPATCHER_RUN_SYSTEM_SELECTOR
    _function_name: str

    def to_calldata(self, calldata: Calldata = None) -> Calldata:
        if calldata is None:
            calldata = Calldata([])
        calldata.push_int(self.__class__._contract_address)
        calldata.push_int(self.__class__._selector)
        args_calldata = super(ContractCall, self).to_calldata(None)
        args_calldata.count_prepend_len()
        args_calldata.prepend_string(self.__class__._function_name)
        calldata.count_push_len_extend(args_calldata)
        return calldata

    @property
    def function_name(self):
        return self._function_name

    @property
    def contract_address(self):
        return self._contract_address

    @property
    def selector(self):
        return self._selector


class AcceptContractAgreement(SystemCall):
    _function_name: str = 'AcceptContractAgreement'
    target: Entity
    permission: u64
    permitted: Entity
    caller_crew: Entity


class AcceptPrepaidMerkleAgreement(SystemCall):
    _function_name: str = 'AcceptPrepaidMerkleAgreement'
    target: Entity
    permission: u64
    permitted: Entity
    term: u64
    merkle_proof: List[felt252]
    caller_crew: Entity


class AcceptPrepaidAgreement(SystemCall):
    _function_name: str = 'AcceptPrepaidAgreement'
    target: Entity
    permission: u64
    permitted: Entity
    term: u64
    caller_crew: Entity


class ExtendPrepaidAgreement(SystemCall):
    _function_name: str = 'ExtendPrepaidAgreement'
    target: Entity
    permission: u64
    permitted: Entity
    added_term: u64
    caller_crew: Entity


class CancelPrepaidAgreement(SystemCall):
    _function_name: str = 'CancelPrepaidAgreement'
    target: Entity
    permission: u64
    permitted: Entity
    caller_crew: Entity


class RemoveFromWhitelist(SystemCall):
    _function_name: str = 'RemoveFromWhitelist'
    target: Entity
    permission: u64
    permitted: Entity
    caller_crew: Entity


class RemoveAccountFromWhiteList(SystemCall):
    _function_name: str = 'RemoveAccountFromWhiteList'
    target: Entity
    permission: u64
    permitted: ContractAddress
    caller_crew: Entity


class Whitelist(SystemCall):
    _function_name: str = 'Whitelist'
    target: Entity
    permission: u64
    permitted: Entity
    caller_crew: Entity


class WhitelistAccount(SystemCall):
    _function_name: str = 'WhitelistAccount'
    target: Entity
    permission: u64
    permitted: ContractAddress
    caller_crew: Entity


class ConstructionAbandon(SystemCall):
    _function_name: str = 'ConstructionAbandon'
    building: Entity
    caller_crew: Entity


class ConstructionDeconstruct(SystemCall):
    _function_name: str = 'ConstructionDeconstruct'
    building: Entity
    caller_crew: Entity


class ConstructionFinish(SystemCall):
    _function_name: str = 'ConstructionFinish'
    building: Entity
    caller_crew: Entity


class ConstructionPlan(SystemCall):
    _function_name: str = 'ConstructionPlan'
    building_type: u64
    lot: Entity
    caller_crew: Entity


class ConstructionStart(SystemCall):
    _function_name: str = 'ConstructionStart'
    building: Entity
    caller_crew: Entity


class CommandeerShip(SystemCall):
    _function_name: str = 'CommandeerShip'
    ship: Entity
    caller_crew: Entity


class ManageAsteroid(SystemCall):
    _function_name: str = 'ManageAsteroid'
    asteroid: Entity
    caller_crew: Entity


class RepossessBuilding(SystemCall):
    _function_name: str = 'RepossessBuilding'
    building: Entity
    caller_crew: Entity


class ArrangeCrew(SystemCall):
    _function_name: str = 'ArrangeCrew'
    composition: List[u64]
    caller_crew: Entity


class DelegateCrew(SystemCall):
    _function_name: str = 'DelegateCrew'
    delegated_to: ContractAddress
    caller_crew: Entity


class EjectCrew(SystemCall):
    _function_name: str = 'EjectCrew'
    ejected_crew: Entity
    caller_crew: Entity


class ExchangeCrew(SystemCall):
    _function_name: str = 'ExchangeCrew'
    crew1: Entity
    comp1: List[u64]
    crew2: Entity  # ABI specifies a leading _
    comp2: List[u64]


class InitializeArvadian(SystemCall):
    _function_name: str = 'InitializeArvadian'
    crewmate: Entity
    impactful: List[u64]
    cosmetic: List[u64]
    name: shortstr
    station: Entity
    caller_crew: Entity


class RecruitAdalian(SystemCall):
    _function_name: str = 'RecruitAdalian'
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


class ResupplyFood(SystemCall):
    _function_name: str = 'ResupplyFood'
    origin: Entity
    origin_slot: u64
    food: u64
    caller_crew: Entity


class ResupplyFoodFromExchange(SystemCall):
    _function_name: str = 'ResupplyFoodFromExchange'
    seller_crew: Entity
    exchange: Entity
    amount: u64
    price: u64
    storage: Entity
    storage_slot: u64
    caller_crew: Entity


class StationCrew(SystemCall):
    _function_name: str = 'StationCrew'
    destination: Entity
    caller_crew: Entity


class AcceptDelivery(SystemCall):
    _function_name: str = 'AcceptDelivery'
    delivery: Entity
    caller_crew: Entity


class DumpDelivery(SystemCall):
    _function_name: str = 'DumpDelivery'
    origin: Entity
    origin_slot: u64
    products: List[InventoryItem]
    caller_crew: Entity


class CancelDelivery(SystemCall):
    _function_name: str = 'CancelDelivery'
    delivery: Entity
    caller_crew: Entity


class PackageDelivery(SystemCall):
    _function_name: str = 'PackageDelivery'
    origin: Entity
    origin_slot: u64
    products: List[InventoryItem]
    dest: Entity
    dest_slot: u64
    price: u64
    caller_crew: Entity


class ReceiveDelivery(SystemCall):
    _function_name: str = 'ReceiveDelivery'
    delivery: Entity
    caller_crew: Entity


class SendDelivery(SystemCall):
    _function_name: str = 'SendDelivery'
    origin: Entity
    origin_slot: u64
    products: List[InventoryItem]
    dest: Entity
    dest_slot: u64
    caller_crew: Entity


class SampleDepositStart(SystemCall):
    _function_name: str = 'SampleDepositStart'
    lot: Entity
    resource: u64
    origin: Entity
    origin_slot: u64
    caller_crew: Entity


class SampleDepositImprove(SystemCall):
    _function_name: str = 'SampleDepositImprove'
    deposit: Entity
    origin: Entity
    origin_slot: u64
    caller_crew: Entity


class SampleDepositFinish(SystemCall):
    _function_name: str = 'SampleDepositFinish'
    deposit: Entity
    caller_crew: Entity


class ListDepositForSale(SystemCall):
    _function_name: str = 'ListDepositForSale'
    deposit: Entity
    price: u64
    caller_crew: Entity


class PurchaseDeposit(SystemCall):
    _function_name: str = 'PurchaseDeposit'
    deposit: Entity
    caller_crew: Entity


class UnlistDepositForSale(SystemCall):
    _function_name: str = 'UnlistDepositForSale'
    deposit: Entity
    caller_crew: Entity


class ActivateEmergency(SystemCall):
    _function_name: str = 'ActivateEmergency'
    caller_crew: Entity


class CollectEmergencyPropellant(SystemCall):
    _function_name: str = 'CollectEmergencyPropellant'
    caller_crew: Entity


class DeactivateEmergency(SystemCall):
    _function_name: str = 'DeactivateEmergency'
    caller_crew: Entity


class CreateSellOrder(SystemCall):
    _function_name: str = 'CreateSellOrder'
    exchange: Entity
    product: u64
    amount: u64
    price: u64
    storage: Entity
    storage_slot: u64
    caller_crew: Entity


class FillSellOrder(SystemCall):
    _function_name: str = 'FillSellOrder'
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


class CancelSellOrder(SystemCall):
    _function_name: str = 'CancelSellOrder'
    seller_crew: Entity
    exchange: Entity
    product: u64
    price: u64
    storage: Entity
    storage_slot: u64
    caller_crew: Entity


class CreateBuyOrder(SystemCall):
    _function_name: str = 'CreateBuyOrder'
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


class FillBuyOrder(SystemCall):
    _function_name: str = 'FillBuyOrder'
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


class AssignContractPolicy(SystemCall):
    _function_name: str = 'AssignContractPolicy'
    target: Entity
    permission: u64
    contract: ContractAddress
    caller_crew: Entity


class AssignPrepaidMerklePolicy(SystemCall):
    _function_name: str = 'AssignPrepaidMerklePolicy'
    target: Entity
    permission: u64
    rate: u64
    initial_term: u64
    notice_period: u64
    merkle_root: felt252
    caller_crew: Entity


class AssignPrepaidPolicy(SystemCall):
    _function_name: str = 'AssignPrepaidPolicy'
    target: Entity
    permission: u64
    rate: u64
    initial_term: u64
    notice_period: u64
    caller_crew: Entity


class AssignPublicPolicy(SystemCall):
    _function_name: str = 'AssignPublicPolicy'
    target: Entity
    permission: u64
    caller_crew: Entity


class RemoveContractPolicy(SystemCall):
    _function_name: str = 'RemoveContractPolicy'
    target: Entity
    permission: u64
    caller_crew: Entity


class RemovePrepaidPolicy(SystemCall):
    _function_name: str = 'RemovePrepaidPolicy'
    target: Entity
    permission: u64
    caller_crew: Entity


class RemovePrepaidMerklePolicy(SystemCall):
    _function_name: str = 'RemovePrepaidMerklePolicy'
    target: Entity
    permission: u64
    caller_crew: Entity


class RemovePublicPolicy(SystemCall):
    _function_name: str = 'RemovePublicPolicy'
    target: Entity
    permission: u64
    caller_crew: Entity


class AssembleShipFinish(SystemCall):
    _function_name: str = 'AssembleShipFinish'
    dry_dock: Entity
    dry_dock_slot: u64
    destination: Entity
    caller_crew: Entity


class AssembleShipStart(SystemCall):
    _function_name: str = 'AssembleShipStart'
    dry_dock: Entity
    dry_dock_slot: u64
    ship_type: u64
    origin: Entity
    origin_slot: u64
    caller_crew: Entity


class ExtractResourceFinish(SystemCall):
    _function_name: str = 'ExtractResourceFinish'
    extractor: Entity
    extractor_slot: u64
    caller_crew: Entity


class ExtractResourceStart(SystemCall):
    _function_name: str = 'ExtractResourceStart'
    deposit: Entity
    yield_: u64  # yield is a reserved keyword
    extractor: Entity
    extractor_slot: u64
    destination: Entity
    destination_slot: u64
    caller_crew: Entity


class ProcessProductsFinish(SystemCall):
    _function_name: str = 'ProcessProductsFinish'
    processor: Entity
    processor_slot: u64
    caller_crew: Entity


class ProcessProductsStart(SystemCall):
    _function_name: str = 'ProcessProductsStart'
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


class ResolveRandomEvent(SystemCall):
    _function_name: str = 'ResolveRandomEvent'
    choice: u64
    caller_crew: Entity


class CheckForRandomEvent(SystemCall):
    _function_name: str = 'CheckForRandomEvent'
    caller_crew: Entity

    # TODO: output is of type u64, need to declare this somewhere?

    async def query(self, dispatcher: DispatcherContract) -> bool:
        result: List[int] = await dispatcher.run_system(self)
        print('CheckForRandomEvent result:', result)
        return result != 0


class ClaimArrivalReward(SystemCall):
    _function_name: str = 'ClaimArrivalReward'
    asteroid: Entity
    caller_crew: Entity


class ClaimPrepareForLaunchReward(SystemCall):
    _function_name: str = 'ClaimPrepareForLaunchReward'
    asteroid: Entity


class ClaimTestnetSway(SystemCall):
    _function_name: str = 'ClaimTestnetSway'
    proof: List[felt252]
    amount: u256


class PurchaseAdalian(SystemCall):
    _function_name: str = 'PurchaseAdalian'
    collection: u64


class PurchaseAsteroid(SystemCall):
    _function_name: str = 'PurchaseAsteroid'
    asteroid: Entity
    caller_crew: Entity


class ScanResourcesFinish(SystemCall):
    _function_name: str = 'ScanResourcesFinish'
    asteroid: Entity
    caller_crew: Entity


class ScanResourcesStart(SystemCall):
    _function_name: str = 'ScanResourcesStart'
    asteroid: Entity
    caller_crew: Entity


class ScanSurfaceFinish(SystemCall):
    _function_name: str = 'ScanSurfaceFinish'
    asteroid: Entity
    caller_crew: Entity


class ScanSurfaceStart(SystemCall):
    _function_name: str = 'ScanSurfaceStart'
    asteroid: Entity
    caller_crew: Entity


class InitializeAsteroid(SystemCall):
    _function_name: str = 'InitializeAsteroid'
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


class SeedAsteroids(SystemCall):
    _function_name: str = 'SeedAsteroids'
    asteroids: List[SeededAsteroid]


class SeedCrewmates(SystemCall):
    _function_name: str = 'SeedCrewmates'
    crewmates: List[SeededCrewmate]


# NOTE: This is according to the system ABI, but it seems to be incorrect or incomplete

class SeedColony(SystemCall):
    _function_name: str = 'SeedColony'
    colony: u64
    building_type: u64


# NOTE: This is according to the system ABI, but it seems to be incorrect or incomplete

class SeedHabitat(SystemCall):
    _function_name: str = 'SeedHabitat'
    pass


# NOTE: This is according to the system ABI, but it seems to be incorrect or incomplete

class SeedOrders(SystemCall):
    _function_name: str = 'SeedOrders'
    market_lot: u64
    warehouse_lot: u64


class DockShip(SystemCall):
    _function_name: str = 'DockShip'
    target: Entity
    powered: bool
    caller_crew: Entity


class TransitBetweenFinish(SystemCall):
    _function_name: str = 'TransitBetweenFinish'
    caller_crew: Entity


class TransitBetweenStart(SystemCall):
    _function_name: str = 'TransitBetweenStart'
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


class UndockShip(SystemCall):
    _function_name: str = 'UndockShip'
    ship: Entity
    powered: bool
    caller_crew: Entity


class AnnotateEvent(SystemCall):
    _function_name: str = 'AnnotateEvent'
    transaction_hash: felt252
    log_index: u64
    content_hash: List[felt252]
    caller_crew: Entity


class ChangeName(SystemCall):
    _function_name: str = 'ChangeName'
    entity: Entity
    name: shortstr
    caller_crew: Entity


class ConfigureExchange(SystemCall):
    _function_name: str = 'ConfigureExchange'
    exchange: Entity
    maker_fee: u64
    taker_fee: u64
    allowed_products: List[u64]
    caller_crew: Entity


class ReadComponent(SystemCall):
    _function_name: str = 'ReadComponent'
    name: felt252  # TODO: could also be a shortstr
    path: List[felt252]
    # TODO: output is of type Span<felt252>, need to declare this somewhere?


class WriteComponent(SystemCall):
    _function_name: str = 'WriteComponent'
    name: felt252  # TODO: could also be a shortstr
    path: List[felt252]
    data: List[felt252]
    # TODO: state_mutability is 'view' which doesn't make sense for a write operation

from typing import List
from dataclasses import dataclass

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


@dataclass
class AcceptContractAgreement(SystemCall):
    target: Entity
    permission: u64
    permitted: Entity
    caller_crew: Entity
    _function_name: str = 'AcceptContractAgreement'


@dataclass
class AcceptPrepaidMerkleAgreement(SystemCall):
    target: Entity
    permission: u64
    permitted: Entity
    term: u64
    merkle_proof: List[felt252]
    caller_crew: Entity
    _function_name: str = 'AcceptPrepaidMerkleAgreement'


@dataclass
class AcceptPrepaidAgreement(SystemCall):
    target: Entity
    permission: u64
    permitted: Entity
    term: u64
    caller_crew: Entity
    _function_name: str = 'AcceptPrepaidAgreement'


@dataclass
class ExtendPrepaidAgreement(SystemCall):
    target: Entity
    permission: u64
    permitted: Entity
    added_term: u64
    caller_crew: Entity
    _function_name: str = 'ExtendPrepaidAgreement'


@dataclass
class CancelPrepaidAgreement(SystemCall):
    target: Entity
    permission: u64
    permitted: Entity
    caller_crew: Entity
    _function_name: str = 'CancelPrepaidAgreement'


@dataclass
class RemoveFromWhitelist(SystemCall):
    target: Entity
    permission: u64
    permitted: Entity
    caller_crew: Entity
    _function_name: str = 'RemoveFromWhitelist'


@dataclass
class RemoveAccountFromWhiteList(SystemCall):
    target: Entity
    permission: u64
    permitted: ContractAddress
    caller_crew: Entity
    _function_name: str = 'RemoveAccountFromWhiteList'


@dataclass
class Whitelist(SystemCall):
    target: Entity
    permission: u64
    permitted: Entity
    caller_crew: Entity
    _function_name: str = 'Whitelist'


@dataclass
class WhitelistAccount(SystemCall):
    target: Entity
    permission: u64
    permitted: ContractAddress
    caller_crew: Entity
    _function_name: str = 'WhitelistAccount'


@dataclass
class ConstructionAbandon(SystemCall):
    building: Entity
    caller_crew: Entity
    _function_name: str = 'ConstructionAbandon'


@dataclass
class ConstructionDeconstruct(SystemCall):
    building: Entity
    caller_crew: Entity
    _function_name: str = 'ConstructionDeconstruct'


@dataclass
class ConstructionFinish(SystemCall):
    building: Entity
    caller_crew: Entity
    _function_name: str = 'ConstructionFinish'


@dataclass
class ConstructionPlan(SystemCall):
    building_type: u64
    lot: Entity
    caller_crew: Entity
    _function_name: str = 'ConstructionPlan'


@dataclass
class ConstructionStart(SystemCall):
    building: Entity
    caller_crew: Entity
    _function_name: str = 'ConstructionStart'


@dataclass
class CommandeerShip(SystemCall):
    ship: Entity
    caller_crew: Entity
    _function_name: str = 'CommandeerShip'


@dataclass
class ManageAsteroid(SystemCall):
    asteroid: Entity
    caller_crew: Entity
    _function_name: str = 'ManageAsteroid'


@dataclass
class RepossessBuilding(SystemCall):
    building: Entity
    caller_crew: Entity
    _function_name: str = 'RepossessBuilding'


@dataclass
class ArrangeCrew(SystemCall):
    composition: List[u64]
    caller_crew: Entity
    _function_name: str = 'ArrangeCrew'


@dataclass
class DelegateCrew(SystemCall):
    delegated_to: ContractAddress
    caller_crew: Entity
    _function_name: str = 'DelegateCrew'


@dataclass
class EjectCrew(SystemCall):
    ejected_crew: Entity
    caller_crew: Entity
    _function_name: str = 'EjectCrew'


@dataclass
class ExchangeCrew(SystemCall):
    crew1: Entity
    comp1: List[u64]
    crew2: Entity  # ABI specifies a leading _
    comp2: List[u64]
    _function_name: str = 'ExchangeCrew'


@dataclass
class InitializeArvadian(SystemCall):
    crewmate: Entity
    impactful: List[u64]
    cosmetic: List[u64]
    name: shortstr
    station: Entity
    caller_crew: Entity
    _function_name: str = 'InitializeArvadian'


@dataclass
class RecruitAdalian(SystemCall):
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
    _function_name: str = 'RecruitAdalian'


@dataclass
class ResupplyFood(SystemCall):
    origin: Entity
    origin_slot: u64
    food: u64
    caller_crew: Entity
    _function_name: str = 'ResupplyFood'


@dataclass
class ResupplyFoodFromExchange(SystemCall):
    seller_crew: Entity
    exchange: Entity
    amount: u64
    price: u64
    storage: Entity
    storage_slot: u64
    caller_crew: Entity
    _function_name: str = 'ResupplyFoodFromExchange'


@dataclass
class StationCrew(SystemCall):
    destination: Entity
    caller_crew: Entity
    _function_name: str = 'StationCrew'


@dataclass
class AcceptDelivery(SystemCall):
    delivery: Entity
    caller_crew: Entity
    _function_name: str = 'AcceptDelivery'


@dataclass
class DumpDelivery(SystemCall):
    origin: Entity
    origin_slot: u64
    products: List[InventoryItem]
    caller_crew: Entity
    _function_name: str = 'DumpDelivery'


@dataclass
class CancelDelivery(SystemCall):
    delivery: Entity
    caller_crew: Entity
    _function_name: str = 'CancelDelivery'


@dataclass
class PackageDelivery(SystemCall):
    origin: Entity
    origin_slot: u64
    products: List[InventoryItem]
    dest: Entity
    dest_slot: u64
    price: u64
    caller_crew: Entity
    _function_name: str = 'PackageDelivery'


@dataclass
class ReceiveDelivery(SystemCall):
    delivery: Entity
    caller_crew: Entity
    _function_name: str = 'ReceiveDelivery'


@dataclass
class SendDelivery(SystemCall):
    origin: Entity
    origin_slot: u64
    products: List[InventoryItem]
    dest: Entity
    dest_slot: u64
    caller_crew: Entity
    _function_name: str = 'SendDelivery'


@dataclass
class SampleDepositStart(SystemCall):
    lot: Entity
    resource: u64
    origin: Entity
    origin_slot: u64
    caller_crew: Entity
    _function_name: str = 'SampleDepositStart'


@dataclass
class SampleDepositImprove(SystemCall):
    deposit: Entity
    origin: Entity
    origin_slot: u64
    caller_crew: Entity
    _function_name: str = 'SampleDepositImprove'


@dataclass
class SampleDepositFinish(SystemCall):
    deposit: Entity
    caller_crew: Entity
    _function_name: str = 'SampleDepositFinish'


@dataclass
class ListDepositForSale(SystemCall):
    deposit: Entity
    price: u64
    caller_crew: Entity
    _function_name: str = 'ListDepositForSale'


@dataclass
class PurchaseDeposit(SystemCall):
    deposit: Entity
    caller_crew: Entity
    _function_name: str = 'PurchaseDeposit'


@dataclass
class UnlistDepositForSale(SystemCall):
    deposit: Entity
    caller_crew: Entity
    _function_name: str = 'UnlistDepositForSale'


@dataclass
class ActivateEmergency(SystemCall):
    caller_crew: Entity
    _function_name: str = 'ActivateEmergency'


@dataclass
class CollectEmergencyPropellant(SystemCall):
    caller_crew: Entity
    _function_name: str = 'CollectEmergencyPropellant'


@dataclass
class DeactivateEmergency(SystemCall):
    caller_crew: Entity
    _function_name: str = 'DeactivateEmergency'


@dataclass
class CreateSellOrder(SystemCall):
    exchange: Entity
    product: u64
    amount: u64
    price: u64
    storage: Entity
    storage_slot: u64
    caller_crew: Entity
    _function_name: str = 'CreateSellOrder'


@dataclass
class FillSellOrder(SystemCall):
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
    _function_name: str = 'FillSellOrder'


@dataclass
class CancelSellOrder(SystemCall):
    seller_crew: Entity
    exchange: Entity
    product: u64
    price: u64
    storage: Entity
    storage_slot: u64
    caller_crew: Entity
    _function_name: str = 'CancelSellOrder'


@dataclass
class CreateBuyOrder(SystemCall):
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
    _function_name: str = 'CreateBuyOrder'


@dataclass
class FillBuyOrder(SystemCall):
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
    _function_name: str = 'FillBuyOrder'


@dataclass
class AssignContractPolicy(SystemCall):
    target: Entity
    permission: u64
    contract: ContractAddress
    caller_crew: Entity
    _function_name: str = 'AssignContractPolicy'


@dataclass
class AssignPrepaidMerklePolicy(SystemCall):
    target: Entity
    permission: u64
    rate: u64
    initial_term: u64
    notice_period: u64
    merkle_root: felt252
    caller_crew: Entity
    _function_name: str = 'AssignPrepaidMerklePolicy'


@dataclass
class AssignPrepaidPolicy(SystemCall):
    target: Entity
    permission: u64
    rate: u64
    initial_term: u64
    notice_period: u64
    caller_crew: Entity
    _function_name: str = 'AssignPrepaidPolicy'


@dataclass
class AssignPublicPolicy(SystemCall):
    target: Entity
    permission: u64
    caller_crew: Entity
    _function_name: str = 'AssignPublicPolicy'


@dataclass
class RemoveContractPolicy(SystemCall):
    target: Entity
    permission: u64
    caller_crew: Entity
    _function_name: str = 'RemoveContractPolicy'


@dataclass
class RemovePrepaidPolicy(SystemCall):
    target: Entity
    permission: u64
    caller_crew: Entity
    _function_name: str = 'RemovePrepaidPolicy'


@dataclass
class RemovePrepaidMerklePolicy(SystemCall):
    target: Entity
    permission: u64
    caller_crew: Entity
    _function_name: str = 'RemovePrepaidMerklePolicy'


@dataclass
class RemovePublicPolicy(SystemCall):
    target: Entity
    permission: u64
    caller_crew: Entity
    _function_name: str = 'RemovePublicPolicy'


@dataclass
class AssembleShipFinish(SystemCall):
    dry_dock: Entity
    dry_dock_slot: u64
    destination: Entity
    caller_crew: Entity
    _function_name: str = 'AssembleShipFinish'


@dataclass
class AssembleShipStart(SystemCall):
    dry_dock: Entity
    dry_dock_slot: u64
    ship_type: u64
    origin: Entity
    origin_slot: u64
    caller_crew: Entity
    _function_name: str = 'AssembleShipStart'


@dataclass
class ExtractResourceFinish(SystemCall):
    extractor: Entity
    extractor_slot: u64
    caller_crew: Entity
    _function_name: str = 'ExtractResourceFinish'


@dataclass
class ExtractResourceStart(SystemCall):
    deposit: Entity
    yield_: u64  # yield is a reserved keyword
    extractor: Entity
    extractor_slot: u64
    destination: Entity
    destination_slot: u64
    caller_crew: Entity
    _function_name: str = 'ExtractResourceStart'


@dataclass
class ProcessProductsFinish(SystemCall):
    processor: Entity
    processor_slot: u64
    caller_crew: Entity
    _function_name: str = 'ProcessProductsFinish'


@dataclass
class ProcessProductsStart(SystemCall):
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
    _function_name: str = 'ProcessProductsStart'


@dataclass
class ResolveRandomEvent(SystemCall):
    choice: u64
    caller_crew: Entity
    _function_name: str = 'ResolveRandomEvent'


@dataclass
class CheckForRandomEvent(SystemCall):
    caller_crew: Entity
    _function_name: str = 'CheckForRandomEvent'

    # TODO: output is of type u64, need to declare this somewhere?

    # TODO: should this be in here, should this be completely removed from the system?
    async def query(self, dispatcher: DispatcherContract) -> bool:
        result: List[int] = await dispatcher.run_system(self)
        print('CheckForRandomEvent result:', result)
        return result != 0


@dataclass
class ClaimArrivalReward(SystemCall):
    asteroid: Entity
    caller_crew: Entity
    _function_name: str = 'ClaimArrivalReward'


@dataclass
class ClaimPrepareForLaunchReward(SystemCall):
    asteroid: Entity
    _function_name: str = 'ClaimPrepareForLaunchReward'


@dataclass
class ClaimTestnetSway(SystemCall):
    proof: List[felt252]
    amount: u256
    _function_name: str = 'ClaimTestnetSway'


@dataclass
class PurchaseAdalian(SystemCall):
    collection: u64
    _function_name: str = 'PurchaseAdalian'


@dataclass
class PurchaseAsteroid(SystemCall):
    asteroid: Entity
    caller_crew: Entity
    _function_name: str = 'PurchaseAsteroid'


@dataclass
class ScanResourcesFinish(SystemCall):
    asteroid: Entity
    caller_crew: Entity
    _function_name: str = 'ScanResourcesFinish'


@dataclass
class ScanResourcesStart(SystemCall):
    asteroid: Entity
    caller_crew: Entity
    _function_name: str = 'ScanResourcesStart'


@dataclass
class ScanSurfaceFinish(SystemCall):
    asteroid: Entity
    caller_crew: Entity
    _function_name: str = 'ScanSurfaceFinish'


@dataclass
class ScanSurfaceStart(SystemCall):
    asteroid: Entity
    caller_crew: Entity
    _function_name: str = 'ScanSurfaceStart'


@dataclass
class InitializeAsteroid(SystemCall):
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
    _function_name: str = 'InitializeAsteroid'


@dataclass
class SeedAsteroids(SystemCall):
    asteroids: List[SeededAsteroid]
    _function_name: str = 'SeedAsteroids'


@dataclass
class SeedCrewmates(SystemCall):
    crewmates: List[SeededCrewmate]
    _function_name: str = 'SeedCrewmates'


# NOTE: This is according to the system ABI, but it seems to be incorrect or incomplete

@dataclass
class SeedColony(SystemCall):
    colony: u64
    building_type: u64
    _function_name: str = 'SeedColony'


# NOTE: This is according to the system ABI, but it seems to be incorrect or incomplete

@dataclass
class SeedHabitat(SystemCall):
    _function_name: str = 'SeedHabitat'


# NOTE: This is according to the system ABI, but it seems to be incorrect or incomplete

@dataclass
class SeedOrders(SystemCall):
    market_lot: u64
    warehouse_lot: u64
    _function_name: str = 'SeedOrders'


@dataclass
class DockShip(SystemCall):
    target: Entity
    powered: bool
    caller_crew: Entity
    _function_name: str = 'DockShip'


@dataclass
class TransitBetweenFinish(SystemCall):
    caller_crew: Entity
    _function_name: str = 'TransitBetweenFinish'


@dataclass
class TransitBetweenStart(SystemCall):
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
    _function_name: str = 'TransitBetweenStart'


@dataclass
class UndockShip(SystemCall):
    ship: Entity
    powered: bool
    caller_crew: Entity
    _function_name: str = 'UndockShip'


@dataclass
class AnnotateEvent(SystemCall):
    transaction_hash: felt252
    log_index: u64
    content_hash: List[felt252]
    caller_crew: Entity
    _function_name: str = 'AnnotateEvent'


@dataclass
class ChangeName(SystemCall):
    entity: Entity
    name: shortstr
    caller_crew: Entity
    _function_name: str = 'ChangeName'


@dataclass
class ConfigureExchange(SystemCall):
    exchange: Entity
    maker_fee: u64
    taker_fee: u64
    allowed_products: List[u64]
    caller_crew: Entity
    _function_name: str = 'ConfigureExchange'


@dataclass
class ReadComponent(SystemCall):
    name: felt252  # TODO: could also be a shortstr
    path: List[felt252]
    _function_name: str = 'ReadComponent'
    # TODO: output is of type Span<felt252>, need to declare this somewhere?


@dataclass
class WriteComponent(SystemCall):
    name: felt252  # TODO: could also be a shortstr
    path: List[felt252]
    data: List[felt252]
    _function_name: str = 'WriteComponent'
    # TODO: state_mutability is 'view' which doesn't make sense for a write operation


class UnknownSystemCall(SystemCall):
    def __init__(self, calldata: List[int], function_name: str):
        self.calldata = calldata
        self.function_name = function_name

    @classmethod
    def from_calldata(cls, calldata: Calldata, **kwargs) -> "UnknownSystemCall":
        """ Pops the argument length and all arguments from the calldata and stores it.
        No further parsing is done. """
        data = []
        for _ in range(kwargs['arg_count']):
            data.append(calldata.pop_int())
        return UnknownSystemCall(calldata=data, function_name=kwargs['function_name'])

    def __repr__(self):
        return f'UnknownSystemCall(function_name={self.function_name}, calldata={self.calldata})'

from dataclasses import dataclass  # noqa: F401
from typing import List, Dict  # noqa: F401

from starknet_py.hash.selector import get_selector_from_name
from starknet_py.net.client_models import Call

from influencepy.starknet.net.constants import DISPATCHER_ADDRESS
from influencepy.starknet.net.contract_call import ContractCall
from influencepy.starknet.net.datatypes import *
from influencepy.starknet.net.structs import *
from influencepy.starknet.util.contract import DispatcherContract  # noqa: F401


class RunSystem(ContractCall):
    _contract_address: int = DISPATCHER_ADDRESS  # TODO: maybe remove
    _selector: int = get_selector_from_name('run_system')  # TODO: maybe remove
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

    def to_call(self) -> Call:
        calldata = Calldata([])
        calldata.push_string(self.__class__._function_name)
        calldata.count_push_len_extend(self._to_callargs())
        return Call(
            to_addr=self.__class__._contract_address,
            selector=self.__class__._selector,
            calldata=calldata.data
        )


@dataclass
class AcceptContractAgreement(RunSystem):
    target: Entity
    permission: u64
    permitted: Entity
    caller_crew: Entity
    _function_name: str = 'AcceptContractAgreement'


@dataclass
class AcceptDelivery(RunSystem):
    delivery: Entity
    caller_crew: Entity
    _function_name: str = 'AcceptDelivery'


@dataclass
class AcceptPrepaidAgreement(RunSystem):
    target: Entity
    permission: u64
    permitted: Entity
    term: u64
    caller_crew: Entity
    _function_name: str = 'AcceptPrepaidAgreement'


@dataclass
class AcceptPrepaidMerkleAgreement(RunSystem):
    target: Entity
    permission: u64
    permitted: Entity
    term: u64
    merkle_proof: List[felt252]
    caller_crew: Entity
    _function_name: str = 'AcceptPrepaidMerkleAgreement'


@dataclass
class ActivateEmergency(RunSystem):
    caller_crew: Entity
    _function_name: str = 'ActivateEmergency'


@dataclass
class AnnotateEvent(RunSystem):
    transaction_hash: felt252
    log_index: u64
    content_hash: List[felt252]
    caller_crew: Entity
    _function_name: str = 'AnnotateEvent'


@dataclass
class ArrangeCrew(RunSystem):
    composition: List[u64]
    caller_crew: Entity
    _function_name: str = 'ArrangeCrew'


@dataclass
class AssembleShipFinish(RunSystem):
    dry_dock: Entity
    dry_dock_slot: u64
    destination: Entity
    caller_crew: Entity
    _function_name: str = 'AssembleShipFinish'


@dataclass
class AssembleShipStart(RunSystem):
    dry_dock: Entity
    dry_dock_slot: u64
    ship_type: u64
    origin: Entity
    origin_slot: u64
    caller_crew: Entity
    _function_name: str = 'AssembleShipStart'


@dataclass
class AssignContractPolicy(RunSystem):
    target: Entity
    permission: u64
    contract: ContractAddress
    caller_crew: Entity
    _function_name: str = 'AssignContractPolicy'


@dataclass
class AssignPrepaidMerklePolicy(RunSystem):
    target: Entity
    permission: u64
    rate: u64
    initial_term: u64
    notice_period: u64
    merkle_root: felt252
    caller_crew: Entity
    _function_name: str = 'AssignPrepaidMerklePolicy'


@dataclass
class AssignPrepaidPolicy(RunSystem):
    target: Entity
    permission: u64
    rate: u64
    initial_term: u64
    notice_period: u64
    caller_crew: Entity
    _function_name: str = 'AssignPrepaidPolicy'


@dataclass
class AssignPublicPolicy(RunSystem):
    target: Entity
    permission: u64
    caller_crew: Entity
    _function_name: str = 'AssignPublicPolicy'


@dataclass
class CancelDelivery(RunSystem):
    delivery: Entity
    caller_crew: Entity
    _function_name: str = 'CancelDelivery'


@dataclass
class CancelPrepaidAgreement(RunSystem):
    target: Entity
    permission: u64
    permitted: Entity
    caller_crew: Entity
    _function_name: str = 'CancelPrepaidAgreement'


@dataclass
class CancelSellOrder(RunSystem):
    seller_crew: Entity
    exchange: Entity
    product: u64
    price: u64
    storage: Entity
    storage_slot: u64
    caller_crew: Entity
    _function_name: str = 'CancelSellOrder'


@dataclass
class ChangeName(RunSystem):
    entity: Entity
    name: longstr
    caller_crew: Entity
    _function_name: str = 'ChangeName'


@dataclass
class CheckForRandomEvent(RunSystem):
    caller_crew: Entity
    _function_name: str = 'CheckForRandomEvent'
    # TODO: output is of type u64, need to declare this somewhere?

    # TODO: should this be in here, should this be completely removed from the system?
    async def query(self, dispatcher: DispatcherContract) -> bool:
        result: List[int] = await dispatcher.run_system(self)
        print('CheckForRandomEvent result:', result)
        if len(result) != 2 or result[0] != 1:
            raise ValueError('CheckForRandomEvent result should have length 2')
        flag = result[1]
        return flag != 0


@dataclass
class ClaimArrivalReward(RunSystem):
    asteroid: Entity
    caller_crew: Entity
    _function_name: str = 'ClaimArrivalReward'


@dataclass
class ClaimPrepareForLaunchReward(RunSystem):
    asteroid: Entity
    _function_name: str = 'ClaimPrepareForLaunchReward'


@dataclass
class ClaimTestnetSway(RunSystem):
    proof: List[felt252]
    amount: u256
    _function_name: str = 'ClaimTestnetSway'


@dataclass
class CollectEmergencyPropellant(RunSystem):
    caller_crew: Entity
    _function_name: str = 'CollectEmergencyPropellant'


@dataclass
class CommandeerShip(RunSystem):
    ship: Entity
    caller_crew: Entity
    _function_name: str = 'CommandeerShip'


@dataclass
class ConfigureExchange(RunSystem):
    exchange: Entity
    maker_fee: u64
    taker_fee: u64
    allowed_products: List[u64]
    caller_crew: Entity
    _function_name: str = 'ConfigureExchange'


@dataclass
class ConstructionAbandon(RunSystem):
    building: Entity
    caller_crew: Entity
    _function_name: str = 'ConstructionAbandon'


@dataclass
class ConstructionDeconstruct(RunSystem):
    building: Entity
    caller_crew: Entity
    _function_name: str = 'ConstructionDeconstruct'


@dataclass
class ConstructionFinish(RunSystem):
    building: Entity
    caller_crew: Entity
    _function_name: str = 'ConstructionFinish'


@dataclass
class ConstructionPlan(RunSystem):
    building_type: u64
    lot: Entity
    caller_crew: Entity
    _function_name: str = 'ConstructionPlan'


@dataclass
class ConstructionStart(RunSystem):
    building: Entity
    caller_crew: Entity
    _function_name: str = 'ConstructionStart'


@dataclass
class CreateBuyOrder(RunSystem):
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
class CreateSellOrder(RunSystem):
    exchange: Entity
    product: u64
    amount: u64
    price: u64
    storage: Entity
    storage_slot: u64
    caller_crew: Entity
    _function_name: str = 'CreateSellOrder'


@dataclass
class DeactivateEmergency(RunSystem):
    caller_crew: Entity
    _function_name: str = 'DeactivateEmergency'


@dataclass
class DelegateCrew(RunSystem):
    delegated_to: ContractAddress
    caller_crew: Entity
    _function_name: str = 'DelegateCrew'


@dataclass
class DirectMessage(RunSystem):
    recipient: ContractAddress
    content_hash: List[felt252]
    _function_name: str = 'DirectMessage'


@dataclass
class DockShip(RunSystem):
    target: Entity
    powered: Bool
    caller_crew: Entity
    _function_name: str = 'DockShip'


@dataclass
class DumpDelivery(RunSystem):
    origin: Entity
    origin_slot: u64
    products: List[InventoryItem]
    caller_crew: Entity
    _function_name: str = 'DumpDelivery'


@dataclass
class EjectCrew(RunSystem):
    ejected_crew: Entity
    caller_crew: Entity
    _function_name: str = 'EjectCrew'


@dataclass
class ExchangeCrew(RunSystem):
    crew1: Entity
    comp1: List[u64]
    crew2: Entity
    comp2: List[u64]
    _function_name: str = 'ExchangeCrew'


@dataclass
class ExtendPrepaidAgreement(RunSystem):
    target: Entity
    permission: u64
    permitted: Entity
    added_term: u64
    caller_crew: Entity
    _function_name: str = 'ExtendPrepaidAgreement'


@dataclass
class ExtractResourceFinish(RunSystem):
    extractor: Entity
    extractor_slot: u64
    caller_crew: Entity
    _function_name: str = 'ExtractResourceFinish'


@dataclass
class ExtractResourceStart(RunSystem):
    deposit: Entity
    yield_: u64
    extractor: Entity
    extractor_slot: u64
    destination: Entity
    destination_slot: u64
    caller_crew: Entity
    _function_name: str = 'ExtractResourceStart'


@dataclass
class FillBuyOrder(RunSystem):
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
class FillSellOrder(RunSystem):
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
class GrantAdalians(RunSystem):
    recipient: ContractAddress
    count: u64
    _function_name: str = 'GrantAdalians'


@dataclass
class GrantStarterPack(RunSystem):
    recipient: ContractAddress
    crewmates: u64
    tokens: u64
    _function_name: str = 'GrantStarterPack'


@dataclass
class InitializeArvadian(RunSystem):
    crewmate: Entity
    impactful: List[u64]
    cosmetic: List[u64]
    name: felt252
    station: Entity
    caller_crew: Entity
    _function_name: str = 'InitializeArvadian'


@dataclass
class InitializeAsteroid(RunSystem):
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
class ListDepositForSale(RunSystem):
    deposit: Entity
    price: u64
    caller_crew: Entity
    _function_name: str = 'ListDepositForSale'


@dataclass
class ManageAsteroid(RunSystem):
    asteroid: Entity
    caller_crew: Entity
    _function_name: str = 'ManageAsteroid'


@dataclass
class PackageDelivery(RunSystem):
    origin: Entity
    origin_slot: u64
    products: List[InventoryItem]
    dest: Entity
    dest_slot: u64
    price: u64
    caller_crew: Entity
    _function_name: str = 'PackageDelivery'


@dataclass
class ProcessProductsFinish(RunSystem):
    processor: Entity
    processor_slot: u64
    caller_crew: Entity
    _function_name: str = 'ProcessProductsFinish'


@dataclass
class ProcessProductsStart(RunSystem):
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
class PurchaseAdalian(RunSystem):
    collection: u64
    _function_name: str = 'PurchaseAdalian'


@dataclass
class PurchaseAsteroid(RunSystem):
    asteroid: Entity
    caller_crew: Entity
    _function_name: str = 'PurchaseAsteroid'


@dataclass
class PurchaseDeposit(RunSystem):
    deposit: Entity
    caller_crew: Entity
    _function_name: str = 'PurchaseDeposit'


@dataclass
class ReadComponent(RunSystem):
    name: felt252
    path: List[felt252]
    _function_name: str = 'ReadComponent'


@dataclass
class ReceiveDelivery(RunSystem):
    delivery: Entity
    caller_crew: Entity
    _function_name: str = 'ReceiveDelivery'


@dataclass
class RecruitAdalian(RunSystem):
    crewmate: Entity
    class_: u64
    impactful: List[u64]
    cosmetic: List[u64]
    gender: u64
    body: u64
    face: u64
    hair: u64
    hair_color: u64
    clothes: u64
    name: felt252
    station: Entity
    caller_crew: Entity
    _function_name: str = 'RecruitAdalian'


@dataclass
class RekeyInbox(RunSystem):
    messaging_key_x: u256
    messaging_key_y: u256
    _function_name: str = 'RekeyInbox'


@dataclass
class RemoveAccountFromWhitelist(RunSystem):
    target: Entity
    permission: u64
    permitted: ContractAddress
    caller_crew: Entity
    _function_name: str = 'RemoveAccountFromWhitelist'


@dataclass
class RemoveContractPolicy(RunSystem):
    target: Entity
    permission: u64
    caller_crew: Entity
    _function_name: str = 'RemoveContractPolicy'


@dataclass
class RemoveFromWhitelist(RunSystem):
    target: Entity
    permission: u64
    permitted: Entity
    caller_crew: Entity
    _function_name: str = 'RemoveFromWhitelist'


@dataclass
class RemovePrepaidMerklePolicy(RunSystem):
    target: Entity
    permission: u64
    caller_crew: Entity
    _function_name: str = 'RemovePrepaidMerklePolicy'


@dataclass
class RemovePrepaidPolicy(RunSystem):
    target: Entity
    permission: u64
    caller_crew: Entity
    _function_name: str = 'RemovePrepaidPolicy'


@dataclass
class RemovePublicPolicy(RunSystem):
    target: Entity
    permission: u64
    caller_crew: Entity
    _function_name: str = 'RemovePublicPolicy'


@dataclass
class RepossessBuilding(RunSystem):
    building: Entity
    caller_crew: Entity
    _function_name: str = 'RepossessBuilding'


@dataclass
class ResolveRandomEvent(RunSystem):
    choice: u64
    caller_crew: Entity
    _function_name: str = 'ResolveRandomEvent'


@dataclass
class ResupplyFood(RunSystem):
    origin: Entity
    origin_slot: u64
    food: u64
    caller_crew: Entity
    _function_name: str = 'ResupplyFood'


@dataclass
class ResupplyFoodFromExchange(RunSystem):
    seller_crew: Entity
    exchange: Entity
    amount: u64
    price: u64
    storage: Entity
    storage_slot: u64
    caller_crew: Entity
    _function_name: str = 'ResupplyFoodFromExchange'


@dataclass
class SampleDepositFinish(RunSystem):
    deposit: Entity
    caller_crew: Entity
    _function_name: str = 'SampleDepositFinish'


@dataclass
class SampleDepositImprove(RunSystem):
    deposit: Entity
    origin: Entity
    origin_slot: u64
    caller_crew: Entity
    _function_name: str = 'SampleDepositImprove'


@dataclass
class SampleDepositStart(RunSystem):
    lot: Entity
    resource: u64
    origin: Entity
    origin_slot: u64
    caller_crew: Entity
    _function_name: str = 'SampleDepositStart'


@dataclass
class ScanResourcesFinish(RunSystem):
    asteroid: Entity
    caller_crew: Entity
    _function_name: str = 'ScanResourcesFinish'


@dataclass
class ScanResourcesStart(RunSystem):
    asteroid: Entity
    caller_crew: Entity
    _function_name: str = 'ScanResourcesStart'


@dataclass
class ScanSurfaceFinish(RunSystem):
    asteroid: Entity
    caller_crew: Entity
    _function_name: str = 'ScanSurfaceFinish'


@dataclass
class ScanSurfaceStart(RunSystem):
    asteroid: Entity
    caller_crew: Entity
    _function_name: str = 'ScanSurfaceStart'


@dataclass
class SeedAsteroids(RunSystem):
    asteroids: List[SeededAsteroid]
    _function_name: str = 'SeedAsteroids'


@dataclass
class SeedColony(RunSystem):
    colony: u64
    building_type: u64
    _function_name: str = 'SeedColony'


@dataclass
class SeedCrewmates(RunSystem):
    crewmates: List[SeededCrewmate]
    _function_name: str = 'SeedCrewmates'


@dataclass
class SeedHabitat(RunSystem):
    _function_name: str = 'SeedHabitat'


@dataclass
class SeedOrders(RunSystem):
    market_lot: u64
    warehouse_lot: u64
    _function_name: str = 'SeedOrders'


@dataclass
class SendDelivery(RunSystem):
    origin: Entity
    origin_slot: u64
    products: List[InventoryItem]
    dest: Entity
    dest_slot: u64
    caller_crew: Entity
    _function_name: str = 'SendDelivery'


@dataclass
class StationCrew(RunSystem):
    destination: Entity
    caller_crew: Entity
    _function_name: str = 'StationCrew'


@dataclass
class TransferPrepaidAgreement(RunSystem):
    target: Entity
    permission: u64
    permitted: Entity
    new_permitted: Entity
    caller_crew: Entity
    _function_name: str = 'TransferPrepaidAgreement'


@dataclass
class TransitBetweenFinish(RunSystem):
    caller_crew: Entity
    _function_name: str = 'TransitBetweenFinish'


@dataclass
class TransitBetweenStart(RunSystem):
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
class UndockShip(RunSystem):
    ship: Entity
    powered: Bool
    caller_crew: Entity
    _function_name: str = 'UndockShip'


@dataclass
class UnlistDepositForSale(RunSystem):
    deposit: Entity
    caller_crew: Entity
    _function_name: str = 'UnlistDepositForSale'


@dataclass
class Whitelist(RunSystem):
    target: Entity
    permission: u64
    permitted: Entity
    caller_crew: Entity
    _function_name: str = 'Whitelist'


@dataclass
class WhitelistAccount(RunSystem):
    target: Entity
    permission: u64
    permitted: ContractAddress
    caller_crew: Entity
    _function_name: str = 'WhitelistAccount'


@dataclass
class WriteComponent(RunSystem):
    name: felt252
    path: List[felt252]
    data: List[felt252]
    _function_name: str = 'WriteComponent'


class UnknownSystemCall(RunSystem):
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


ALL_SYSTEMS: Dict[str, RunSystem | List[RunSystem]] = {
    AcceptContractAgreement._function_name: AcceptContractAgreement,
    AcceptDelivery._function_name: AcceptDelivery,
    AcceptPrepaidAgreement._function_name: AcceptPrepaidAgreement,
    AcceptPrepaidMerkleAgreement._function_name: AcceptPrepaidMerkleAgreement,
    ActivateEmergency._function_name: ActivateEmergency,
    AnnotateEvent._function_name: AnnotateEvent,
    ArrangeCrew._function_name: ArrangeCrew,
    AssembleShipFinish._function_name: AssembleShipFinish,
    AssembleShipStart._function_name: AssembleShipStart,
    AssignContractPolicy._function_name: AssignContractPolicy,
    AssignPrepaidMerklePolicy._function_name: AssignPrepaidMerklePolicy,
    AssignPrepaidPolicy._function_name: AssignPrepaidPolicy,
    AssignPublicPolicy._function_name: AssignPublicPolicy,
    CancelDelivery._function_name: CancelDelivery,
    CancelPrepaidAgreement._function_name: CancelPrepaidAgreement,
    CancelSellOrder._function_name: CancelSellOrder,
    ChangeName._function_name: ChangeName,
    CheckForRandomEvent._function_name: CheckForRandomEvent,
    ClaimArrivalReward._function_name: ClaimArrivalReward,
    ClaimPrepareForLaunchReward._function_name: ClaimPrepareForLaunchReward,
    ClaimTestnetSway._function_name: ClaimTestnetSway,
    CollectEmergencyPropellant._function_name: CollectEmergencyPropellant,
    CommandeerShip._function_name: CommandeerShip,
    ConfigureExchange._function_name: ConfigureExchange,
    ConstructionAbandon._function_name: ConstructionAbandon,
    ConstructionDeconstruct._function_name: ConstructionDeconstruct,
    ConstructionFinish._function_name: ConstructionFinish,
    ConstructionPlan._function_name: ConstructionPlan,
    ConstructionStart._function_name: ConstructionStart,
    CreateBuyOrder._function_name: CreateBuyOrder,
    CreateSellOrder._function_name: CreateSellOrder,
    DeactivateEmergency._function_name: DeactivateEmergency,
    DelegateCrew._function_name: DelegateCrew,
    DirectMessage._function_name: DirectMessage,
    DockShip._function_name: DockShip,
    DumpDelivery._function_name: DumpDelivery,
    EjectCrew._function_name: EjectCrew,
    ExchangeCrew._function_name: ExchangeCrew,
    ExtendPrepaidAgreement._function_name: ExtendPrepaidAgreement,
    ExtractResourceFinish._function_name: ExtractResourceFinish,
    ExtractResourceStart._function_name: ExtractResourceStart,
    FillBuyOrder._function_name: FillBuyOrder,
    FillSellOrder._function_name: FillSellOrder,
    GrantAdalians._function_name: GrantAdalians,
    GrantStarterPack._function_name: GrantStarterPack,
    InitializeArvadian._function_name: InitializeArvadian,
    InitializeAsteroid._function_name: InitializeAsteroid,
    ListDepositForSale._function_name: ListDepositForSale,
    ManageAsteroid._function_name: ManageAsteroid,
    PackageDelivery._function_name: PackageDelivery,
    ProcessProductsFinish._function_name: ProcessProductsFinish,
    ProcessProductsStart._function_name: ProcessProductsStart,
    PurchaseAdalian._function_name: PurchaseAdalian,
    PurchaseAsteroid._function_name: PurchaseAsteroid,
    PurchaseDeposit._function_name: PurchaseDeposit,
    ReadComponent._function_name: ReadComponent,
    ReceiveDelivery._function_name: ReceiveDelivery,
    RecruitAdalian._function_name: RecruitAdalian,
    RekeyInbox._function_name: RekeyInbox,
    RemoveAccountFromWhitelist._function_name: RemoveAccountFromWhitelist,
    RemoveContractPolicy._function_name: RemoveContractPolicy,
    RemoveFromWhitelist._function_name: RemoveFromWhitelist,
    RemovePrepaidMerklePolicy._function_name: RemovePrepaidMerklePolicy,
    RemovePrepaidPolicy._function_name: RemovePrepaidPolicy,
    RemovePublicPolicy._function_name: RemovePublicPolicy,
    RepossessBuilding._function_name: RepossessBuilding,
    ResolveRandomEvent._function_name: ResolveRandomEvent,
    ResupplyFood._function_name: ResupplyFood,
    ResupplyFoodFromExchange._function_name: ResupplyFoodFromExchange,
    SampleDepositFinish._function_name: SampleDepositFinish,
    SampleDepositImprove._function_name: SampleDepositImprove,
    SampleDepositStart._function_name: SampleDepositStart,
    ScanResourcesFinish._function_name: ScanResourcesFinish,
    ScanResourcesStart._function_name: ScanResourcesStart,
    ScanSurfaceFinish._function_name: ScanSurfaceFinish,
    ScanSurfaceStart._function_name: ScanSurfaceStart,
    SeedAsteroids._function_name: SeedAsteroids,
    SeedColony._function_name: SeedColony,
    SeedCrewmates._function_name: SeedCrewmates,
    SeedHabitat._function_name: SeedHabitat,
    SeedOrders._function_name: SeedOrders,
    SendDelivery._function_name: SendDelivery,
    StationCrew._function_name: StationCrew,
    TransferPrepaidAgreement._function_name: TransferPrepaidAgreement,
    TransitBetweenFinish._function_name: TransitBetweenFinish,
    TransitBetweenStart._function_name: TransitBetweenStart,
    UndockShip._function_name: UndockShip,
    UnlistDepositForSale._function_name: UnlistDepositForSale,
    Whitelist._function_name: Whitelist,
    WhitelistAccount._function_name: WhitelistAccount,
    WriteComponent._function_name: WriteComponent,
}

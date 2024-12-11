from dataclasses import dataclass  # noqa: F401
from typing import Dict, List  # noqa: F401

from starknet_py.hash.utils import _starknet_keccak

from influencepy.starknet.net.datatypes import *  # noqa: F401
from influencepy.starknet.net.structs import *  # noqa: F401


class ComponentReference(Schema):
    pass


class Component(Schema):
    """Note: The name of this event class was reversed from its keccak hash.
    As such, it may be incorrect and is subject to change."""
    _name: str
    _version_key: int  # optional versioning keys


@dataclass
class Building(Component):
    status: u64
    building_type: u64
    planned_at: u64
    finish_time: u64
    _name: str = 'Building'


@dataclass
class BuildingType(Component):
    process_type: u64
    site_slot: u64
    site_type: u64
    _name: str = 'BuildingType'


@dataclass
class Celestial(Component):
    celestial_type: u64
    mass: CubitFixedPoint128
    radius: CubitFixedPoint64
    purchase_order: u64
    scan_status: u64
    scan_finish_time: u64
    bonuses: u64
    abundances: felt252
    _name: str = 'Celestial'


@dataclass
class ContractAgreement(Component):
    address: ContractAddress
    _name: str = 'ContractAgreement'


@dataclass
class ContractPolicy(Component):
    address: ContractAddress
    _name: str = 'ContractPolicy'


@dataclass
class Control(Component):
    controller: Entity
    _name: str = 'Control'


@dataclass
class CrewV0(Component):
    delegated_to: ContractAddress
    roster: List[u64]
    last_fed: u64
    ready_at: u64
    unknown_field_1: u64
    unknown_field_2: u64
    _name: str = 'Crew'
    _version_key: int = 0


@dataclass
class CrewV1(Component):
    delegated_to: ContractAddress
    roster: List[u64]
    last_fed: u64
    ready_at: u64
    action_type: u64
    action_target: Entity
    action_round: u64
    action_weight: u64
    action_strategy: u64
    _name: str = 'Crew'
    _version_key: int = 1


@dataclass
class Crewmate(Component):
    status: u64
    collection: u64
    class_: u64
    title: u64
    appearance: u128
    cosmetic: List[u64]
    impactful: List[u64]
    _name: str = 'Crewmate'


@dataclass
class Delivery(Component):
    status: u64
    origin: Entity
    origin_slot: u64
    dest: Entity
    dest_slot: u64
    finish_time: u64
    contents: List[InventoryItem]
    _name: str = 'Delivery'


@dataclass
class Deposit(Component):
    status: u64
    resource: u64
    initial_yield: u64
    remaining_yield: u64
    finish_time: u64
    yield_eff: CubitFixedPoint64
    _name: str = 'Deposit'


@dataclass
class Dock(Component):
    dock_type: u64
    docked_ships: u64
    ready_at: u64
    _name: str = 'Dock'


@dataclass
class DockType(Component):
    cap: u64
    delay: u64
    _name: str = 'DockType'


@dataclass
class DryDock(Component):
    dry_dock_type: u64
    status: u64
    output_ship: Entity
    finish_time: u64
    _name: str = 'DryDock'


@dataclass
class DryDockType(Component):
    max_mass: u64
    max_volume: u64
    _name: str = 'DryDockType'


@dataclass
class Exchange(Component):
    exchange_type: u64
    maker_fee: u64
    taker_fee: u64
    orders: u64
    allowed_products: List[u64]
    _name: str = 'Exchange'


@dataclass
class ExchangeType(Component):
    allowed_products: u64
    _name: str = 'ExchangeType'


@dataclass
class Extractor(Component):
    extractor_type: u64
    status: u64
    output_product: u64
    yield_: u64
    destination: Entity
    destination_slot: u64
    finish_time: u64
    _name: str = 'Extractor'


@dataclass
class Inventory(Component):
    inventory_type: u64
    status: u64
    mass: u64
    volume: u64
    reserved_mass: u64
    reserved_volume: u64
    contents: List[InventoryItem]
    reservations: List[InventoryItem]
    _name: str = 'Inventory'


@dataclass
class InventoryType(Component):
    mass: u64
    volume: u64
    modifiable: Bool
    products: List[InventoryItem]
    _name: str = 'InventoryType'


@dataclass
class Location(Component):
    location: Entity
    _name: str = 'Location'


@dataclass
class ModifierType(Component):
    class_: u64
    dept_type: u64
    dept_eff: u64
    mgmt_eff: u64
    trait_type: u64
    trait_eff: u64
    further_modified: Bool
    _name: str = 'ModifierType'


@dataclass
class Name(Component):
    name: ShortString
    _name: str = 'Name'


@dataclass
class Orbit(Component):
    a: CubitFixedPoint128
    ecc: CubitFixedPoint128
    inc: CubitFixedPoint128
    raan: CubitFixedPoint128
    argp: CubitFixedPoint128
    m: CubitFixedPoint128
    _name: str = 'Orbit'


@dataclass
class Order(Component):
    status: u64
    amount: u64
    valid_time: u64
    maker_fee: u64
    _name: str = 'Order'


@dataclass
class PrepaidAgreement(Component):
    rate: u64
    initial_term: u64
    notice_period: u64
    start_time: u64
    end_time: u64
    notice_time: u64
    _name: str = 'PrepaidAgreement'


@dataclass
class PrepaidPolicy(Component):
    rate: u64
    initial_term: u64
    notice_period: u64
    _name: str = 'PrepaidPolicy'


@dataclass
class PrivateSale(Component):
    status: u64
    amount: u64
    _name: str = 'PrivateSale'


@dataclass
class ProcessType(Component):
    setup_time: u64
    recipe_time: u64
    batched: Bool
    processor_type: u64
    inputs: List[InventoryItem]
    outputs: List[InventoryItem]
    _name: str = 'ProcessType'


@dataclass
class Processor(Component):
    processor_type: u64
    status: u64
    running_process: u64
    output_product: u64
    recipes: CubitFixedPoint64
    secondary_eff: CubitFixedPoint64
    destination: Entity
    destination_slot: u64
    finish_time: u64
    _name: str = 'Processor'


@dataclass
class ProductType(Component):
    mass: u64
    volume: u64
    _name: str = 'ProductType'


@dataclass
class PublicPolicy(Component):
    public: Bool
    _name: str = 'PublicPolicy'


@dataclass
class ShipType(Component):
    cargo_inventory_type: u64
    cargo_slot: u64
    docking: Bool
    exhaust_velocity: CubitFixedPoint128
    hull_mass: u64
    landing: Bool
    process_type: u64
    propellant_emergency_divisor: u64
    propellant_inventory_type: u64
    propellant_slot: u64
    propellant_type: u64
    station_type: u64
    _name: str = 'ShipType'


@dataclass
class ShipV0(Component):
    ship_type: u64
    status: u64
    ready_at: u64
    variant: u64
    _name: str = 'Ship'
    _version_key: int = 0


@dataclass
class ShipV1(Component):
    ship_type: u64
    status: u64
    ready_at: u64
    variant: u64
    emergency_at: u64
    transit_origin: Entity
    transit_departure: u64
    transit_destination: Entity
    transit_arrival: u64
    _name: str = 'Ship'
    _version_key: int = 1


@dataclass
class ShipVariantType(Component):
    ship_type: u64
    exhaust_velocity_modifier: CubitFixedPoint64
    _name: str = 'ShipVariantType'


@dataclass
class Station(Component):
    station_type: u64
    population: u64
    _name: str = 'Station'


@dataclass
class StationType(Component):
    cap: u64
    recruitment: Bool
    efficiency: CubitFixedPoint64
    _name: str = 'StationType'


@dataclass
class Unique(Component):
    unique: ShortString
    used: Bool
    _name: str = 'Unique'


@dataclass
class WhitelistAgreement(Component):
    whitelisted: Bool
    _name: str = 'WhitelistAgreement'


class UnknownComponent(Component):
    def __init__(self, name: str, keys: List[int], data: Calldata):
        self.name = name
        self.keys = keys
        self.data = data


ALL_COMPONENTS: Dict[str, Component | List[Component]] = {
    Building._name: Building,
    BuildingType._name: BuildingType,
    Celestial._name: Celestial,
    ContractAgreement._name: ContractAgreement,
    ContractPolicy._name: ContractPolicy,
    Control._name: Control,
    CrewV0._name: [CrewV0, CrewV1],
    Crewmate._name: Crewmate,
    Delivery._name: Delivery,
    Deposit._name: Deposit,
    Dock._name: Dock,
    DockType._name: DockType,
    DryDock._name: DryDock,
    DryDockType._name: DryDockType,
    Exchange._name: Exchange,
    ExchangeType._name: ExchangeType,
    Extractor._name: Extractor,
    Inventory._name: Inventory,
    InventoryType._name: InventoryType,
    Location._name: Location,
    ModifierType._name: ModifierType,
    Name._name: Name,
    Orbit._name: Orbit,
    Order._name: Order,
    PrepaidAgreement._name: PrepaidAgreement,
    PrepaidPolicy._name: PrepaidPolicy,
    PrivateSale._name: PrivateSale,
    ProcessType._name: ProcessType,
    Processor._name: Processor,
    ProductType._name: ProductType,
    PublicPolicy._name: PublicPolicy,
    ShipType._name: ShipType,
    ShipV0._name: [ShipV0, ShipV1],
    ShipVariantType._name: ShipVariantType,
    Station._name: Station,
    StationType._name: StationType,
    Unique._name: Unique,
    WhitelistAgreement._name: WhitelistAgreement,
}

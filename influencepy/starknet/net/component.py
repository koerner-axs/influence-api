from dataclasses import dataclass  # noqa: F401
from typing import Dict, List  # noqa: F401

from influencepy.starknet.net.datatypes import *  # noqa: F401
from influencepy.starknet.net.struct import *  # noqa: F401


class Component:
    _name: str


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
class Crew(Component):
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
    modifiable: bool
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
    further_modified: bool
    _name: str = 'ModifierType'


@dataclass
class Name(Component):
    name: shortstr
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
    batched: bool
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
    public: bool
    _name: str = 'PublicPolicy'


@dataclass
class Ship(Component):
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


@dataclass
class ShipType(Component):
    cargo_inventory_type: u64
    cargo_slot: u64
    docking: bool
    exhaust_velocity: CubitFixedPoint128
    hull_mass: u64
    landing: bool
    process_type: u64
    propellant_emergency_divisor: u64
    propellant_inventory_type: u64
    propellant_slot: u64
    propellant_type: u64
    station_type: u64
    _name: str = 'ShipType'


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
    recruitment: bool
    efficiency: CubitFixedPoint64
    _name: str = 'StationType'


@dataclass
class Unique(Component):
    unique: felt252
    _name: str = 'Unique'


@dataclass
class WhitelistAgreement(Component):
    whitelisted: bool


ALL_COMPONENTS: Dict[str, Component] = {
    "Building._key": Building,
    "BuildingType._key": BuildingType,
    "Celestial._key": Celestial,
    "ContractAgreement._key": ContractAgreement,
    "ContractPolicy._key": ContractPolicy,
    "Control._key": Control,
    "Crew._key": Crew,
    "Crewmate._key": Crewmate,
    "Delivery._key": Delivery,
    "Deposit._key": Deposit,
    "Dock._key": Dock,
    "DockType._key": DockType,
    "DryDock._key": DryDock,
    "DryDockType._key": DryDockType,
    "Exchange._key": Exchange,
    "ExchangeType._key": ExchangeType,
    "Extractor._key": Extractor,
    "Inventory._key": Inventory,
    "InventoryType._key": InventoryType,
    "Location._key": Location,
    "ModifierType._key": ModifierType,
    "Name._key": Name,
    "Orbit._key": Orbit,
    "Order._key": Order,
    "PrepaidAgreement._key": PrepaidAgreement,
    "PrepaidPolicy._key": PrepaidPolicy,
    "PrivateSale._key": PrivateSale,
    "ProcessType._key": ProcessType,
    "Processor._key": Processor,
    "ProductType._key": ProductType,
    "PublicPolicy._key": PublicPolicy,
    "Ship._key": Ship,
    "ShipType._key": ShipType,
    "ShipVariantType._key": ShipVariantType,
    "Station._key": Station,
    "StationType._key": StationType,
    "Unique._key": Unique,
    "WhitelistAgreement._key": WhitelistAgreement,
}

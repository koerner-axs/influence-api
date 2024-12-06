type_map = {
    'core::integer::u64': 'u64',
    'core::array::Span::<core::integer::u64>': 'List[u64]',
    'core::integer::u128': 'u128',
    'core::array::Span::<core::integer::u128>': 'List[u128]',
    'core::integer::u256': 'u256',
    'core::array::Span::<core::integer::u256>': 'List[u256]',
    'core::felt252': 'felt252',
    'core::array::Span::<core::felt252>': 'List[felt252]',
    'core::bool': 'bool',
    'core::starknet::contract_address::ContractAddress': 'ContractAddress',
    'influence::common::types::string::String': 'shortstr',
    'cubit::f64::types::fixed::Fixed': 'CubitFixedPoint64',
    'cubit::f128::types::fixed::Fixed': 'CubitFixedPoint128',
    'influence::common::types::entity::Entity': 'Entity',
    'influence::common::types::inventory_item::InventoryItem': 'InventoryItem',
    'core::array::Span::<influence::common::types::inventory_item::InventoryItem>': 'List[InventoryItem]'
}

from typing import Dict, Tuple, Any

from influencepy.starknet.net.contract_call import SwayTransferWithConfirmation, UnknownContractCall
from influencepy.starknet.net.schema import Schema
from influencepy.starknet.net.system import *


class SystemCallDispatcher(Schema):
    _contract_address: int = SystemCall.contract_address
    _selector: int = SystemCall.selector
    _variants: Dict[str, SystemCall] = {
        variant.function_name: variant for variant in [
            AcceptContractAgreement,
            AcceptDelivery,
            AcceptPrepaidAgreement,
            AcceptPrepaidMerkleAgreement,
            ActivateEmergency,
            AnnotateEvent,
            ArrangeCrew,
            AssembleShipFinish,
            AssembleShipStart,
            AssignContractPolicy,
            AssignPrepaidMerklePolicy,
            AssignPrepaidPolicy,
            AssignPublicPolicy,
            CancelDelivery,
            CancelPrepaidAgreement,
            CancelSellOrder,
            ChangeName,
            CheckForRandomEvent,
            ClaimArrivalReward,
            ClaimPrepareForLaunchReward,
            ClaimTestnetSway,
            CollectEmergencyPropellant,
            CommandeerShip,
            ConfigureExchange,
            ConstructionAbandon,
            ConstructionDeconstruct,
            ConstructionFinish,
            ConstructionPlan,
            ConstructionStart,
            CreateBuyOrder,
            CreateSellOrder,
            DeactivateEmergency,
            DelegateCrew,
            DockShip,
            DumpDelivery,
            EjectCrew,
            ExchangeCrew,
            ExtendPrepaidAgreement,
            ExtractResourceFinish,
            ExtractResourceStart,
            FillBuyOrder,
            FillSellOrder,
            InitializeArvadian,
            InitializeAsteroid,
            ListDepositForSale,
            ManageAsteroid,
            PackageDelivery,
            ProcessProductsFinish,
            ProcessProductsStart,
            PurchaseAdalian,
            PurchaseAsteroid,
            PurchaseDeposit,
            ReadComponent,
            ReceiveDelivery,
            RecruitAdalian,
            RemoveAccountFromWhiteList,
            RemoveContractPolicy,
            RemoveFromWhitelist,
            RemovePrepaidMerklePolicy,
            RemovePrepaidPolicy,
            RemovePublicPolicy,
            RepossessBuilding,
            ResolveRandomEvent,
            ResupplyFood,
            ResupplyFoodFromExchange,
            SampleDepositFinish,
            SampleDepositImprove,
            SampleDepositStart,
            ScanResourcesFinish,
            ScanResourcesStart,
            ScanSurfaceFinish,
            ScanSurfaceStart,
            SeedAsteroids,
            SeedColony,
            SeedCrewmates,
            SeedHabitat,
            SeedOrders,
            SendDelivery,
            StationCrew,
            TransitBetweenFinish,
            TransitBetweenStart,
            UndockShip,
            UnlistDepositForSale,
            Whitelist,
            WhitelistAccount,
            WriteComponent
        ]
    }

    @classmethod
    def from_calldata(cls, calldata: Calldata, **kwargs) -> Schema | Any:
        function_name = calldata.pop_string()
        _arg_count = calldata.pop_int()
        if function_name in cls.subtype_map:
            return cls.subtype_map[function_name].from_calldata(calldata)
        else:
            raise ValueError(f'Unknown function name {function_name}')


class ContractCallDispatcher(Schema):
    _variants: Dict[Tuple[int, int], ContractCall] = {
        (variant._contract_address, variant._selector): variant for variant in [
            SystemCallDispatcher,
            SwayTransferWithConfirmation
        ]
    }

    @classmethod
    def from_calldata(cls, calldata: Calldata, **kwargs) -> ContractCall:
        contract_address = calldata.pop_int()
        selector = calldata.pop_int()
        arg_count = calldata.pop_int()
        variant: ContractCall = cls._variants.get((contract_address, selector), UnknownContractCall)
        return variant.from_calldata(calldata, contract_address=contract_address, selector=selector,
                                     arg_count=arg_count, **kwargs)

from typing import Dict, Any

from influencepy.starknet.net.contract_call import UnknownContractCall
from influencepy.starknet.net.schema import Schema
from influencepy.starknet.net.sway import *
from influencepy.starknet.net.system import *


class RunSystemDispatcher(Schema):
    _contract_address: int = DISPATCHER_ADDRESS  # TODO: maybe remove
    _selector: int = get_selector_from_name('run_system')
    _variants: Dict[str, Schema] = {
        variant._function_name: variant for variant in [
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
    def from_calldata(cls, calldata: Calldata, **kwargs) -> Schema:
        function_name = calldata.pop_string()
        arg_count = calldata.pop_int()
        variant: Schema = cls._variants.get(function_name, UnknownSystemCall)
        kwargs.update({'function_name': function_name, 'arg_count': arg_count})
        return variant.from_calldata(calldata, **kwargs)


class DispatcherContractCallDispatcher(Schema):
    _contract_address: int = DISPATCHER_ADDRESS
    _variants: Dict[int, Schema] = {
        RunSystemDispatcher._selector: RunSystemDispatcher
    }

    @classmethod
    def from_calldata(cls, calldata: Calldata, **kwargs) -> Schema:
        selector = calldata.pop_int()
        arg_count = calldata.pop_int()
        variant: Schema = cls._variants.get(selector, UnknownContractCall)
        kwargs.update({'selector': selector, 'arg_count': arg_count})
        return variant.from_calldata(calldata, **kwargs)


class SwayTokenContractCallDispatcher(Schema):
    _contract_address: int = SwayTokenContractCall._contract_address
    _variants: Dict[int, SwayTokenContractCall] = {
        SwayTransferWithConfirmation._selector: SwayTransferWithConfirmation,
        SwayTransferFromWithConfirmation._selector: SwayTransferFromWithConfirmation,
        SwayConfirmReceipt._selector: SwayConfirmReceipt,
        SwayAllowance._selector: SwayAllowance,
        SwayApprove._selector: SwayApprove,
        SwayBalanceOf._selector: SwayBalanceOf,
        DecreaseAllowance._selector: DecreaseAllowance,
        IncreaseAllowance._selector: IncreaseAllowance,
        SwayTransfer._selector: SwayTransfer,
        SwayTransferFrom._selector: SwayTransferFrom
    }

    @classmethod
    def from_calldata(cls, calldata: Calldata, **kwargs) -> ContractCall:
        selector = calldata.pop_int()
        arg_count = calldata.pop_int()
        variant: ContractCall = cls._variants.get(selector, UnknownContractCall)
        kwargs.update({'selector': selector, 'arg_count': arg_count})
        return variant.from_calldata(calldata, **kwargs)


class ContractCallDispatcher(Schema):
    _variants: Dict[int, Schema] = {
        DispatcherContractCallDispatcher._contract_address: DispatcherContractCallDispatcher,
        SwayTokenContractCall._contract_address: SwayTokenContractCallDispatcher
    }

    @classmethod
    def from_calldata(cls, calldata: Calldata, **kwargs) -> Schema:
        contract_address = calldata.pop_int()
        if contract_address in cls._variants:
            variant: Schema = cls._variants[contract_address]
            kwargs.update({'contract_address': contract_address})
            return variant.from_calldata(calldata, **kwargs)
        else:
            selector = calldata.pop_int()
            arg_count = calldata.pop_int()
            kwargs.update({'contract_address': contract_address, 'selector': selector, 'arg_count': arg_count})
            return UnknownContractCall.from_calldata(calldata, **kwargs)

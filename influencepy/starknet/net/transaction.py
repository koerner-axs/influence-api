from typing import List, Any

from influencepy.starknet.net.contract_call import ContractCall
from influencepy.starknet.net.dispatcher import ContractCallDispatcher
from influencepy.starknet.net.schema import Schema


class MultiInvocationTransaction(Schema):
    invocations: List[ContractCallDispatcher]

    def __init__(self):
        self.invocations = []

    def get_invocation(self, index: int) -> ContractCall:
        return self.invocations[index]

    def prepend_contract_call(self, contract_call: ContractCall | Any):
        self.invocations.insert(0, contract_call)

    def append_contract_call(self, contract_call: ContractCall | Any):
        self.invocations.append(contract_call)

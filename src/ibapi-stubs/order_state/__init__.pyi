from _typeshed import Incomplete
from ibapi.const import UNSET_DOUBLE as UNSET_DOUBLE

class OrderState:
    status: str
    initMarginBefore: str
    maintMarginBefore: str
    equityWithLoanBefore: str
    initMarginChange: str
    maintMarginChange: str
    equityWithLoanChange: str
    initMarginAfter: str
    maintMarginAfter: str
    equityWithLoanAfter: str
    commission: Incomplete
    minCommission: Incomplete
    maxCommission: Incomplete
    commissionCurrency: str
    warningText: str
    completedTime: str
    completedStatus: str
    def __init__(self) -> None: ...

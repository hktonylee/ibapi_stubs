from _typeshed import Incomplete
from ibapi.const import UNSET_DECIMAL as UNSET_DECIMAL, UNSET_DOUBLE as UNSET_DOUBLE
from ibapi.object_implem import Object as Object
from ibapi.utils import decimalMaxString as decimalMaxString, floatMaxString as floatMaxString

class OrderAllocation(Object):
    account: str
    position: Incomplete
    positionDesired: Incomplete
    positionAfter: Incomplete
    desiredAllocQty: Incomplete
    allowedAllocQty: Incomplete
    isMonetary: bool
    def __init__(self) -> None: ...

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
    commissionAndFees: Incomplete
    minCommissionAndFees: Incomplete
    maxCommissionAndFees: Incomplete
    commissionAndFeesCurrency: str
    marginCurrency: str
    initMarginBeforeOutsideRTH: Incomplete
    maintMarginBeforeOutsideRTH: Incomplete
    equityWithLoanBeforeOutsideRTH: Incomplete
    initMarginChangeOutsideRTH: Incomplete
    maintMarginChangeOutsideRTH: Incomplete
    equityWithLoanChangeOutsideRTH: Incomplete
    initMarginAfterOutsideRTH: Incomplete
    maintMarginAfterOutsideRTH: Incomplete
    equityWithLoanAfterOutsideRTH: Incomplete
    suggestedSize: Incomplete
    rejectReason: str
    orderAllocations: Incomplete
    warningText: str
    completedTime: str
    completedStatus: str
    def __init__(self) -> None: ...

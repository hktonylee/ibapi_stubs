from _typeshed import Incomplete
from enum import Enum
from ibapi.const import UNSET_DECIMAL as UNSET_DECIMAL, UNSET_INTEGER as UNSET_INTEGER
from ibapi.object_implem import Object as Object
from ibapi.utils import decimalMaxString as decimalMaxString, floatMaxString as floatMaxString, getEnumTypeName as getEnumTypeName, intMaxString as intMaxString, longMaxString as longMaxString

class Execution(Object):
    execId: str
    time: str
    acctNumber: str
    exchange: str
    side: str
    shares: Incomplete
    price: float
    permId: int
    clientId: int
    orderId: int
    liquidation: int
    cumQty: Incomplete
    avgPrice: float
    orderRef: str
    evRule: str
    evMultiplier: float
    modelCode: str
    lastLiquidity: int
    pendingPriceRevision: bool
    submitter: str
    optExerciseOrLapseType: Incomplete
    def __init__(self) -> None: ...

class ExecutionFilter(Object):
    clientId: int
    acctCode: str
    time: str
    symbol: str
    secType: str
    exchange: str
    side: str
    lastNDays: Incomplete
    specificDates: Incomplete
    def __init__(self) -> None: ...

class OptionExerciseType(Enum):
    NoneItem = (-1, 'None')
    Exercise = (1, 'Exercise')
    Lapse = (2, 'Lapse')
    DoNothing = (3, 'DoNothing')
    Assigned = (100, 'Assigned ')
    AutoexerciseClearing = (101, 'AutoexerciseClearing')
    Expired = (102, 'Expired')
    Netting = (103, 'Netting')
    AutoexerciseTrading = (200, 'AutoexerciseTrading')

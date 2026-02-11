from _typeshed import Incomplete
from ibapi.common import UNSET_DECIMAL as UNSET_DECIMAL
from ibapi.object_implem import Object as Object
from ibapi.utils import decimalMaxString as decimalMaxString, floatMaxString as floatMaxString, intMaxString as intMaxString

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
    def __init__(self) -> None: ...

class ExecutionFilter(Object):
    clientId: int
    acctCode: str
    time: str
    symbol: str
    secType: str
    exchange: str
    side: str
    def __init__(self) -> None: ...

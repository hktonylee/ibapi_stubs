from ibapi.object_implem import Object as Object

class Execution(Object):
    execId: str
    time: str
    acctNumber: str
    exchange: str
    side: str
    shares: float
    price: float
    permId: int
    clientId: int
    orderId: int
    liquidation: int
    cumQty: float
    avgPrice: float
    orderRef: str
    evRule: str
    evMultiplier: float
    modelCode: str
    lastLiquidity: int
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

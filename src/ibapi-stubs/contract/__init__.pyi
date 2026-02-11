from _typeshed import Incomplete
from ibapi.object_implem import Object as Object

SAME_POS: Incomplete
OPEN_POS: Incomplete
CLOSE_POS: Incomplete
UNKNOWN_POS: Incomplete

class ComboLeg(Object):
    conId: int
    ratio: int
    action: str
    exchange: str
    openClose: int
    shortSaleSlot: int
    designatedLocation: str
    exemptCode: int
    def __init__(self) -> None: ...

class DeltaNeutralContract(Object):
    conId: int
    delta: float
    price: float
    def __init__(self) -> None: ...

class Contract(Object):
    conId: int
    symbol: str
    secType: str
    lastTradeDateOrContractMonth: str
    strike: float
    right: str
    multiplier: str
    exchange: str
    primaryExchange: str
    currency: str
    localSymbol: str
    tradingClass: str
    includeExpired: bool
    secIdType: str
    secId: str
    comboLegsDescrip: str
    comboLegs: Incomplete
    deltaNeutralContract: Incomplete
    def __init__(self) -> None: ...

class ContractDetails(Object):
    contract: Incomplete
    marketName: str
    minTick: float
    orderTypes: str
    validExchanges: str
    priceMagnifier: int
    underConId: int
    longName: str
    contractMonth: str
    industry: str
    category: str
    subcategory: str
    timeZoneId: str
    tradingHours: str
    liquidHours: str
    evRule: str
    evMultiplier: int
    mdSizeMultiplier: int
    aggGroup: int
    underSymbol: str
    underSecType: str
    marketRuleIds: str
    secIdList: Incomplete
    realExpirationDate: str
    lastTradeTime: str
    cusip: str
    ratings: str
    descAppend: str
    bondType: str
    couponType: str
    callable: bool
    putable: bool
    coupon: int
    convertible: bool
    maturity: str
    issueDate: str
    nextOptionDate: str
    nextOptionType: str
    nextOptionPartial: bool
    notes: str
    def __init__(self) -> None: ...

class ContractDescription(Object):
    contract: Incomplete
    derivativeSecTypes: Incomplete
    def __init__(self) -> None: ...

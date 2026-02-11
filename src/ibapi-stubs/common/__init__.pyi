from _typeshed import Incomplete
from ibapi.const import UNSET_DECIMAL as UNSET_DECIMAL, UNSET_INTEGER as UNSET_INTEGER
from ibapi.enum_implem import Enum as Enum
from ibapi.object_implem import Object as Object
from ibapi.utils import decimalMaxString as decimalMaxString, floatMaxString as floatMaxString, intMaxString as intMaxString

TickerId = int
OrderId = int
TagValueList = list
FaDataType = int
FaDataTypeEnum: Incomplete
MarketDataType = int
MarketDataTypeEnum: Incomplete
Liquidities = int
LiquiditiesEnum: Incomplete
SetOfString = set
SetOfFloat = set
ListOfOrder = list
ListOfFamilyCode = list
ListOfContractDescription = list
ListOfDepthExchanges = list
ListOfNewsProviders = list
SmartComponentMap = dict
HistogramDataList = list
ListOfPriceIncrements = list
ListOfHistoricalTick = list
ListOfHistoricalTickBidAsk = list
ListOfHistoricalTickLast = list
ListOfHistoricalSessions = list

class BarData(Object):
    date: str
    open: float
    high: float
    low: float
    close: float
    volume: Incomplete
    wap: Incomplete
    barCount: int
    def __init__(self) -> None: ...

class RealTimeBar(Object):
    time: Incomplete
    endTime: Incomplete
    open_: Incomplete
    high: Incomplete
    low: Incomplete
    close: Incomplete
    volume: Incomplete
    wap: Incomplete
    count: Incomplete
    def __init__(self, time: int = 0, endTime: int = -1, open_: float = 0.0, high: float = 0.0, low: float = 0.0, close: float = 0.0, volume=..., wap=..., count: int = 0) -> None: ...

class HistogramData(Object):
    price: float
    size: Incomplete
    def __init__(self) -> None: ...

class NewsProvider(Object):
    code: str
    name: str
    def __init__(self) -> None: ...

class DepthMktDataDescription(Object):
    exchange: str
    secType: str
    listingExch: str
    serviceDataType: str
    aggGroup: Incomplete
    def __init__(self) -> None: ...

class SmartComponent(Object):
    bitNumber: int
    exchange: str
    exchangeLetter: str
    def __init__(self) -> None: ...

class TickAttrib(Object):
    canAutoExecute: bool
    pastLimit: bool
    preOpen: bool
    def __init__(self) -> None: ...

class TickAttribBidAsk(Object):
    bidPastLow: bool
    askPastHigh: bool
    def __init__(self) -> None: ...

class TickAttribLast(Object):
    pastLimit: bool
    unreported: bool
    def __init__(self) -> None: ...

class FamilyCode(Object):
    accountID: str
    familyCodeStr: str
    def __init__(self) -> None: ...

class PriceIncrement(Object):
    lowEdge: float
    increment: float
    def __init__(self) -> None: ...

class HistoricalTick(Object):
    time: int
    price: float
    size: Incomplete
    def __init__(self) -> None: ...

class HistoricalTickBidAsk(Object):
    time: int
    tickAttribBidAsk: Incomplete
    priceBid: float
    priceAsk: float
    sizeBid: Incomplete
    sizeAsk: Incomplete
    def __init__(self) -> None: ...

class HistoricalTickLast(Object):
    time: int
    tickAttribLast: Incomplete
    price: float
    size: Incomplete
    exchange: str
    specialConditions: str
    def __init__(self) -> None: ...

class HistoricalSession(Object):
    startDateTime: str
    endDateTime: str
    refDate: str
    def __init__(self) -> None: ...

class WshEventData(Object):
    conId: Incomplete
    filter: str
    fillWatchlist: bool
    fillPortfolio: bool
    fillCompetitors: bool
    startDate: str
    endDate: str
    totalLimit: Incomplete
    def __init__(self) -> None: ...

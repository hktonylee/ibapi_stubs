from _typeshed import Incomplete
from enum import Enum
from ibapi.const import UNSET_DECIMAL as UNSET_DECIMAL, UNSET_DOUBLE as UNSET_DOUBLE
from ibapi.object_implem import Object as Object
from ibapi.utils import decimalMaxString as decimalMaxString, floatMaxString as floatMaxString, intMaxString as intMaxString

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
    lastTradeDate: str
    strike: Incomplete
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
    description: str
    issuerId: str
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
    aggGroup: int
    underSymbol: str
    underSecType: str
    marketRuleIds: str
    secIdList: Incomplete
    realExpirationDate: str
    lastTradeTime: str
    stockType: str
    minSize: Incomplete
    sizeIncrement: Incomplete
    suggestedSizeIncrement: Incomplete
    minAlgoSize: Incomplete
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
    fundName: str
    fundFamily: str
    fundType: str
    fundFrontLoad: str
    fundBackLoad: str
    fundBackLoadTimeInterval: str
    fundManagementFee: str
    fundClosed: bool
    fundClosedForNewInvestors: bool
    fundClosedForNewMoney: bool
    fundNotifyAmount: str
    fundMinimumInitialPurchase: str
    fundSubsequentMinimumPurchase: str
    fundBlueSkyStates: str
    fundBlueSkyTerritories: str
    fundDistributionPolicyIndicator: Incomplete
    fundAssetType: Incomplete
    ineligibilityReasonList: Incomplete
    eventContract1: str
    eventContractDescription1: str
    eventContractDescription2: str
    def __init__(self) -> None: ...

class ContractDescription(Object):
    contract: Incomplete
    derivativeSecTypes: Incomplete
    def __init__(self) -> None: ...

class FundAssetType(Enum):
    NoneItem = ('None', 'None')
    Others = (('000', 'Others'),)
    MoneyMarket = ('001', 'Money Market')
    FixedIncome = ('002', 'Fixed Income')
    MultiAsset = ('003', 'Multi-asset')
    Equity = ('004', 'Equity')
    Sector = ('005', 'Sector')
    Guaranteed = ('006', 'Guaranteed')
    Alternative = ('007', 'Alternative')

class FundDistributionPolicyIndicator(Enum):
    NoneItem = ('None', 'None')
    AccumulationFund = ('N', 'Accumulation Fund')
    IncomeFund = ('Y', 'Income Fund')

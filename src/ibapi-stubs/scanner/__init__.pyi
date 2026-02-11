from _typeshed import Incomplete
from ibapi.const import UNSET_DOUBLE as UNSET_DOUBLE, UNSET_INTEGER as UNSET_INTEGER
from ibapi.object_implem import Object as Object

class ScanData(Object):
    contract: Incomplete
    rank: Incomplete
    distance: Incomplete
    benchmark: Incomplete
    projection: Incomplete
    legsStr: Incomplete
    marketName: Incomplete
    def __init__(self, contract=None, rank: int = 0, distance: str = '', benchmark: str = '', projection: str = '', legsStr: str = '', marketName: str = '') -> None: ...

NO_ROW_NUMBER_SPECIFIED: int

class ScannerSubscription(Object):
    numberOfRows: Incomplete
    instrument: str
    locationCode: str
    scanCode: str
    abovePrice: Incomplete
    belowPrice: Incomplete
    aboveVolume: Incomplete
    marketCapAbove: Incomplete
    marketCapBelow: Incomplete
    moodyRatingAbove: str
    moodyRatingBelow: str
    spRatingAbove: str
    spRatingBelow: str
    maturityDateAbove: str
    maturityDateBelow: str
    couponRateAbove: Incomplete
    couponRateBelow: Incomplete
    excludeConvertible: bool
    averageOptionVolumeAbove: Incomplete
    scannerSettingPairs: str
    stockTypeFilter: str
    def __init__(self) -> None: ...

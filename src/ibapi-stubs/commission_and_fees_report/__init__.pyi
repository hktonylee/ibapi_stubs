from ibapi.object_implem import Object as Object
from ibapi.utils import floatMaxString as floatMaxString, intMaxString as intMaxString

class CommissionAndFeesReport(Object):
    execId: str
    commissionAndFees: float
    currency: str
    realizedPNL: float
    yield_: float
    yieldRedemptionDate: int
    def __init__(self) -> None: ...

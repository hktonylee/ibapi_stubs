from ibapi.object_implem import Object as Object
from ibapi.utils import floatMaxString as floatMaxString, intMaxString as intMaxString

class CommissionReport(Object):
    execId: str
    commission: float
    currency: str
    realizedPNL: float
    yield_: float
    yieldRedemptionDate: int
    def __init__(self) -> None: ...

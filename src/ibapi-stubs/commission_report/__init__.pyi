from ibapi import utils as utils
from ibapi.object_implem import Object as Object

class CommissionReport(Object):
    execId: str
    commission: float
    currency: str
    realizedPNL: float
    yield_: float
    yieldRedemptionDate: int
    def __init__(self) -> None: ...

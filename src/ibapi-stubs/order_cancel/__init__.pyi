from _typeshed import Incomplete
from ibapi.const import UNSET_INTEGER as UNSET_INTEGER
from ibapi.object_implem import Object as Object
from ibapi.utils import intMaxString as intMaxString

class OrderCancel(Object):
    manualOrderCancelTime: str
    extOperator: str
    manualOrderIndicator: Incomplete
    def __init__(self) -> None: ...

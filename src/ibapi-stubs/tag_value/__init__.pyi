from _typeshed import Incomplete
from ibapi.object_implem import Object as Object

class TagValue(Object):
    tag: Incomplete
    value: Incomplete
    def __init__(self, tag: str = None, value: str = None) -> None: ...

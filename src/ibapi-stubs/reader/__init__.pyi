from _typeshed import Incomplete
from ibapi import comm as comm
from threading import Thread

logger: Incomplete

class EReader(Thread):
    conn: Incomplete
    msg_queue: Incomplete
    def __init__(self, conn, msg_queue) -> None: ...
    def run(self) -> None: ...

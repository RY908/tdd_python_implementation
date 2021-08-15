from __future__ import annotations
from .money import Money

class Dollar(Money):
    def __init__(self, amount: int, currency: str):
        super().__init__(amount, currency)
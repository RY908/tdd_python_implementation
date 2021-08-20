from __future__ import annotations
from .expression import Expression
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .money import Money
    from .total import Total

class Bank:
    def __init__(self):
        self._rates = dict()

    def reduce(self, source: Expression, to: str) -> Money:
        return source.reduce(self, to)

    def add_rate(self, from_currency: str, to_currency: str, rate: int):
        self._rates[(from_currency, to_currency)] =rate

    def rate(self, from_currency: str, to_currency: str) -> int: 
        if (from_currency == to_currency): return 1
        return self._rates[(from_currency, to_currency)]


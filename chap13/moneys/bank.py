from __future__ import annotations
from .expression import Expression
from .money import Money
from .total import Total

class Bank:
    def reduce(self, source: Expression, to: str) -> Money:
        return source.reduce(to)

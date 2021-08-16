from __future__ import annotations
from .money import Money

class Dollar(Money):
    def times(self, multiplier: int) -> Dollar:
        return Dollar(self.amount * multiplier)
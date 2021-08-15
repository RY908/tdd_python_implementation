from __future__ import annotations
from .money import Money

class Franc(Money):
    def __init__(self, amount: int, currency: str):
        super().__init__(amount, currency)
        
    def times(self, multiplier: int) -> Money:
        return Money.franc(self.amount * multiplier)
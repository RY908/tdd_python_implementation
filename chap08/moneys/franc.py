from __future__ import annotations
from .money import Money

class Franc(Money):
    def __init__(self, amount: int):
        self.amount = amount
        
    def times(self, multiplier: int) -> Money:
        return Franc(self.amount * multiplier)
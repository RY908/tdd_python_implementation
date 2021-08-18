from __future__ import annotations
from .money import Money
from .expression import Expression
from .bank import Bank

class Total(Expression):
    def __init__(self, augend: Money, added: Money):
        self.augend = augend
        self.added = added
    
    def reduce(self, bank: Bank, to: str) -> Money:
        amount = self.augend.amount + self.added.amount
        return Money(amount, to)
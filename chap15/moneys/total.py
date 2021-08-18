from __future__ import annotations
from .money import Money
from .expression import Expression
from .bank import Bank

class Total(Expression):
    def __init__(self, augend: Expression, added: Expression):
        self.augend = augend
        self.added = added
    
    def reduce(self, bank: Bank, to: str) -> Money:
        amount = self.augend.reduce(bank, to).amount + self.added.reduce(bank, to).amount
        return Money(amount, to)

    def plus(self, addend: Expression) -> Expression:
        pass
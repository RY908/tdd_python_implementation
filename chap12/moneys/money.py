from __future__ import annotations
from .expression import Expression

class Money(Expression):
    def __init__(self, amount: int, currency: str):
        self.amount = amount
        self._currency = currency

    def __eq__(self, other: Money) -> bool:
        return (self.amount == other.amount) and \
            (self._currency == other._currency)
    
    def __str__(self) -> str:
        return str(self.amount) + " " + self._currency

    def currency(self) -> str:
        return self._currency

    def times(self, multiplier: int) -> Money:
        return Money(self.amount * multiplier, self._currency)

    def plus(self, added: Money) -> Expression:
        return Money(self.amount + added.amount, self._currency)

    @staticmethod
    def dollar(amount: int) -> Money:
        return Money(amount, "USD")

    @staticmethod
    def franc(amount: int) -> Money:
        return Money(amount, "CHF")
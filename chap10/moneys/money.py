from __future__ import annotations
from abc import ABCMeta, abstractmethod

class Money():
    def __init__(self, amount: int, currency: str):
        self.amount = amount
        self._currency = currency

    def __eq__(self, other: Money) -> bool:
        return (self.amount == other.amount) and \
            (self._currency == other._currency)
    
    def __str__(self) -> str:
        return self.amount + " " + self.currency

    def currency(self) -> str:
        return self._currency

    def times(self, multiplier: int) -> Money:
        return Money(self.amount * multiplier, self._currency)

    @staticmethod
    def dollar(amount: int) -> Money:
        from .dollar import Dollar
        return Dollar(amount, "USD")

    @staticmethod
    def franc(amount: int) -> Money:
        from .franc import Franc
        return Franc(amount, "CHF")
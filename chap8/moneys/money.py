from __future__ import annotations
from abc import ABCMeta, abstractmethod

class Money(metaclass=ABCMeta):
    def __init__(self, amount: int):
        self.amount = amount

    def __eq__(self, other: Money) -> bool:
        return (self.amount == other.amount) and \
            (self.__class__.__name__ == other.__class__.__name__)

    @abstractmethod
    def times(self, multiplier: int) -> Money:
        pass

    @staticmethod
    def dollar(amount: int) -> Money:
        from .dollar import Dollar
        return Dollar(amount)

    @staticmethod
    def franc(amount: int) -> Money:
        from .franc import Franc
        return Franc(amount)
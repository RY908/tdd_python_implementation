from __future__ import annotations
from abc import ABCMeta, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .money import Money
    from .bank import Bank

class Expression(metaclass=ABCMeta):
    @abstractmethod
    def reduce(self, bank: Bank, to: str) -> Money:
        pass

    @abstractmethod
    def plus(self, added: Expression) -> Expression:
        pass

    @abstractmethod
    def times(self, multiplier: int) -> Expression:
        pass

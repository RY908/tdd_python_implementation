from __future__ import annotations
from abc import ABCMeta, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .money import Money

class Expression(metaclass=ABCMeta):
    @abstractmethod
    def reduce(self, to: str) -> Money:
        pass

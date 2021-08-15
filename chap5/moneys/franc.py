from __future__ import annotations

class Franc:
    def __init__(self, amount: int):
        self.amount = amount

    def __eq__(self, other: Franc) -> bool:
        return self.amount == other.amount

    def times(self, multiplier: int) -> Franc:
        return Franc(self.amount * multiplier)
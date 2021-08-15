from __future__ import annotations

class Dollar:
    def __init__(self, amount: int):
        self.amount = amount

    def __eq__(self, other: Dollar) -> bool:
        return self.amount == other.amount

    def times(self, multiplier: int) -> Dollar:
        return Dollar(self.amount * multiplier)
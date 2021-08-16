import sys
import pathlib
import unittest as ut

current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append( str(current_dir) + '/../' )

from moneys.money import Money
from moneys.expression import Expression
from moneys.bank import Bank
from moneys.total import Total

class MoneyTest(ut.TestCase):
    def test_multiplication(self):
        five: Money = Money.dollar(5)
        self.assertEqual(Money.dollar(10), five.times(2))
        self.assertEqual(Money.dollar(15), five.times(3))

    def test_equality(self):
        self.assertTrue(Money.dollar(5) == Money.dollar(5))
        self.assertFalse(Money.dollar(5) == Money.dollar(6))
        self.assertFalse(Money.dollar(5) == Money.franc(5))

    def test_currency(self):
        self.assertEqual("USD", Money.dollar(1).currency())
        self.assertEqual("CHF", Money.franc(1).currency())

    def test_simple_addition(self):
        five: Money = Money.dollar(5)
        total: Expression = five.plus(five)
        bank: Bank = Bank()
        reduced: Money = bank.reduce(total, "USD")
        self.assertEqual(Money.dollar(10), reduced)

    def test_plus_returns_total(self):
        five: Money = Money.dollar(5)
        result: Expression = five.plus(five)
        total: Total = result
        self.assertEqual(five, total.augend)
        self.assertEqual(five, total.added)

    def test_reduce_total(self):
        total: Expression = Total(Money.dollar(3), Money.dollar(4))
        bank: Bank = Bank()
        result: Money = bank.reduce(total, "USD")
        self.assertEqual(Money.dollar(7), result, "{} {}".format(Money.dollar(7), result))

    def test_reduce_money(self):
        bank: Bank = Bank()
        result: Money = bank.reduce(Money.dollar(1), "USD")
        self.assertEqual(Money.dollar(1), result, "{} {}".format(Money.dollar(1), result))

if __name__ == "__main__":
    ut.main()
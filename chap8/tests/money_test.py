import sys
import pathlib
import unittest as ut

current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append( str(current_dir) + '/../' )

from moneys.dollar import Dollar
from moneys.franc import Franc
from moneys.money import Money

class MoneyTest(ut.TestCase):
    def test_multiplication(self):
        five: Money = Money.dollar(5)
        self.assertEqual(Money.dollar(10), five.times(2), "amount expected 10")
        self.assertEqual(Money.dollar(15), five.times(3), "amount expected 15")

    def test_equality(self):
        self.assertTrue(Money.dollar(5) == Money.dollar(5))
        self.assertFalse(Money.dollar(5) == Money.dollar(6))
        self.assertTrue(Money.franc(5) == Money.franc(5))
        self.assertFalse(Money.franc(5) == Money.franc(6))
        self.assertFalse(Money.dollar(5) == Money.franc(5))

    def test_franc_multiplication(self):
        five: Money = Franc(5)
        self.assertEqual(Money.franc(10), five.times(2), "amount expected 10")
        self.assertEqual(Money.franc(15), five.times(3), "amount expected 15")


if __name__ == "__main__":
    ut.main()
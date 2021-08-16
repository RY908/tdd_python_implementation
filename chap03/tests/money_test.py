import sys
import pathlib
import unittest as ut

current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append( str(current_dir) + '/../' )

from moneys.dollar import Dollar

class MoneyTest(ut.TestCase):
    def test_multiplication(self):
        five = Dollar.Dollar(5)
        product = five.times(2)
        self.assertEqual(10, product.amount, "amount expected 10")
        product = five.times(3)
        self.assertEqual(15, product.amount, "amount expected 15")

    def test_equality(self):
        self.assertTrue(Dollar(5) == Dollar(5))
        self.assertFalse(Dollar(5) == Dollar(6))


if __name__ == "__main__":
    ut.main()
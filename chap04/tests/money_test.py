import sys
import pathlib
import unittest as ut

current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append( str(current_dir) + '/../' )

from moneys.dollar import Dollar

class MoneyTest(ut.TestCase):
    def test_multiplication(self):
        five = Dollar(5)
        self.assertEqual(Dollar(10), five.times(2), "amount expected 10")
        self.assertEqual(Dollar(15), five.times(3), "amount expected 15")

    def test_equality(self):
        self.assertTrue(Dollar(5) == Dollar(5))
        self.assertFalse(Dollar(5) == Dollar(6))


if __name__ == "__main__":
    ut.main()
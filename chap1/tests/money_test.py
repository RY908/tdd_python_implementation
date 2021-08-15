import sys
import pathlib
import unittest as ut

current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append( str(current_dir) + '/../' )

from moneys.dollar import Dollar

class MoneyTest(ut.TestCase):
    def test_multiplication(self):
        five = Dollar(5)
        five.times(2)
        self.assertEqual(10, five.amount, "amount expected 10")

if __name__ == "__main__":
    ut.main()
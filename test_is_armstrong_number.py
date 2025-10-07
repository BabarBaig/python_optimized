# test_is_armstrong_number.py
import unittest
from is_armstrong_number import is_armstrong_number

class TestArmstrongNumber(unittest.TestCase):

    def test_known_armstrong_numbers(self):
        self.assertTrue(is_armstrong_number(153))
        self.assertTrue(is_armstrong_number(370))
        self.assertTrue(is_armstrong_number(371))
        self.assertTrue(is_armstrong_number(407))

    def test_non_armstrong_numbers(self):
        self.assertFalse(is_armstrong_number(100))
        self.assertFalse(is_armstrong_number(200))
        self.assertFalse(is_armstrong_number(123))

    def test_single_digit_numbers(self):
        for i in range(10):
            with self.subTest(i=i):
                self.assertTrue(is_armstrong_number(i))

if __name__ == "__main__":
    unittest.main()

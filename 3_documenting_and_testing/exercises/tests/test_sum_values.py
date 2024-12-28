import unittest

from ..sum_values import sum_values

class TestSumValues(unittest.TestCase):
    """ """

    def test_minimal_input(self):
        """ It should return 0 """
        self.assertEqual(sum_values(0, 0), 0)
    
    def test_two_positive_num(self):
        """ It should return 4"""
        self.assertEqual(sum_values(2, 2), 4)

    def test_first_value_negative(self):
        """ It should return 1 """
        self.assertEqual(sum_values(-4, 5), 1)

    def test_second_value_negative(self):
        """ It should return -4 """
        self.assertEqual(sum_values(-7, 3), -4)

    def test_both_values_negative(self):
        """ It should return -10"""
        self.assertEqual(sum_values(-9, -1), -10)

    def test_both_strings(self):
        """ It should return goodbye """
        self.assertEqual(sum_values("good", "bye"), "goodbye")

    

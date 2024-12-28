# Run unittest python3 -m unittest path/to/file
import unittest

from ..add_two_values import add_two_values

class TestAddTwoValues(unittest.TestCase):
    """ Test the addition function """
    def test_1(self):
        actual = add_two_values(1,2)
        expected = 3
        self.assertEqual(actual,expected)

    def test_2(self):
        actual = add_two_values(3,4)
        expected = 7
        self.assertEqual(actual,expected)

    def test_3(self):
        actual = add_two_values(5,6)
        expected = 11
        self.assertEqual(actual,expected)

    def test_4(self):
        actual = add_two_values(-1,2)
        expected = 1
        self.assertEqual(actual,expected)

    def test_5(self):
        actual = add_two_values(-3,-4)
        expected = -7
        self.assertEqual(actual,expected)

    def test_1(self):
        actual = add_two_values(5,-6)
        expected = 1
        self.assertEqual(actual,expected)

#This should fail intentionally 
    def test_1(self):
        actual = add_two_values(0,1)
        expected = 1
        self.assertEqual(actual,expected)
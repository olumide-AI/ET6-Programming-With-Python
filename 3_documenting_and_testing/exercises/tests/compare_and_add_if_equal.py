# Run unittest python3 -m unittest path/to/file
import unittest

from ..compare_and_add_if_equal import compare_and_add_if_equal

class TestCompareAndAddIfEqual(unittest.TestCase):
    """ Test if the function to compare to values, to return the min value or the combined value"""
    def test_1(self):
        actual = compare_and_add_if_equal(2,4)
        expected = 2
        self.assertEqual(actual,expected)

    def test_2(self):
        actual = compare_and_add_if_equal(-1,-1)
        expected = -2
        self.assertEqual(actual,expected)

    def test_3(self):
        actual = compare_and_add_if_equal(4,2)
        expected = 2
        self.assertEqual(actual,expected)

    def test_4(self):
        actual = compare_and_add_if_equal(100,100.5)
        expected = 100
        self.assertEqual(actual,expected)

    def test_5(self):
        actual = compare_and_add_if_equal(0,0)
        expected = 0
        self.assertEqual(actual,expected)

    def test_6(self):
        actual = compare_and_add_if_equal(20,21)
        expected = 20
        self.assertEqual(actual,expected)
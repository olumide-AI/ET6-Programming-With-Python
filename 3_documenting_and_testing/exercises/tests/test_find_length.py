# Run unittest python3 -m unittest path/to/file
import unittest
import unittest

from ..find_length import find_length

class TestFindLength(unittest.TestCase):
    """ Test the len function to find input length"""
    def test_1(self):
        actual = find_length("Boeing")
        expected = 6
        self.assertEqual(actual,expected)

    def test_2(self):
        actual = find_length([3,4,7,8,1111,])
        expected = 5
        self.assertEqual(actual,expected)

    def test_3(self):
        actual = find_length({12345})
        expected = 1
        self.assertEqual(actual,expected)

    def test_4(self):
        actual = find_length("B2B")
        expected = 3
        self.assertEqual(actual,expected)

    def test_5(self):
        actual = find_length([3])
        expected = 1
        self.assertEqual(actual,expected)

    def test_6(self):
        actual = find_length({1,2,3})
        expected = 3
        self.assertEqual(actual,expected)
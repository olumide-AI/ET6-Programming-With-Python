# Run unittest python3 -m unittest path/to/file
import unittest
import unittest

from ..list_from_length import list_from_length

class TestListFromLength(unittest.TestCase):
    """Generates a new least using a starting point and a length given in the parameter """
    def test_1(self):
        actual = list_from_length(0,0)
        expected = []
        self.assertEqual(actual,expected)

    def test_2(self):
        actual = list_from_length(1,0)
        expected = [0]
        self.assertEqual(actual,expected)

    def test_3(self):
        actual = list_from_length(5,20)
        expected = [20, 21, 22, 23, 24]
        self.assertEqual(actual,expected)

    def test_4(self):
        actual = list_from_length(5,-2)
        expected = [-2, -1, 0, 1, 2]
        self.assertEqual(actual,expected)

    def test_5(self):
        actual = list_from_length(6,-4)
        expected = [-4, -3, -2, -1, 0, 1]
        self.assertEqual(actual,expected)

    def test_6(self):
        actual = list_from_length(2,100)
        expected = [100, 101]
        self.assertEqual(actual,expected)


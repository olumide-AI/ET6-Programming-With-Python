# Run unittest python3 -m unittest path/to/file
import unittest

from ..create_list import create_list

class TestCreateList(unittest.TestCase):
    """ To create a list of numbers form 0 to the (list_length -1) """
    def test_1(self):
        actual = create_list(0)
        expected = []
        self.assertEqual(actual,expected)

    def test_2(self):
        actual = create_list(1)
        expected = [0]
        self.assertEqual(actual,expected)

    def test_3(self):
        actual = create_list(2)
        expected = [0, 1]
        self.assertEqual(actual,expected)

    def test_4(self):
        actual = create_list(3)
        expected = [0, 1, 2]
        self.assertEqual(actual,expected)

    def test_5(self):
        actual = create_list(4)
        expected = [0, 1, 2, 3]
        self.assertEqual(actual,expected)

    def test_6(self):
        actual = create_list(5)
        expected = [0,1,2,3,4]
        self.assertEqual(actual,expected)

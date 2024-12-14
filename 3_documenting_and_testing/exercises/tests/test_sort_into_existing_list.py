# Run unittest python3 -m unittest path/to/file
import unittest

from ..sort_into_existing_list import sort_into_existing_list

class TestSortIntoExistingList(unittest.TestCase):
    """ Test the function to sort a list into another list in ascending order"""
    def test_1(self):
        actual = sort_into_existing_list([1, 2, 3], None)
        expected = [1, 2, 3]
        self.assertEqual(actual,expected)

    def test_2(self):
        actual = sort_into_existing_list(['z', 'c', 'v'], ['y'])
        expected = ['y', 'c', 'v', 'z']
        self.assertEqual(actual,expected)

    def test_3(self):
        actual = sort_into_existing_list([2, 1, 0], ['y'])
        expected = ['y', 0, 1, 2]
        self.assertEqual(actual,expected)

    def test_4(self):
        actual = sort_into_existing_list(['abba', 'baba', 'mama', 'dada'], ['baby_speech'])
        expected = ['baby_speech', 'abba', 'baba', 'dada', 'mama']
        self.assertEqual(actual,expected)

    def test_5(self):
        actual = sort_into_existing_list([3, 66, 45655, 0], [889, 2, 0])
        expected = [889, 2, 0, 0, 3, 66, 45655]
        self.assertEqual(actual,expected)

    def test_6(self):
        actual = sort_into_existing_list(['b', 'c', 'a'], None)
        expected = ['a', 'b', 'c']
        self.assertEqual(actual,expected)
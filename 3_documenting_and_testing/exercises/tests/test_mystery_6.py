import unittest

from ..mystery_6 import mystery_6

class TestMystery6(unittest.TestCase):
    """ """

    def test_minimal_input(self):
        """"""
        self.assertEqual(mystery_6(0, 0), [])
    
    def test_two_same_num(self):
        """"""
        self.assertEqual(mystery_6(1,1), [1])

    def test_two_diff_num(self):
        """"""
        self.assertEqual(mystery_6(1, 2), [2])

    def test_two_num_far_apart(self):
        """"""
        self.assertEqual(mystery_6(1, 4), [4])

    def test_change_first_value_to_not_one(self):
        """"""
        self.assertEqual(mystery_6(2, 4), [4, 5]) #[4,5]

    def test_with_a_diff_lower_bound(self):
        """"""
        self.assertEqual(mystery_6(2, 3), [3, 4])

    def test_diff_bounds(self):
        """"""
        self.assertEqual(mystery_6(3,4), [4, 5, 6])

    def test_if_a_can_be_a_float(self):
        """"""
        self.assertEqual(mystery_6(4.6, 4), [4, 5, 6, 7, 8])

    def test_second_value_as_float(self):
        """"""
        self.assertEqual(mystery_6(5, 2.45),[2.45, 3.45, 4.45, 5.45, 6.45])


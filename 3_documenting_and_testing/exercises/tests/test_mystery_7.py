# Run unittest python3 -m unittest path/to/file
import unittest

from ..mystery_7 import mystery_7

class TestMystery7(unittest.TestCase):
    """ """
    def test_minimal_input(self):
        """ """
        self.assertEqual(mystery_7('a','b'), [])
    
    def test_strings(self):
        """ """
        self.assertEqual(mystery_7('a1', '1'), ['1'])

    def test_reverse_string_and_num(self):
        """ """
        self.assertEqual(mystery_7('1', 'a1'), [])
    
    def test_more_string(self):
        """ """
        self.assertEqual(mystery_7('applesauce', 'a'), ['a', 'a'])

    def test_more_inputs(self):
        """ Can only be one letter at a time """
        self.assertEqual(mystery_7('applesauce', 'ap'), [])

    def test_value2_greater_than_value1(self):
        """ """
        self.assertEqual(mystery_7('apple', 'applesauce'), [])


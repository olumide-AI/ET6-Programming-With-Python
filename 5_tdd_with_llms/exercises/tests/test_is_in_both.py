#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for

Test categories:
   - Standard cases: Test normal input scenarios where the query string is found or not found.
  - Edge cases: Test unusual or extreme conditions, such as empty inputs or varying capitalizations.
  - Defensive tests: Validate behavior with invalid inputs, such as non-string elements or missing query strings.

Created on 2024-12-06
Author:Olumide Kolawole
"""

import unittest
from ..is_in_both import is_in_both


class TestIsInBoth(unittest.TestCase):
    """Test suite for the is_in_both function"""

    # Standard test cases
    def test_if_a_is_present_in_both_list(self):
        """Should return True if 'a' is in both lists."""
        self.assertEqual(is_in_both(["a", "b"], ["a", "c"], "a"), True)

    def test_if_joy_is_present_in_both_list(self):
        """Should return True if 'joy' is in both lists."""
        self.assertEqual(
            is_in_both(["boy", "joy", "toy"], ["zoo", "dog", "joy"], "joy"), True
        )

    def test_if_dog_is_present_in_both_list(self):
        """Should return False if 'dog' is only in one list."""
        self.assertEqual(is_in_both(["adam"], ["dog"], "dog"), False)

    def test_for_capital_letters_in_query_string(self):
        """Should return True regardless of capitalization."""
        self.assertEqual(
            is_in_both(["gym", "tim", "dear"], ["gym", "dim", "dear"], "DEAR"), True
        )

    def test_alphanumeric_string(self):
        """Should return True if the alphanumeric query string matches in both lists."""
        self.assertEqual(
            is_in_both(["11b1", "00gab"], ["11b1", "00gab"], "00gab"), True
        )

    # Defensive test cases
    def test_non_string_list(self):
        """Should raise a ValueError if lists contain non-string elements."""
        with self.assertRaises(ValueError):
            is_in_both([1, 2, 3], [2, 3, 4], "2")

    def test_query_string_as_int(self):
        """Should raise a ValueError if the query string is not a string."""
        with self.assertRaises(ValueError):
            is_in_both(["a", "b"], ["a", "c"], 12)

    # Edge cases
    def test_empty_list(self):
        """Should return False if both lists are empty."""
        self.assertEqual(is_in_both([], [], ""), False)

    def test_spaces_in_string(self):
        """Should return True if the query string with spaces matches."""
        self.assertEqual(is_in_both(["", "  ", "   "], ["   ", "     "], "   "), True)

    def test_only_one_empty_list(self):
        """Should return False if one list is empty."""
        self.assertEqual(is_in_both([], ["boy", "girls"], "jump"), False)

    def test_large_list(self):
        """Should return True for a valid query string in very large lists."""
        large_list = ["a"] * 10000
        self.assertEqual(is_in_both(large_list, large_list, "a"), True)


if __name__ == "__main__":
    unittest.main()

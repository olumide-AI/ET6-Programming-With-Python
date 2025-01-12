#!/usr/bin/env/python3
# -*- coding: utf-8 -*-
"""
Unittest module for is_in_one function.

Test Categories:
  - Standard cases: Common scenarios where the function is expected to work.
  - Edge cases: Handle unusual or extreme inputs, including empty and large inputs.
  - Defensive tests: Validate input types and error handling.

Created on 2025-01-12
Author: Olumide Kolawole
"""

import unittest
from ..is_in_one import is_in_one


class TestIsInOne(unittest.TestCase):
    """Unit test for the is_in_one function"""

    # Standard cases
    def test_base_case(self):
        """Test a typical case where query is in one list."""
        self.assertEqual(
            is_in_one(["boy", "bee", "buzz"], ["cat", "dog", "pig"], "boy"), True
        )

    def test_query_in_both_list(self):
        """Test case where query is in both lists."""
        self.assertEqual(is_in_one(["boy"], ["boy"], "boy"), False)

    def test_query_in_neither_list(self):
        """Test case where query is in neither list."""
        self.assertEqual(
            is_in_one(["apple", "orange"], ["banana", "grape"], "pear"), False
        )

    def test_query_in_one_list_only(self):
        """Test case where query is in only one list."""
        self.assertEqual(is_in_one(["cat", "dog"], ["bird", "fish"], "cat"), True)

    # Edge cases
    def test_repeated_string(self):
        """Test case with repeated strings in a list."""
        self.assertEqual(
            is_in_one(["boy", "boy", "guy"], ["girl", "lady"], "boy"), True
        )

    def test_empty_both_lists(self):
        """Test case with empty lists."""
        self.assertEqual(is_in_one([], [], "query"), False)

    def test_empty_lists(self):
        """Test case with one empty lists."""
        self.assertEqual(is_in_one([], ["a", "b"], "a"), True)

    def test_empty_query_string(self):
        """Test case with an empty query string."""
        self.assertEqual(is_in_one(["a", "b"], ["b", "c"], ""), False)

    def test_single_item_lists(self):
        """Test case with single-item lists."""
        self.assertEqual(is_in_one(["a"], ["b"], "a"), True)

    def test_case_insensitivity(self):
        """Test case-insensitive matching."""
        self.assertEqual(is_in_one(["Cat"], ["dog"], "cat"), True)

    # Defensive tests
    def test_invalid_list_inputs(self):
        """Test invalid input types for lists."""
        with self.assertRaises(TypeError):
            is_in_one("not_a_list", ["b", "c"], "a")
        with self.assertRaises(TypeError):
            is_in_one(["a", "b"], "not_a_list", "a")

    def test_invalid_query_string(self):
        """Test invalid input types for the query string."""
        with self.assertRaises(TypeError):
            is_in_one(["a", "b"], ["b", "c"], 123)
        with self.assertRaises(TypeError):
            is_in_one(["a", "b"], ["b", "c"], None)


if __name__ == "__main__":
    unittest.main()

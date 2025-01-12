#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Is in Both

This module defines a function `is_in_both` that checks if a query string
is present as an exact match in two lists of strings.

Functionality:
    - Takes in two lists of strings and a query string.
    - Returns True if the query string exists in both lists.
    - Case-insensitive: Comparisons are normalized to lowercase.

Example Usage:
    >>> is_in_both(["joy", "joy"], ["boy", "joy"], "joy")
    True
    >>> is_in_both(["girl", "sad"], ["sad", "bad"], "sad")
    True
    >>> is_in_both(["adam"], ["dog"], "dog")
    False

Pseudocode:
    Input: Two lists of strings (list_a, list_b), a query string (query_string)
    Process:
        1. Convert all strings to lowercase for case-insensitivity.
        2. Check if query_string exists in both lists.
    Output: Boolean (True if query_string is in both lists, False otherwise)

Author: Olumide Kolawole
Created: 2024-12-06
"""


def is_in_both(list_a: list, list_b: list, query_string: str) -> bool:
    """Generates true or false based on if the item in query_string
     are in list_ and list_b together
    Parameters: list_a (list), list_b (list), query_string (str)

    Returns -> bool

    >>> is_in_both(["joy", "joy"], ["boy", "joy"], "joy")
    True

    >>> is_in_both(["girl", "sad"], ["sad", "bad"], "sad")
    True

    >>> is_in_both(["adam"], ["dog"], "dog")
    False
    """
    # convert query_string to lowercase
    lower_query_string = query_string.lower()

    # convert the list to lowercase
    lowercase_list_a = [item.lower() for item in list_a]
    lowercase_list_b = [item.lower() for item in list_b]

    return (
        lower_query_string in lowercase_list_a
        and lower_query_string in lowercase_list_b
    )

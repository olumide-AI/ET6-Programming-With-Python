#!/usr/bin/env/python3
# -*- coding: utf-8 -*-
"""
A function for comparing a string with two lists
to determine if it is present in only one of the lists.

Module contents:
  - is_in_one: Takes in two list and a string and returns true if the string
  is only found in one of the list otherwise return false

Created on 2025-01-12
Author: Olumide kolawole

Write a function that takes in a string and two lists of strings.
It will return true if the item is in _only one_ of the lists.

"""


def is_in_one(list_a: list, list_b: list, query_string: str) -> bool:
    """Determine if the query string is in only one of the two lists.
    It has to be strings values in list and query_string must be a string
    If not it will raise an error for int or any other data type
    List could be any length

    Parameters:
      list_a (list): A list of string values.
      list_b (list): A list of string values.
      query_string: The string to search for.

    Returns: -> bool: True or False value

    Raises:
      AssertionError:
        - If input is not a list (TypeError)
        - If list doesn't contain strings (TypeError)

    Pseudocode:
    if query_string in list_a or query_string in list_b
    return True
    else
    return False

    Examples:
    >>> is_in_one(["boy", "bee", "buzz"], ["cat", "dog", "pig"], "boy")
    True
    >>> is_in_one([], ["joy","happy"], "happy")
    True
    >>> is_in_one(["tom, "david", "peter"], ["cam", "victor", "max"], "judy")
    False

    """
    # Validate input types
    if not isinstance(list_a, list):
        raise TypeError("list_a must be a list")
    if not isinstance(list_b, list):
        raise TypeError("list_b must be a list")
    if not isinstance(query_string, str):
        raise TypeError("query_string must be a string")

    # Firstly check if query_string is in each list individually
    # Creating new variable facilitate debugging
    in_list_a = query_string in list_a
    in_list_b = query_string in list_b

    if in_list_a and not in_list_b:
        return True
    elif not in_list_a and in_list_b:
        return True
    else:
        return False

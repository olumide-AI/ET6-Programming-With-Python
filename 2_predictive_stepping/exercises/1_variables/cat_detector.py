#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Variables: Cat Detector

Asks the use for the input "cat", throws an assertion error if the input is wrong

"""

maybe_cat = input('Enter "cat": ')

is_cat = maybe_cat == "cat"

assert is_cat, 'you should have entered "cat"'

print("thank you for the cat")

""" Started my breakpoint on line 10
Nothing changes in memory, you're prompted to input a something 
Whatever you input is now saved in memory under variable maybe_cat
is_cat = maybe_cat and if variable is == cat, its true and saves in memory
it runs the print statement and nothing changes in memory
If not it raises an assertion error and prints an assertion error

"""
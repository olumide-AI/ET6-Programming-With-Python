#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" For-in Strings

For-in strings can be used to iterate through each character in a string.

"""

to_reverse = input("Enter anything, this program will reverse it: ")

backwards = ""
for char in to_reverse:
    backwards = char + backwards

print("end of program")

# the code loops around the for loop until it runs through all the characters in input
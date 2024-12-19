#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" While Loops

While loops execute the same block of code as long as a condition is not met

"""

maybe_a_cat = "" #This is an initialization 

while maybe_a_cat.lower() != "cat": #i'm a little confused on this line 
    maybe_a_cat = input('Enter "cat": ')

print("Thank you for the cat.")

"""I get line 12 now so the .lower check that all letters are converted the lowercase
and if they're not equal to cat. The loop wil start again
"""
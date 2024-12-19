#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" String Operations

Python has features to help with lots of common string manipulations.
None of these operations modify the string they use as input!

"""

text = "Python"

# slicing single characters
sliced = text[0] #p
sliced = text[5] #n

# slicing substrings
sliced = text[0:5] #pytho
sliced = text[0:4] #pyth
sliced = text[0:3] #pyt
sliced = text[1:4] #yth
sliced = text[2:4] #th

# getting the length of a string
length = len(text) #6

# replacing substrings
replaced = text.replace("P", "Z") #Zython
replaced = text.replace("p", "z") #not sure what happened in this line 
replaced = text.replace("on", "agoras") #pythagoras

# setting strings to lower or upper case
upper = text.upper() #PYTHON
lower = text.lower() #python

# remove whitespace from the ends of a string
stripped = "  Python  ".strip()

print("end of script")

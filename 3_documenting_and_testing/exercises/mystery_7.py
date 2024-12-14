"""
An exercise for outputting an ordered list based on a given length and starting value.

Module contents:
    -  The function is a filter, checking the elements in 
    - a (probably a list, tuple)if they have the letter d
    - Then check if it has 
    -  If value_2 is greater than value_1, return value_2
    -  If both values are equal combine them 

Created on 12 14 24
@author: Evan Cole (instructor) + Olumide Kolawole (student)
"""
# --- my doctest --- #
#Solving mystery 7
#LOGIC
# This code will only work for ints not list, because we're using the len() function
#it checks the length list first, if 0 empty list created 
#If != 0, it creates a new list, starting empty and uses the length
#and a initial value already given to create the new list, 
# it does this one at a time until it matches the said length given

#I can run docstring using python3 -m pydoc path/to/file.py
# Run a doc test python3 -m doctest -v path/to/file.py

#QUESTIONS
def mystery_7(a, b):
    c = []
    for d in a: #finds what elements are "d" in a
        if b in d: 
            c.append(d)
    return c

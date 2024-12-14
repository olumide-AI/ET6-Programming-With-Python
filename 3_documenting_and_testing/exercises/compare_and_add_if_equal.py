"""
An exercise for outputting the length of a value.

Module contents:
    -  If value_1 is less than value_2, return value_1
    -  If value_2 is greater than value_1, return value_2
    -  If both values are equal combine them 

Created on 12 13 24
@author: Evan Cole (instructor) + Olumide Kolawole (student)
"""

# --- my doctest --- #
#Solving mystery 3
#LOGIC
# If value_1 is less than value_2, return value_1
# If value_2 is greater than value_1, return value_2
# If they both values are equals add them together 

#I can run docstring using python3 -m pydoc path/to/file.py
# Run a doc test python3 -m doctest -v path/to/file.py

#QUESTIONS
#If they're more than 2 value it should give a error 
#if the values are string it should give an error

def compare_and_add_if_equal(value_1, value_2):
    """Compare two values and returns the minimum value as output
    combine the two values, if values are equal (behavior of function)
    
    Parameters: (A little implementation)
    input_value: int value_1, int value_2

    this function will work for only numbers(int and float) using a comparison
    operator to find the minimum values of the input,  
    
    Returns -> it will return the combination of the inputted values if they
    are equal, and return the minimum of the two values if they're different 

    Some examples

    >>> compare_and_add_if_equal(1,2)
    1

    >>> compare_and_add_if_equal(6,6)
    12

    >>> compare_and_add_if_equal(10,9)
    9
    
    """

    #return's the smallest value during comparison
    #if value_1 != value_2
    #return min(value_1 & value_2)
    if value_1 < value_2:
        return value_1
    elif value_1 > value_2:
        return value_2
    #returns a combination of both value when value_1 = value_2
    else:
        return value_1 + value_2

"""
An exercise for an addition function.

Module contents:
    - A function that adds two value(int)
    -I would love to test it out with string 

Created on 12 12 24
@author: Evan Cole (instructor) + Olumide Kolawole (student)
"""

# --- my doctest --- #
#Solving mystery 1
#This a function that takes in two values 
# I used value instead of a & b like the example said 
#Mostly because i would like to take this code above solving for numbers
#And returns the sum of the values s
#I can run docstring using python3 -m pydoc path/to/file.py
# Run a doc test python3 -m doctest -v path/to/file.py

def add_two_values(value_1,value_2):
    """Generating a sum of two values (behavior of function)
    
    Parameters: (A little implementation)
    value_1 = int, float
    value_2 = int, float
    this function will assume a & b are numbers(int)
    but we can also add two stings?
    but not two different data types like string and int
    
    Returns -> int value_1 + value_2 or str value_1 + value_2
    
    Some examples

    >>> add_two_values(1,2)
    3

    >>> add_two_values(3,4)
    7

    >>> add_two_values(5,6)
    11
    
    """
    # a & b should be int or float fot this test case to work 
    #assert isinstance (value_1, int)
   # assert isinstance (value_2, int)

    return value_1 + value_2 

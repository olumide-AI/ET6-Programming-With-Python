"""
An exercise for outputting the length of a value.

Module contents:
    - Given the list length
    - Generate a number from 0 to (list_length -1)
    - so 5 will give us [0,1,2,3,4]
    - We can change the initialization to anything and it will start from the initial number

Created on 12 13 24
@author: Evan Cole (instructor) + Olumide Kolawole (student)
"""

# --- my doctest --- #
#Solving mystery 4

#LOGIC
# We're working with 3 values
# c is a starting variable 0, and a counter for the number based on the input_number/desired list length
# a is the given list length = "list_length"
# b is an empty list, to create a "new list" based on the input a 
# uses a while loop, we always start with an empty list b =[]
# c is an initialization, starting the count like a For loop in c++ for i = 0; i > 0; i++
#This function only works on numbers


#I can run docstring using python3 -m pydoc path/to/file.py
# Run a doc test python3 -m doctest -v path/to/file.py

#QUESTIONS


def create_list(list_length):
    """ Generates a list based on a given number (behavior of function)
    
    Parameters: (A little implementation)
    input_value: list_length

    this function will work for only numbers(int and float)
    
    Returns -> a list count of a list of integers from 0 to (list_length - 1) 

    Some examples

    >>> create_list(0)
    []

    >>> create_list(1)
    [0]

    >>> create_list(2)
    [0, 1]
    
    """
    new_list = []

    list_count = 0 #current list count
    while len(new_list) < list_length:
        new_list.append(list_count)
        list_count = list_count + 1 #updating the list count by 1 until it matches length of a

    return new_list

"""
An exercise for outputting an ordered list based on a given length and starting value.

Module contents:
    -  If list_length = 0; return empty string 
    - If list_length < 0; Type error 
    - If list_length > 0; creates a new list and run the while loop
    -based on the initial value, the value becomes the starting point 
    - and a sequential length is created based on the list_length

Created on 12 14 24
@author: Evan Cole (instructor) + Olumide Kolawole (student)
"""

# --- my doctest --- #
#Solving mystery 6
#LOGIC
# This code will only work for ints not list, because we're using the len() function
#it checks the length list first, if 0 empty list created 
#If != 0, it creates a new list, starting empty and uses the length
#and a initial value already given to create the new list, 
# it does this one at a time until it matches the said length given

#I can run docstring using python3 -m pydoc path/to/file.py
# Run a doc test python3 -m doctest -v path/to/file.py

#QUESTIONS

def list_from_length(list_length, initial_value):
    """Creates a Sequential list from the list_length
    and passes it onto a new list that matches the length 
    using the initial_value. If the list_length = 0; 
    it won't generate any list (behavior of function)
    
    Parameters: (A little implementation)
    input_value: int list_length, int initial_value

    this function will work for only numbers(int) 

    Returns -> it returns a new list starting at thr initial value
    using the length to judge
    Some examples

    >>> list_from_length(0,5)
    []

    >>> list_from_length(2,6)
    [6, 7]

    >>> list_from_length(1,3)
    [3]
      
    """

    if list_length == 0:
        return []

    new_list = []
    while len(new_list) < list_length: #suggest we're working with int
        new_list.append(initial_value)
        initial_value = initial_value + 1 #suggest we're working with int

    return new_list

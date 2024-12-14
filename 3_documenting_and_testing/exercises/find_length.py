"""
An exercise for outputting the length of a value.

Module contents:
    - if the length of value = 0; return None
    -if length != 0 return length using len function

Created on 12 13 24
@author: Evan Cole (instructor) + Olumide Kolawole (student)
"""

# --- my doctest --- #
#Solving mystery 2
#To my understanding this function finds the length of a value using len()
#If length = 0, no length 
# If length != 0, output the length  
#I can run docstring using python3 -m pydoc path/to/file.py
# Run a doc test python3 -m doctest -v path/to/file.py

#QUESTIONS
#I believe i understand the function but running the file isn't doing anything?
#I tried to use help() to find more on the len function but it didn't work
#Can i find length of negative numbers
#I learnt len can't run integers

def find_length(input_value):
    """Generating the length of an input function (behavior of function)
    
    Parameters: (A little implementation)
    input_value: the value

    this function will assume find the length of any value of string, list, tuples 
    
    Returns -> the number of individual character/elements in thr input_value, None if the input is empty
    Some examples

    >>> find_length("joy")
    3

    >>> find_length([1,2,3,4])
    4

    >>> find_length("joy2theworld")
    12
    
    # should output nothing
    >>> find_length("")
    
    
    """
    if len(input_value) == 0:
        return None
    
    return len(input_value)
        

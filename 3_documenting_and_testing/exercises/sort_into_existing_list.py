"""
An exercise for sorting the first list into another list in ascending order.

Module contents:
    - If the list_2=None; list_2 starts as an empty list and just return values in list_1 in ascending order
    - If list_2 has values, the elements in list_1 just just added to list_2 in that same way.

Created on 12 14 24
@author: Evan Cole (instructor) + Olumide Kolawole (student)
"""

# --- my doctest --- #
#Solving mystery 5
#To my understanding this function sorts the elements
# in list_1 in ascending order and adds them to list_2
#It first check if list_2 has elements, if list_2 is none, list_2 starts of empty
#It then collects the values in list_1 and stores the min vales in a temp_variable
#It removes that min value element in list_1 and adds it to list_2
#It does that until all the values and elements have been copied to list_2 from list_1
#It should work for numbers, letters, and strings. Mixed type will give an error
#I can run docstring using python3 -m pydoc path/to/file.py
# Run a doc test python3 -m doctest -v path/to/file.py

#QUESTIONS
#Should i put None in [] or leave it as it is 
#Can "" work or it as to be '', what of if you mix and match quotation marks

def sort_into_existing_list(list_1, list_2=None):
    """Generating the minimum elements in list_1 and appending them to list_2 (behavior of function)
    
    Parameters: (A little implementation)
    input_value: list_1, list_2

    this function will work for any num, stings, and char. But not a mix of them 
    
    Returns -> list_2 should be list_2 + (content in list_1 in an ascending order)
    Some examples

    >>> sort_into_existing_list([7, 4, 5], None)
    [4, 5, 7]
    

    >>> sort_into_existing_list(['z', 't', 'a', 'v'], None)
    ['a', 't', 'v', 'z']

    >>> sort_into_existing_list(['dog', 'apple', 'cattle'], ['animals'])
    ['animals', 'apple', 'cattle', 'dog']
    

    
    
    """    
    if list_2 is None:
        list_2 = []
    while list_1:
        min_value = min(list_1)
        list_1.remove(min_value)
        list_2.append(min_value)
    return list_2

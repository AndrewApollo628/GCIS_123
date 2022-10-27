"""
Various useful array utilities. Provided for use on the homework in this unit.

@author GCCIS Faculty

additions made by 
Andrew Apollo 
"""

import arrays
import random


def range_array(start, stop, step=1):
    a_range = range(start, stop, step)
    length = len(a_range)
    an_array = arrays.Array(length, 0)
    for index in range(length):
        an_array[index] = a_range[index]
    return an_array

def random_array(size, min_value=0, max_value=None):
    an_array = arrays.Array(size, 0)
    if max_value is None:
        max_value = size

    for index in range(size):
        an_array[index] = random.randint(min_value, max_value)
    
    return an_array

def cat_array(array1, array2):
    new_array = arrays.Array (len (array1) + len (array2))
    for i in range (len (array1)):
        new_array [i] = array1[i]
    for i in range (len (array1), len (new_array)):
        new_array [i] = array2 [i - len(array1)]
    return new_array

def increasing_comparator(a,b): #Added from searches.py 
    return a <= b

def decreasing_comparator(a,b): #Added from searches.py 
    return a>=b

def is_sorted(an_array, comparator = increasing_comparator):
    '''
    This function will
        - Check to see if the array is sorted using comparaters 
    
    Paramaters 
        - an_array: Array being passed in 
        - comparator: comparator being used 
    '''
    
    if comparator == increasing_comparator:
        for index in range(0, len(an_array)):
            if comparator(an_array[index] , an_array[index-1]) == False:
                return False
        return True

    if comparator == decreasing_comparator:
        for index in range(0 , len(an_array) - 1 ):
            if comparator(an_array[index -3 ] , an_array[index -2 ]) == False:
                return False
        return True


def main():
    '''
    random.seed(1)
    rand_array = random_array(10)
    print(rand_array)
    '''
    array1 = [20, 10, 30]
    array2 = [30, 20, 10]
    print(is_sorted(array1))
    print(is_sorted(array1, decreasing_comparator))
    print(is_sorted(array2, increasing_comparator))
    print(is_sorted(array2, decreasing_comparator))

if __name__ == "__main__":
    main()
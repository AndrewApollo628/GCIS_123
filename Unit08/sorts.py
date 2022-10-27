"""
Implementations of the insertion sort algorithm. Provided for use in the 
homework for this unit.

@author GCCIS Faculty.
"""

import array_utils

def swap(an_array, a, b):
    temp = an_array[a]
    an_array[a] = an_array[b]
    an_array[b] = temp

def shift(an_array, comparator , index = 0):
    
    
    while index > 0 and comparator(an_array[index] , an_array[index-1]):
        swap(an_array, index, index-1)
        index -= 1
        
    '''
    while index > 0 and an_array[index] < an_array[index-1]:
        swap(an_array, index, index-1)
        index -= 1
    '''
def insertion_sort(an_array , comparator = array_utils.increasing_comparator ):
    '''
    This function
        - Takes in an array 
        - Comapres the value of the array 
    
    Paramaters
        - an_array: array being passed in 
        - comparator= array_utils.increasing_comparator: compariter function from array utils
    '''
    
    for index in range(1, len(an_array)):
        shift(an_array, comparator , index)
        
   
    '''
    for index in range(1, len(an_array)):
        shift(an_array, index)
    '''

def shift_wo_swap(an_array, index):
    target = an_array[index]
    target_index = index
    while target_index > 0 and target < an_array[target_index-1]:
        an_array[target_index] = an_array[target_index - 1]
        target_index -= 1
    an_array[target_index] = target

'''
def insertion_sort(an_array):
    for index in range(1, len(an_array)):
        shift(an_array, index)
'''
def insertion_sort_wo_swap(an_array):
    for index in range(1, len(an_array)):
        shift_wo_swap(an_array, index)

def main():
    an_array2 = [1 , 4 , 6 , 2 , 7 , 3]
    print(an_array2)
    insertion_sort(an_array2)
    

if __name__ == "__main__":
    main()

def test_insertion_sort():
    an_array2 = [1 , 4 , 2 ]
    insertion_sort(an_array2)
    assert an_array2 == [1 , 2 , 4 ]
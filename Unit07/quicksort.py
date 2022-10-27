'''
Author: Andrew Apollo

This program will 
    - Create a quicksort function 
    - create a quicksort mid function 
    - create a partition function
    - create a quick inertion sort function 
'''

import arrays 
import array_utils
import random
import sorts

#Class activity 7.3.3
def quicksort(an_array):
    if len(an_array) < 2:
        return an_array
#Class activity 7.3.5 add on
    else:
        pivot = an_array[0]
        less, same, more = partition(pivot, an_array)
        new_array = array_utils.cat_array(quicksort(less), same)
        new_array = array_utils.cat_array(new_array, quicksort(more))
        return new_array

#Class activity 7.3.10
def quicksort_mid(an_array):
    if len(an_array) < 2:
        return an_array

    else:
        pivot = an_array[(len(an_array)//2)]
        less, same, more = partition(pivot, an_array)
        new_array = array_utils.cat_array(quicksort_mid(less), same)
        new_array = array_utils.cat_array(new_array, quicksort_mid(more))
        return new_array

#class Activity 7.3.8
def partition(pivot, an_array):
    length = len(an_array)
    less_count = 0 
    same_count = 0
    more_count = 0
    for index in range(length):
        value = an_array[index]
        if value < pivot:
            less_count += 1
        elif value > pivot:
            more_count += 1
        else:
            same_count += 1

    less = arrays.Array(less_count)
    same = arrays.Array(same_count)
    more = arrays.Array(more_count)

    less_index = 0
    same_index = 0 
    more_index = 0

    for index in range(length):
        value = an_array[index]
        if value < pivot:
            less[less_index] = value
            less_index += 1
        elif value > pivot:
            more[more_index] = value
            more_index += 1
        else:
            same[same_index] = value
            same_index +=1 

    return less, same , more 

def quick_insertion_sort(an_array):
    '''
    This function will
        - Take in an array and compare the lengths to see what sort to use 
        - if the array is less than 2 it will resturn the array 
        - if no values are in less or more arrays than the function will do an insertion sort 
        - if other staements are false it will do a quicksort

    Paramaters
        - an_array: the array being passed in 
    
    '''
    if len(an_array) < 2:
        return an_array
        
    pivot = an_array[0]
    less, same, more = partition(pivot, an_array)
    if len(less) < 1 or len(more) < 1: 
        new_array = sorts.insertion_sort(an_array)
        return new_array
    else:
        new_array = array_utils.cat_array(quicksort_mid(less), same)
        new_array = array_utils.cat_array(new_array, quicksort_mid(more))
        return new_array

def main():
    
    #an_array = arrays.Array(1,1)
    #print(quicksort(an_array))
    
    #Class activity 7.3.8 tests 
    an_array = arrays.Array(10)
    '''
    unsorted 
    an_array[0] = 10
    an_array[1] = 2
    an_array[2] = 4
    an_array[3] = 7
    an_array[4] = 12
    an_array[5] = 1
    an_array[6] = 3
    an_array[7] = 13
    an_array[8] = 5
    an_array[9] = 6
    print(an_array)
    '''
    #sorted array 
    an_array[0] = 1
    an_array[1] = 2
    an_array[2] = 3
    an_array[3] = 4
    an_array[4] = 5
    an_array[5] = 6
    an_array[6] = 7
    an_array[7] = 8
    an_array[8] = 9
    an_array[9] = 10
    print(an_array)
    #print(partition(10 , an_array))
    
    print(quick_insertion_sort(an_array))
main()


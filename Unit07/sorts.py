#Author: Andrew Apollo

import array
import array_utils 
import merge_sort

#Class activity 7.1.2
def swap(an_array, a ,b):
    temp = an_array[a]
    an_array[a] = an_array[b]
    an_array[b] = temp

#Class activity 7.1.3
def shift(an_array , index):
    while index > 0 and an_array[index] < an_array[index -1]:
        swap(an_array, index, index-1)
        index-=1

#Class activity 7.1.4
def insertion_sort(an_array):
    for index in range(1, len(an_array)):
        shift(an_array , index)
        return an_array
        
        
        
'''

def insertion_sort_backwards(an_array):
    n = 0 
    unsorted = (an_array[0:3])
    sorted = (an_array[3:5])
    while (len(sorted[n]) > len(sorted(n+1))):
        swap(sorted, n , n+1)
    print(unsorted)
    print(sorted)
    #sorted = 
    
    for index in range(1, len(an_array)):
        shift(an_array , index)
    '''
#Class activity 7.1.5
def shift_wo_swap(an_array, index):
    target = an_array[index]
    target_index = index
    while target_index > 0 and target < an_array[target_index-1]:
        an_array[target_index] = an_array[target_index - 1]
        target_index -=1 
    an_array[target_index] = target

#Class activity 7.1.6
def insertion_sort_wo_swap(an_array):
    for index in range(1, len(an_array)):
        shift_wo_swap(an_array,index)

def main():
    #array1 = array_utils.random_array(10,1)
    
    #insertion_sort_wo_swap(array1)
    array = [5,3,7,4,1]
    print(array)
    print(insertion_sort(array))
    #insertion_sort_backwards(array)
    
main()
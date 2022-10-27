#Author: Andrew Apollo

import arrays
import array_utils

def linear_search(an_array , target):

    for index in range(len(an_array)):
        if an_array[index] == target:
            return index 
    return None

#Class activity 6.3.6
def binary_search(an_array , target , start=None , end=None):
    if start is None:
        start = 0
    if end == None:
        end = len(an_array) - 1
    if start > end:
        return None
    else:
        mid = (start + end) // 2
        if an_array[mid] == target:
            return mid 
        elif an_array[mid] < target:
            start = mid + 1 
            return binary_search(an_array, target, start, end)
        else:
            end = mid - 1
            return binary_search(an_array, target, start, end)

def main():
    '''
    an_array = arrays.Array(101, 0)
    for i in range(1,101):
        an_array[i]=i

    print("Found 1 at index" , linear_search(an_array, 1))
    print("Found 50 at index" , linear_search(an_array, 50))
    print("Found 100 at index" , linear_search(an_array, 100))
    print("Found 101 at index" , linear_search(an_array, 101))
    '''

    an_array = array_utils.range_array(1, 10000001)
    print(binary_search(an_array , 1))
    print(binary_search(an_array , 5000000))
    print(binary_search(an_array , 10000000))
    print(binary_search(an_array , 0))

if __name__ == "__main__":
    main()
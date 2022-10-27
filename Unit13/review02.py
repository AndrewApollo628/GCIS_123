#Author: Andrew Apollo

#Import 
import arrays
import array_utils

#Activity 13.2.2
def is_power(a , b):
    if a == 1:
        return True
    elif a % b == 0:
        return is_power(a/b, b)
    else: 
        return False

#Activity 13.2.3
def what_power(a, b, x = 0):
    if a == 1:
        return x
    elif a % b == 0:
        return what_power(a/b, b, x + 1)
    else: 
        raise ValueError("a is not a power of b")

#Activity 13.2.4
def fill_array(an_array, start=0, step=1, index=0):
    if index >= len(an_array):
        return
    else:
        an_array[index] = start
        fill_array(an_array, start+step, step, index+1)

#Activity 13.2.5
def arrays_equal(a_array, b_array, index=0):
    if index == len(a_array):
        return index == len(b_array)
    elif index == len(b_array):
        return False
    elif a_array[index] == b_array[index]:
        return arrays_equal(a_array, b_array, index+1)
    else:
        return False

#Activity 13.2.6
'''
Algorithim             best       worst      expected
Linear search:        O(1)       O(n)       O(n)
Binary search:        O(1)       O(logn)    O(logn)
Insertion Sort:       O(n)       O(n^2)     O(n^2)
merge sort:           O(nlogn)   O(nlogn)   O(nlogn)
quicksort:            O(nlogn)   O(n^2)     O(n^2)
'''

#Activity 13.2.7
def tuplify():
    first = input("Enter your first name: ")
    middle = input("Enter your middle name: ")
    last = input("Enter your last name: ")

    if middle == "":
        return (first, last)
    else:
        return (first, middle, last)

#Activity 13.2.8
def cubed(a_list):
    for index in range(len(a_list)):
        a_list[index] = a_list[index] ** 3

#Activity 13.2.9
def reversal(a_list):
    backward = []
    index = len(a_list) - 1
    while index >= 0:
        backward.append(a_list[index])
        index -= 1
    return backward

#Activity 13.2.10
def multiples(rows, col):
    table = []
    for row in range(1, rows+1):
        table_row = []
        table.append(table_row)
        for colum in range(1, col+1):
            product = row * col
            table_row.append(product)

    return table

#Activity 13.2.15
'''
I was not happy with prac 2 grades 
I would like to get a great grade to finsih strong 

I did do the study guide and played around with the questions after 
I dont plan to try anything new 
I have an idea on both the practicum and written parts 

'''

def main():
    '''
    #Activity 13.2.2 main
    print("is_power(25, 5) = ", is_power(25, 5))
    print("is_power(27, 3) = ", is_power(27, 3))
    print("is_power(30, 3) = ", is_power(30, 3))
    print("is_power(128, 2) = ", is_power(128, 2))

    #Activity 13.2.3 main
    print("what_power(25, 5) = ", what_power(25, 5))
    print("what_power(27, 3) = ", what_power(27, 3))
    print("what_power(128, 2) = ", what_power(128, 2))
    print("what_power(30, 3) = ", what_power(30, 3))
    
    #Activity 13.2.4 main
    an_array = arrays.Array(10)
    fill_array(an_array)
    print(an_array)
    fill_array(an_array, 1, 3)
    print(an_array)
    
    #Activity 13.2.5 main
    a_array  = array_utils.range_array(1,11)
    b_array  = array_utils.range_array(1,11)
    c_array  = array_utils.range_array(1,12)
    print("a_array == b_array: ", arrays_equal(a_array, b_array))
    print("a_array == c_array: ", arrays_equal(a_array, c_array))
    print("b_array == c_array: ", arrays_equal(b_array, c_array))
    
    #Activity 13.2.7 main
    print(tuplify())
    
    #Activity 13.2.8 main
    new_list = [1,2,3]
    cubed(new_list)
    print(new_list)
    
    #Activity 13.2.9 main
    new_list = [1,2,3]
    print(new_list)
    print(reversal(new_list))
    print(new_list)
    '''
    #Activity 13.2.10 main
    new_table = multiples(5,7)
    for row in new_table:
        print(row)


if __name__ == "__main__":
    main()


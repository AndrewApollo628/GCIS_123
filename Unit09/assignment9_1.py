'''
Author: Andrew Apollo 

This program will
    - Reverse a list 

'''
def in_place_reverse(a_list):
    '''
    This function will
        - Take a list in 
        - reverse the list indencies  

    Paramaters
        - a_list: list being passed in
    '''
    for i in range(len(a_list)):
        p = a_list.pop()
        a_list.insert(i , p)

    return a_list

def my_slice(a_list, start, stop, step = 1):
    '''
    This function will
        - Slice a string with the givin values passed into the function

    Paramaters
        - a_list: List being passed in
        - start: start of the slice
        - stop: end of the slice
        - step: step of each slice 
    '''
    return a_list[start:stop:step]

def make_multiplication_table():
    '''
    This function will
        - prints a 10x10 multiplication table 
    '''
    for row in range(1, 10 + 1):
        for col in range(1, 10 + 1):
            print(row*col, end= ' ')
        print()

def main():

    '''
    Test for Part 1 
    a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(in_place_reverse(a_list))
    
    #Tests for my_slice
    a_list = [0, 10, 20, 30, 40, 50]
    print(my_slice(a_list, 2, 4))
    print(my_slice(a_list, 1, 8, 2))
    print(my_slice(a_list, 5, 1, -1))
    '''
    #test 3 
    make_multiplication_table()


main()
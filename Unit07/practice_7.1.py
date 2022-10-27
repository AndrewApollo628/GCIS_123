'''
Author: Andrew Apollo 

This program will
    - Recursivly seach by incrementing index between calls then returns the target found at 
'''
#Import statements 
import arrays

def linear_recursive(arr, i, target):
    '''
    This function will
        - Search an array for the target
        - IF target is found will return teh index at which it was found 
        - If target is not found it will return none 

    Paramaters
        - arr: Array that will be searched 
        - i: index of the array 
        - traget: target value 
    '''
    for i in range(len(arr)): 
        if arr[i] == target:
            return i
    return None

def count_vowels(s, index):
    '''
    This function will
        - Take in a string and see how many vowels are in the string

    Paramaters:
        - s: String being passed in 
        - index: keeps count of how amny vowels are in the string
    '''
    
    for char in s:
        if char == "a":
            index +=1 
        elif char == "e":
            index +=1 
        elif char == "i":
            index +=1 
        elif char == "o":
            index +=1 
        elif char == "u":
            index +=1 
            
    print("Number of vowels " , index)
def main():
    '''
    # Test for activity 1
    a = arrays.Array(5, 0)
    res  = linear_recursive(a,0,4)
    print(res)
    a[3] = 4
    res = linear_recursive(a,0,4)
    print(res)
    '''
    #Tests for activity 2 
    count_vowels("code commentary is useful" , index=0)
    count_vowels("thr3 b33 n0 vwls h33r3" , index=0)
    count_vowels("" , index=0)
    count_vowels("u" , index=0)

main()
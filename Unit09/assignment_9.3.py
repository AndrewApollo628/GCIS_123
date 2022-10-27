'''
Author: Andrew Apollo

This program will
    - 

'''
#Import Statements 
import time

#Copied from Class activty 9.3.5
def make_myset(capasity, hash_func = hash):
    table = [[] for _ in range(capasity)]
    return (hash_func, table)

#Copied from Class activty 9.3.6
def add(mystet , element):
    hash_func = mystet[0]
    table = mystet[1]
    capasity = len(table)
    index = hash_func(element)%capasity
    row = table[index]
    for entry in row:
        if entry == element:
            return
    table[index].append(element)

def hash_bad(a_string):
    '''
    This Function will
        - Take in a string 
        - get each characters ASCii value 
        - return the total ascii value   

    Paramaters
        - a_string: string being passed in   
    '''
    total_ascii = 0 
    for char in a_string:
        char_ascii = ord(char)
        total_ascii += char_ascii

    return total_ascii

def hash_good(a_string):
    '''
    This function will 
        - Take in a string 
        - get each characters ASCii value 
        - mulitple the value by 31 ^ index
        - return the total ascii value

    Paramaters
        - a_string: string being passed in  
    '''
    length = len(a_string) - 1
    index = length 
    total_ascii = 0 
    for char in a_string:
        char_ascii = ord(char)
        total_ascii += char_ascii * 31 **(index)
        index -= 1
        
    return total_ascii

def read_data(hash_func):
    '''
    Thid function will 
        - create a set 
        - opens words.txt and adds it to the set 
        - then returns the set

    Paramaters 
        - hash_func: hash function being passed in 
    '''
    filename = 'data/words.txt'
    data_set =  make_myset(466547 , hash_func)
    
    with open(filename) as file:
        for line in file:
            line = line.strip()
            line_low = line.lower()
            add(data_set , line_low)
            
    return data_set
    
def quality_hash_function(myset):
    '''
    This function will
        - take in a set of data 
        - print the hash function
        - find the number of empty sets and max collisons 
        - return the number of empty sets and max collisons

    Paramaters
        - myset: set being passed in
    '''

    hashfunc , data_set = myset
    print("The quality of", hashfunc.__name__)
    empty_sets = 0 
    max_collisons = 0 

    for line in data_set:
        if len(line) == 0:
            empty_sets += 1
        elif len(line) > max_collisons:
            max_collisons = len(line) - 1 

    return max_collisons , empty_sets
         
def main():

    #Hash main call
    start = time.perf_counter()
    myset = read_data(hash)
    end = time.perf_counter()
    max_collisons , empty_rows = quality_hash_function(myset)
    print("maximum collisions:", max_collisons)
    print("number of empty slots:", empty_rows)
    print("Elapsed time to build a set:", round(end-start, 2), "seconds")
    print()

    #Hash_bad main call
    start = time.perf_counter()
    myset = read_data(hash_bad)
    end = time.perf_counter()
    max_collisons , empty_rows = quality_hash_function(myset)
    print("maximum collisions:", max_collisons)
    print("number of empty slots:", empty_rows)
    print("Elapsed time to build a set:", round(end-start, 2), "seconds")
    print()

    #Hash_good main call
    start = time.perf_counter()
    myset = read_data(hash_good)
    end = time.perf_counter()
    max_collisons , empty_rows = quality_hash_function(myset)
    print("maximum collisions:", max_collisons)
    print("number of empty slots:", empty_rows)
    print("Elapsed time to build a set:", round(end-start, 2), "seconds")
    print()

main()
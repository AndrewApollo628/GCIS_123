#Author: Andrew Apollo 

#Import Statements
import arrays
import time
import random 
import math
import re

#Class activity 9.1.2
def unique_array(an_array , value):
    for index in range(len(an_array)):
        current = an_array[index]
        if current == None:
            an_array[index] = value
            break
        elif current == value:
            return

def fill_array(length):
    an_array = arrays.Array(length,None)
    start = time.perf_counter()
    for value in range(length):
        unique_array(an_array, value)

    return round(time.perf_counter() - start, 3)

#Class Activity 9.1.3
def unique_list(a_list , value):
    length = len(a_list)
    for index in range(length):
        if a_list[index] == value:
            return
    a_list.append(value)

def fill_list(length):
    a_list = []
    start = time.perf_counter()
    for value in range(length):
        unique_list(a_list , value)
    
    return round(time.perf_counter() - start, 4)

#Class activity 9.1.4
def sets():
    a_set = {1, 5, 7, 9}
    print(a_set)
    a_set.add(10)
    a_set.add(11)
    a_set.add(99)

    for value in a_set:
        print(value, end= " ")
    print()
    b_set = set("abcddcbaabcde")
    print(b_set)
    print()

#Class activity 9.1.5
def unique_set(a_set, value):
    if value not in a_set:
        a_set.add(value)

def fill_set(length):
    a_set = set()
    start = time.perf_counter()
    for value in range(length):
        unique_set(a_set, value)
    print("a_set: ", a_set)

    return round(time.perf_counter() - start, 6)

#Calss activity 9.1.6
def coupon_collector(n):
    collection = set()
    boxes = 0
    while len(collection) < n:
        r = random.randint(1 , n)
        collection.add(r)
        boxes += 1

    return boxes

#Class activity 9.1.7
def mixup():
    a_string = "abcdefghijklmnopqrstuvwxyz"
    a_set = set(a_string)
    for char in a_set:
        print(char , end=" ")
    print()
    print(a_set)

#Class activity 9.1.8
def unique_words(filename):
    a_set = set()
    with open(filename) as file:
        for line in file:
            words = line.split()
            for word in words:
                a_set.add(word.lower())

    return a_set

def unique_words_challange(filename):
    a_set = set()
    with open(filename) as file:
        for line in file:
            words = line.split()
            for word in words:
                real_words = re.findall("[\w]+" , word.lower())
                for real_word in real_words:
                    a_set.add(real_word)

    return a_set

#Class activity 9.1.9
def superset(a_set : set , b_set : set) -> bool:
    for value in b_set:
        if not(value in a_set):
            return False
    return True

#Class activity 9.1.10
def subset(a_set : set , b_set : set):
    for value in a_set:
        if not(value in b_set):
            return False
    return True

#Class activity 9.1.11
def intersection(a_set : set , b_set : set):
    c_set = set()
    for value in a_set:
        if value in b_set:
            c_set.add(value)
    
    return c_set

#Class activity 9.1.12
def union(a_set : set , b_set : set):
    c_set = set()
    for value in a_set:
        c_set.add(value)
    for value in b_set:
        c_set.add(value)
    return c_set

#Class activity 9.1.12
def minus(a_set : set , b_set : set):
    for value in b_set:
        if value in a_set:
            a_set.remove(value)

#Class actiity 9.2.6 / 9.2.7
def names():
    names = {}
    names["J"] = "John"
    names["F"] = "Fitzgerald"
    names["K"] = "Kennedy"
    names["J"] = "Jacqueline"
    names["L"] = "Lee"
    names["K"] = "Kennedy"
    #9.2.7
    print(names["J"])
    print(names["F"])
    print(names["K"])
    print(names["L"])

#Class activity 9.2.8
def print_dict(dictonary):
    for key in dictonary:
        value = dictonary[key]
        print(key, ":", value, sep="")

#Class activty 9.3.2
def find_maxium(dictionary):
    max_key = None
    max_value = 0

    for key in dictionary:
        value = dictionary[key]
        if value > max_value:
            max_value = value
            max_key = key
    
    return max_key, max_value

#Class activty 9.3.3
def hashes():
    hashcode1 = hash("Hello World!")
    hashcode2 = hash("Hello World?")
    print(hashcode1)
    print(hashcode1)
    print(hashcode2)
    print(hashcode2)
    
    hashcode3 = hash("A"*100000)
    hashcode4 =hash("A"*100000000)

    return hashcode3 , hashcode4
    
#Class activty 9.3.4
def collisions(filename, length, hash_func = hash):
    an_array = arrays.Array(length, None)
    with open(filename) as file:
        count = 0
        for line in file:
            line = line.strip()
            if line == "":
                continue
            hash_code = hash_func(line)
            index = hash_code % length
            if an_array[index] is None:
                an_array[index] = line
                count += 1
            else:
                return count 

#Class activty 9.3.5
def make_myset(capasity, hash_func = hash):
    table = [[] for _ in range(capasity)]
    return (hash_func, table)

#Class activty 9.3.6
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

#Class activty 9.3.7
def contains(myset, element):
    hash_func = myset[0]
    table = myset[1]
    capasity = len(table)
    index = hash_func(element)%capasity
    row = table[index]
    for elt in row:
        if elt == element:
            return True
    return False

#Class activty 9.3.8
def ascii_codes(a_string):
    for char in a_string:
        print(char , ":" , ord(char), sep="")

#Class activty 9.3.9
def string_hash(a_string):
    max_ascii = -1
    for char in a_string:
        char_ascii = ord(char)
        if char_ascii > max_ascii:
            max_ascii = char_ascii
    
    return max_ascii

#Class activty 9.3.10
def string_hash_better(a_string):
    max_ascii = -1
    for char in a_string:
        char_ascii = ord(char)
        if char_ascii > max_ascii:
            max_ascii = char_ascii
    
    return max_ascii * len(a_string)

def main():

    #Class Activities 9.1.2
    '''
    size = 5000
    print("Fill array: " , fill_array(size), "Seconds")
    '''

    #Class Activities 9.1.3
    '''
    size = 5000
    print("Fill list: " , fill_list(size), "Seconds")
    '''

    #Class activies 9.1.4
    '''
    a_set = sets()
    b_sets = sets()
    c_sets = sets()
    '''

    #Class activies 9.1.5
    '''
    size = 5000
    print("Fill set: " , fill_set(size), "Seconds")
    '''

    #Class activies 9.1.6
    '''
    n = 500000
    boxes = coupon_collector(n)
    print(boxes , round(n*math.log(n) + 0.577215*n, 0))
    '''

    #Class activies 9.1.7
    '''
    mixup()
    mixup()
    mixup()
    '''

    #Class activies 9.1.8
    '''
    filename = "data/alice.txt"
    words = unique_words(filename)
    print("found" , len(words), "unique_words in " , filename)

    chllangewords = unique_words_challange(filename)
    print("found" , len(chllangewords), "unique_words in " , filename)
    '''

    #Class activies 9.1.9
    '''
    a_set = set('abcd')
    b_set = set('cdef')
    c_set = set('ab')
    print(superset(a_set , b_set))
    print(superset(a_set, c_set))
    '''

    #Class activies 9.1.10
    '''
    a_set = set('abcd')
    b_set = set('cdef')
    c_set = set('ab')
    print(subset(a_set , b_set))
    print(subset(c_set, a_set))
    '''

    #Class activies 9.1.11
    '''
    a_set = set('abcd')
    b_set = set('cdef')
    
    print(intersection(a_set , b_set))
    '''

    #Class activies 9.1.12
    '''
    a_set = set('abcd')
    b_set = set('cdef')
    c_set = set('ab')
    print(sorted(union(a_set, b_set)))
    '''

    #Class activies 9.1.13
    '''
    a_set = set('abcd')
    b_set = set('cdef')
    minus(a_set , b_set)
    print(a_set)
    '''

    #Class activies 9.2.6 / 9.2.7
    #names()

    #Class activies 9.2.8
    '''
    a_dict = {"B": "Buttercup", "H" : "Hermione", "T":"Thunder", "L": "Lighting"}
    print_dict(a_dict)
    '''

    #Class activity 9.3.2
    '''
    a_dict = {"one":0 , "two":200 , "three":3}
    print(find_maxium(a_dict))
    '''

    #Class activty 9.3.3
    #print(hashes())

    #Class activity 9.3.4
    '''
    filename = "data/alice.txt"
    print("hashes before collison (10):", collisions(filename, 10, hash))
    print("hashes before collison (100):", collisions(filename, 100, hash))
    print("hashes before collison (500):", collisions(filename, 500, hash))
    print("hashes before collison (5000):", collisions(filename, 5000, hash))
    '''

    #Class activty 9.3.5
    '''
    myset = make_myset(7)
    print(myset)
    '''

    #Class activty 9.3.6
    '''
    myset = make_myset(7)
    add(myset , "one")
    add(myset , "two")
    add(myset , "three")
    add(myset , "four")
    add(myset , "two")
    print(myset[1])
    '''

    #Class activty 9.3.8
    #ascii_codes("Deutschland, mein Herz in Flammen")

    #Class activty 9.3.9
    '''
    print(string_hash("Deutschland, Deutschland über allen"))
    print(string_hash("The quick brown fox"))
    filename = "data/alice.txt"
    print("Hashes before collision (10):" , collisions(filename , 10, string_hash))
    print("Hashes before collision (100):" , collisions(filename , 100, string_hash))
    print("Hashes before collision (500):" , collisions(filename , 500, string_hash))
    print("Hashes before collision (5000):" , collisions(filename , 5000, string_hash))
    '''

    #Class activty 9.3.10
    print(string_hash_better("Deutschland, Deutschland über allen"))
    print(string_hash_better("The quick brown fox"))
    filename = "data/alice.txt"
    print("Hashes before collision (10):" , collisions(filename , 10, string_hash_better))
    print("Hashes before collision (100):" , collisions(filename , 100, string_hash_better))
    print("Hashes before collision (500):" , collisions(filename , 500, string_hash_better))
    print("Hashes before collision (5000):" , collisions(filename , 5000, string_hash_better))

main()

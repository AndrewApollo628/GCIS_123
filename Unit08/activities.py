#Author: Andrew Apollo 

#Import statements 
import random
import arrays
import array_utils
import sorts


#Activity 8.1.2 
def tuples(a_tuple):
    print(len(a_tuple))
    print(a_tuple)
    for element in a_tuple:
        print(element)

#Activity 8.1.3 / 8.1.4
def lists():
    a_list = [1, 2, "a", True, ('b' , 'c')]
    for index in range(len(a_list)):
        print(index, ": " , a_list[index], sep="")
    a_list[0] = 57
    return a_list

#Activity 8.1.5
def make_list(a_sequence):
    a_list = []
    for elemrnt in a_sequence:
        a_list.append(elemrnt)
    return a_list

#Activity 8.1.6
def scale(a_list, scaler):
    for index in range(len(a_list)):
        a_list[index] = a_list[index] *scaler
    return a_list

#Activity 8.1.7
def mutator(a_list , an_int):
    print("mutator:" , an_int, a_list)
    an_int = an_int * 5
    a_list[0] *= 5
    print("mutator:" , an_int, a_list)

#Activity 8.1.8 
def cat(a_list , b_list):
    a_list = a_list + b_list
    return a_list

#Activity 8.1.9
def extender(a_list , b_list):
    a_list += b_list
    return a_list

#Activity 8.1.10
def inserter(a_list, vlaue):
    middle = len(a_list) // 2
    a_list.insert(middle, vlaue)

#Activity 8.1.11
def popper(a_list):
    length = len(a_list)
    if length > 0:
        index = random.randrange(length)
        popped = a_list.pop(index)
        print(a_list, popped)
        popper(a_list)

#Activity 8.1.12
def array_insert(an_array , index, value):
    length = len(an_array)
    if length == 0:
        return arrays.Array(1 , value)
    else:
        inserted = arrays.Array(length + 1) 
        for i in range(index):
            inserted[i] = an_array[i]
        inserted[index] = value
        for i in range(index + 1 , length + 1):
            inserted[i] = an_array[i-1]
        return inserted

#Activity 8.1.13
def array_pop(an_array , index):
    length = len(an_array)
    popped = arrays.Array(length - 1)
    for i in range(index):
        popped[i] = an_array[i]
    for i in range(index + 1 , length):
        popped[i-1] = an_array[i]

    return popped , an_array[index] 

#Activity 8.2.2
def rgb_tuple():
    red = random.random()
    green = random.random()
    blue = random.random()

    return(red, green, blue)

#Activity 8.2.3
def tuple_equality(tuple1 , tuple2):
    print(tuple1)
    print(tuple2)
    print(tuple1 is tuple2)
    print(tuple1 == tuple2)
    print()

#Activity 8.2.4
def reverse_sequence(sequence):
    list = []
    length = len(sequence)
    for index in range(length-1, -1, -1):
        list.append(sequence[index])

    return list

#Activity 8.2.5
def slices():
    lyric = "Deutschland, mein Herz in Flammen Will dich lieben und verdammen"
    a_list = list(lyric)
    print(a_list)
    start = 0 
    stop = 0 
    for index in range(len(a_list)):
        if a_list[index] == ' ':
            stop = index
            word = a_list[start:stop]
            print(word)
            start = stop + 1

    word = a_list[start:]
    print(word)

#Activity 8.2.6 
def dices(a_list):
    if not a_list:
        return
    else:
        index = random.randrange(len(a_list))
        element = a_list[index:index+1]
        print(element)
        new_list = a_list[:index] + a_list[index +1:]
        dices(new_list)

#Activity 8.2.7
def random_list(size):
    rand_list = []
    for _ in range(size):
        value = random.randint(0, 100)
        rand_list.append(value)
    return rand_list

#Activity 8.2.7 / 8.2.9 
def sorted_test(a_list):
    print("before:", a_list)
    b_list = sorted(a_list)
    print("after:", a_list)
    print("sorted:", b_list)

#Activity 8.2.8 / 8.2.9 
def sort_test(a_list , backwards = False):
    print(a_list)
    a_list.sort(reverse  = backwards)
    print(a_list)

#Activty 8.2.10 / 8.2.11
def sort_cards(hand):
    print(hand)
    #hand.sort()
    hand.sort(key = suit_key)
    print(hand)

#Activity 8.2.11
def suit_key(card):
    key = 0 
    suit = card[1]
    if suit == "D":
        key += 100
    elif suit == "H":
        key += 200
    elif suit == "S":
        key += 300
    key += card[0]
    return key
def main():

    #Activity 8.1.2
    '''
    tuples(())
    tuples(("a" , "b" , "c"))
    tuples((1 , 2 , 3))
    tuples(("a" , 12 , True))
    '''

    #Activity 8.1.3 / 8.1.4
    #print(lists())

    #Activity 8.1.5
    #print(make_list("this is a list"))

    #Activity 8.1.6
    '''
    a_list = [1, 2, 3, 4, 5]
    print(a_list)
    scale(a_list,5)
    print(a_list)
    '''

    #Activity 8.1.7
    '''
    an_int = 7
    a_list = [an_int]
    print("Before: " , an_int , a_list)
    mutator(a_list , an_int)
    print("After: " , an_int , a_list)
    '''

    #Activity 8.1.8 / 8.1.9
    '''
    a_list = [1, 2 , 3]
    b_list = ["a" , "b"]
    #c_list = cat(a_list , b_list) #Activity 8.1.8
    c_list = extender(a_list , b_list) #Activity 8.1.9
    print(a_list)
    print(b_list)
    print(c_list)
    '''

    #Activity 8.1.10
    '''
    a_list = []
    for i in range(5):
        inserter(a_list , 1)
        print(a_list)
    '''

    #Activity 8.1.11
    '''
    a_list = []
    for i in range(5):
        inserter(a_list , i)
    print(a_list)
    popper(a_list)
    print(a_list)
    '''

    #Activity 8.1.12
    '''
    an_array = array_utils.range_array(0,11)
    print(an_array)
    print(array_insert(an_array,4,100))
    '''

    #Activity 8.1.13
    '''
    an_array = array_utils.range_array(0,11)
    print(an_array)
    print(array_pop(an_array,4))
    '''

    #Activity 8.2.2 
    '''
    print(rgb_tuple())
    print(rgb_tuple())
    print(rgb_tuple())
    '''

    #Activity 8.2.3
    '''
    a_list = [1, 5, True, "abc"]
    a_tuple = tuple(a_list)
    tuple_equality(a_tuple , a_tuple)
    b_tuple = tuple(a_list)
    tuple_equality(a_tuple , b_tuple)
    c_tuple = ("abc" , True, 5, 1)
    tuple_equality(a_tuple , c_tuple)
    '''
    #Activity 8.2.4
    '''
    print(reverse_sequence("abcd"))
    print(reverse_sequence([1, 2, 3, 4]))
    print(reverse_sequence(range(5, 10)))
    print(reverse_sequence(("x" , "y", "Z")))
    '''

    #Activity 8.2.5
    #slices()

    #Activity 8.2.6
    #dices(list(range(1, 11)))

    #Activty 8.2.7
    '''
    rand_list = random_list(10)
    sorted_test(rand_list)
    print()
    '''
    #Activity 8.2.8
    '''
    rand_list = random_list(10)
    sort_test(rand_list)
    print()
    '''

    #Activity 8.2.9
    '''
    rand_list = random_list(10)
    sort_test(rand_list, True)
    print()
    '''

    #Activty 8.2.10
    '''
    hand = [(5, "H") , (2 , "D"), (10 , "S") , (7 , "S") , (10, "C")]
    sort_cards(hand)
    '''

    #Activity 8.2.11
    hand = [(5, "H") , (2 , "D"), (10 , "S") , (7 , "S") , (10, "C")]
    sort_cards(hand)
main()
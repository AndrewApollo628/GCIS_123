#Author: Andrew Apollo 

import arrays
import random
import time
import array_utils
import searches
import turtle
import math

#class activity 6.1.2
def making_arrays():
    array_1 = arrays.Array(5)
    print(array_1)

    array_2 = arrays.Array(1 , 0)
    print(array_2)

    array_3 = arrays.Array(10 , " ")
    print(array_3)

    array_4 = arrays.Array(20, False)
    print(array_4)

#class activity 6.1.3
def while_fill(an_array):
    index = 0
    length = len(an_array)
    while index < length:
        an_array[index] = index
        index += 1

#class activity 6.1.4
def for_fill(an_array):
    for index in range(len(an_array)):
        an_array[index] = index

#class activity 6.1.5 / 6.1.6
def roll_the_die(sides):
    return random.randint(1,sides)

#class activity 6.1.9
def linear_search_timer(an_array, target):
    start = time.perf_counter()
    searches.linear_search(an_array, target)
    stop  = time.perf_counter()
    return stop - start
    

def time_linear():
    an_array = array_utils.range_array(1, 10000001)

    length = len(an_array)
    first = an_array[0]
    middle = an_array[length // 2]
    last = an_array[length -1]

    elapsed = linear_search_timer(an_array, first)
    print("First:", elapsed , "seconds....")

    elapsed = linear_search_timer(an_array, middle)
    print("middle:", elapsed , "seconds....")

    elapsed = linear_search_timer(an_array, last)
    print("last:", elapsed , "seconds....")

#Class activity 6.2.3
def print_odds(an_array):
    for index in range(len(an_array)):
        if an_array[index] % 2 == 1:
            print(an_array[index], end=" ")
    print()

#Class activity 6.2.4/6.2.5
def print_odds_rec(an_array , index = 0):
    if index >= len(an_array):
        print()
    else:
        if an_array[index] % 2 == 1:
            print(an_array[index], end =" ")
        print_odds_rec(an_array , index +1)

#Class activity 6.2.6
def countdown(n):
    if n == 0:
        print(n)
        return 0 
    else:
        print(n)
        return n + countdown(n-1)

#Class activity 6.2.7/6.2.8
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

#Class activity 6.2.9
def circles(radius,depth):
    if depth == 0:
        return 0
    elif depth == 1:
        turtle.circle(radius)
        return math.pi * radius * 2 
    else:
        for _ in range(4):
            turtle.circle(radius , 90)
            circles(radius/2 , depth-1)

#Class activity 6.3.2
def count_up(num):
    if num == 0:
        print(num)
        return
    else:
        count_up(num - 1)
        print(num)
        return

#Class Activity 6.3.8
def binary_search_timer(an_array, target):
    start = time.perf_counter()
    searches.binary_search(an_array, target)
    stop  = time.perf_counter()
    return stop - start

def main():
    '''
    making_arrays()
    
    array_a = arrays.Array(10, 0)
    print(array_a)
    while_fill(array_a)
    print(array_a)
    
    array_b = arrays.Array(10, "a")
    print(array_b)
    for_fill(array_b)
    print(array_b)
    
    random.seed(1)
    for _ in range(10):
        print("Rolling a 6-sided die: ", roll_the_die(6))
    
    time_linear()
    
    an_array = array_utils.range_array(0,101)
    print_odds(an_array)
    print_odds_rec(an_array, )
    
    print("Sum: ", countdown(5))
    
    print("10! = ", factorial(10))
    print("100! = ", factorial(100))
    print("1000! = ", factorial(1000))
    
    #Class activity 6.2.9
    radius = 200
    turtle.up()
    turtle.setpos(0, -radius)
    turtle.down()
    turtle.speed(0)
    turtle.pencolor('red')
    turtle.pensize(1)
    circumfrence = circles(radius, 6)
    print("circumfrence:", circumfrence)
    input("Press enter to continue: ")
    
    count_up(3)
    '''
    an_array = array_utils.range_array(1, 10000001)
    total = binary_search_timer(an_array , 1)
    total += binary_search_timer(an_array , 1000000)
    total += binary_search_timer(an_array , 2000000)
    total += binary_search_timer(an_array , 3000000)
    total += binary_search_timer(an_array , 4000000)
    total += binary_search_timer(an_array , 5000000)
    total += binary_search_timer(an_array , 6000000)
    total += binary_search_timer(an_array , 7000000)
    total += binary_search_timer(an_array , 8000000)
    total += binary_search_timer(an_array , 9000000)
    total += binary_search_timer(an_array , 10000000)
    
    avg = total/11
    print("Average binary search: " , avg)

if __name__ == "__main__":
    main()
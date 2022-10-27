'''
Author: Andrew Apollo

This program tests the program fibbonacci.py
'''
#Import Statements 
import fibonacci

def test_check_n_less_than_zero(): #test to see if n is less than 1 
    value = fibonacci.fibonacci_naive(-1)
    assert (value == "undefined")

def test_check_n_equal_one(): #test to see if n = 1
    value = fibonacci.fibonacci_naive(1)
    assert (value == 0)

def test_check_n_equal_two(): #test to see if n = 2
    value = fibonacci.fibonacci_naive(2)
    assert (value == 1)

def test_check_n_greater_than_one(): #test to see if n > 1
    value = fibonacci.fibonacci_naive(9)
    assert (value == 21)

def test_check_n_less_than_zero_fast(): #test to see if n is less than 1 in fibonacci_fast
    value = fibonacci.fibonacci_fast(-1)
    assert (value == "undefined")

def test_check_n_less_equal_one_fast(): #test to see if n is equal to 1 in fibonacci_fast
    value = fibonacci.fibonacci_fast(1)
    assert (value == 0)

def test_check_return(): #test to see if n is equal to 1 in fibonacci_fast
    value = fibonacci.fibonacci_fast(10)
    assert (value == 144)
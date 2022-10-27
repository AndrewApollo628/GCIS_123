'''
Author: Andrew Apollo 

This program 
    - finds the Fibonacci sequence for a number 
    - plot the time it takes to compute the first n numbers in the sequence using plotter 
'''
#Import Statements 
import plotter 
import time


def fibonacci_naive(n):
    ''' 
    This function finds the fibonacci sequence for a number (n)

    Paramaters
        - n: number of the sequence the function goes to 
    
    '''
    if n <= 0:
        return "undefined"
    elif n == 1:
        return 0 
    elif n == 2:
        return 1 
    elif n > 1: 
        return(fibonacci_naive(n-1) + fibonacci_naive(n-2))

def fibonacci_fast(n ,depth = 0,  fn_minus_1 = 1 , fn_minus_2= 0): 
    '''
    This function finds the fibonacci sequence for a number (n) fast 

    Paramaters: 
        - n: number of the sequence the function wants to get
        - fn_minus_1: set to represent 1 
        - fn_minus_2: set to represent 0
        - depth: 

        This solution refrences
            - https://stackoverflow.com/questions/66488774/python-fibonacci-recursion-and-not-iteration-with-on-time?rq=1  
    '''
    if n <= 0:
        return "undefined"
    elif n == 1: 
        return 0 
    elif n == 2:
        return 1
    elif depth < n:
        return (fibonacci_fast(n=n ,depth = depth + 1 , fn_minus_1= fn_minus_1+fn_minus_2 , fn_minus_2 = fn_minus_1))
    else: 
        return fn_minus_1 + fn_minus_2
    
def naive_timer(n):
    '''
    This function will call the fibonacci_fast function adn plot the time 
    it takes to compute the first n numbers in the sequence 

    Paramaters 
        - n: number of times the sequence is ran 
    '''
    index = 0 
    while index < n: 
        start = time.perf_counter()
        fibonacci_naive(n)
        stop = time.perf_counter()
        timer = stop - start 
        plotter.add_data_point(timer)
        index += 1
    plotter.plot()

def faster_timer(n):
    '''
    This function will call the fibonacci_naive function adn plot the time 
    it takes to compute the first n numbers in the sequence 

    Paramaters 
        - n: number of times the sequence is ran 
    '''
    index = 0 
    while index < n: 
        start = time.perf_counter()
        fibonacci_fast(n)
        stop = time.perf_counter()
        timer = stop - start 
        plotter.add_data_point(timer)
        index += 1
    plotter.plot()

def main():
    plotter.init("Naive Fibonacci" , "in" , "time")
    
    #first input calls plots naive_timer
    value = int(input("Enter value for n: "))
    naive_timer(value)
    
    #Second input calls plots faster_timer
    value2 = int(input("Enter value for n: "))
    faster_timer(value2)

    #third input calls plots naive_timer vs faster_timer
    value3 = int(input("Enter value for n: "))
    plotter.new_series(naive_timer(value3) , faster_timer(value3))
    input("Press enter to exit: ")
    
if __name__ == "__main__":
    main()

 
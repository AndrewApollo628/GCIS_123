'''
Author: Andrew Apollo 

This program will 
    - Plot the results of timing each search using plotter 
'''
#Import Statements 
import plotter
import array_utils
import time

def linear_plot(size , runs):
    '''
    This function will  
        - initialise plotter 
        - create an array of a specified size 
        - time the number of linear serches for a target value 
    Paramaters 
        - Size: size of the array 
        - Runs: amount of points being taken in 
    '''
    plotter.init("Linear Search" , "Length" , "Time")
    an_array = array_utils.range_array(1 , size , runs)
    index = 0 
    
    while index < len(an_array) :
        start = time.perf_counter()
        an_array[index]
        stop = time.perf_counter()
        index += 1
        timing = stop - start
        plotter.add_data_point(timing)


    plotter.plot()
def main():    

    size = int(input("enter the size: "))
    runs = int(input("enter the number of runs: "))
    
    if size == "" or runs == "":
        return 
    else:
        linear_plot(size , runs)
    input()
main()
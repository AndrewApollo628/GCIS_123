'''
Author: Andrew Apollo

This program will
    - Creates a sorted array of the given size
    - Calculates the average time for binary search to find every value
    - Returns the average time

'''
#import staements
import searches
import time
import array_utils
import plotter

def average_binary_search(size , runs):
    '''
    This function 
        - Creates a sorted array of the given size
        - Calculates the average time for binary search to find every value
        - Returns the average time

    Paramaters
        - size: size of the aray
        - how many values of the array are returned 
    '''
    x = 0
    an_array = array_utils.range_array(0 , size, runs)
    searches.binary_search(an_array , an_array[x])
    while x <= runs:
        start = time.perf_counter()
        an_array[x]
        stop = time.perf_counter()
        x += 1
        average = stop - start
        
    #return average
    
def plot_average_binary_searches(min_size , max_size , runs):
    for i in range(min_size , max_size , runs):
        average_binary_search(max_size , runs-1)
        plotter.add_data_point(i)
plotter.plot()
plot_average_binary_searches(1 , 100 , 10)
input()
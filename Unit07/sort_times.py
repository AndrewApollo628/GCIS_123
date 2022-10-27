'''
Author: Andrew Apollo 

This program will 
    - time a sort function
    - plot the time returned 

'''
#Import Statements
import sorts
import time
import array_utils
import plotter
import arrays
import merge_sort
import quicksort

#Global Varibles 
ARRAY_SIZE = 3000
SIZES = [200 ,500, 800, 1100, 1400, 1700, 2000]


def insertion_sort_function_timer(an_array):
    '''
    This function
        - Takes in an array 
        - claculates the time that an insertion sort takes
    
    Paramaters
        - an_array: Array being passed in to the function
    '''
    start = time.perf_counter()
    sorts.insertion_sort(an_array)
    stop = time.perf_counter()
    elapsed = stop -start
    return elapsed

def sort_function_timer(an_array , sort_function):
    start = time.perf_counter()
    sort_function(an_array)
    stop = time.perf_counter()
    elapsed = stop -start
    return elapsed

def plot_sort_time_using_random_arrays(sort_function):
    '''
    This function will 
        - Creates a random array with array sizes  
        - calls sort_function_timer to plot the time it takes to go through the array

    Paramaters
        - sort_function: sort function that is being used   
    '''
    
    for i in range(len(SIZES)):
        an_array = array_utils.random_array(SIZES[i])
        plot = sort_function_timer(an_array , sort_function)
        plotter.add_data_point(plot)

def plot_sort_time_using_sorted_arrays(sort_function):
    '''
    This function will 
        - Creates a sorted array with array sizes  
        - calls sort_function_timer to plot the time it takes to go through the array

    Paramaters
        - sort_function: sort function that is being used   
    '''
    for i in range(len(SIZES)):
        an_array = array_utils.range_array(0 , SIZES[i])
        #print(an_array)
        plot = sort_function_timer(an_array , sort_function)
        plotter.add_data_point(plot)
    
def plot_sort_time_using_duplicate_random_arrays(sort_function):
    '''
    This function 
        - Creates a random array with dulicate values
        - Takes the array and sort function and plots the time that the sort function takes

    Paramaters
        - sort_function: sort function that is being used 
    '''
    for i in range(len(SIZES)):
        an_array = array_utils.random_array(i, 0, i//100)
        #print(an_array)
        plot = sort_function_timer(an_array , sort_function)
        plotter.add_data_point(plot)

def main():
    '''
    sorted_array = array_utils.range_array(0, ARRAY_SIZE)
    print("insertion sort for sorted array: ")
    print(insertion_sort_function_timer(sorted_array))

    random_array = array_utils.random_array(ARRAY_SIZE)
    print("insertion sort for sorted array: ")
    print(insertion_sort_function_timer(random_array))

    random_array2 = array_utils.range_array(ARRAY_SIZE , 0 , -1)
    print("insertion sort for sorted array: ")
    print(insertion_sort_function_timer(random_array2))
    '''
    #print(SIZES)
    
    plotter.init("Sort","array","Time")
    #an_array = arrays.Array(SIZES)
    #an_array = array_utils.random_array(SIZES[i])
    #print(an_array)
    '''
    plot_sort_time_using_random_arrays(sorts.insertion_sort)
    plotter.new_series()
    plot_sort_time_using_random_arrays(sorts.insertion_sort_wo_swap)
    plotter.new_series()
    plot_sort_time_using_random_arrays(merge_sort.merge_sort)
    plotter.new_series()
    plot_sort_time_using_random_arrays(quicksort.quicksort)
    plotter.plot()
    
    plot_sort_time_using_sorted_arrays(sorts.insertion_sort)
    plotter.new_series()
    #plot_sort_time_using_sorted_arrays(sorts.insertion_sort_wo_swap)
    #plotter.new_series()
    plot_sort_time_using_sorted_arrays(merge_sort.merge_sort)
    plotter.new_series()
    plot_sort_time_using_sorted_arrays(quicksort.quicksort_mid)
    plotter.plot()
    '''

    #HW 7.1 activity 5 part 1 random arrays test 
    '''
    plot_sort_time_using_random_arrays(sorts.insertion_sort)
    plotter.new_series()
    plot_sort_time_using_random_arrays(merge_sort.merge_sort)
    plotter.new_series()
    plot_sort_time_using_random_arrays(quicksort.quick_insertion_sort)
    plotter.new_series()
    plotter.plot()
    
    #HW 7.1 activity 5 part 2 sorted arrays test
    plot_sort_time_using_sorted_arrays(sorts.insertion_sort)
    plotter.new_series()
    plot_sort_time_using_sorted_arrays(merge_sort.merge_sort)
    plotter.new_series()
    plot_sort_time_using_sorted_arrays(quicksort.quick_insertion_sort)
    plotter.plot()
    

    '''
    #HW 7.1 activity 6 test
    plot_sort_time_using_duplicate_random_arrays(sorts.insertion_sort)
    plotter.new_series()
    plot_sort_time_using_duplicate_random_arrays(merge_sort.merge_sort)
    plotter.new_series()
    plot_sort_time_using_duplicate_random_arrays(quicksort.quick_insertion_sort)
    plotter.plot()
    

    input("Press enter to continue")

main()
    
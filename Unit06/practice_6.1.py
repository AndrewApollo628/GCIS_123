'''
Author: Andrew Apollo

This program will:
    -Return the number of time "Alice" apears in "alice.txt" 
    -Calculate the average of count fields
    -Print names of students above the min grade average 

'''
#Import Statements 
import csv
from typing import Counter


def find_alice ():
    """
    Function that returns the number of times the word
    "Alice" appears in the story, 'Alice and Wonderland'.

    See Assignment 6.1 for requirement details.
    """
    count = 0
    col = 0
    filename = "data/alice.txt"
    with open(filename) as alice:
        for line in alice:
            for word in line.split():
                if word == "Alice":
                    count += 1
    return(count)

            


def calculate_average (record, start_col, count):
    """
    Function to calculate the average of count fields
    in a record, starting at start_col.

    Update to handle issues that might occur. Refer to 
    Assignment 6.1 for more details.
    """
    sum = 0
    for index in range (start_col, start_col + count):
        try:
            sum += int (record [index])
        
        except ValueError: 
            try:
                sum = round(float(record [index])) + sum
            except:
                pass
    average = sum / count

    return average



def deans_list (filename, min_grade):
    """
    Function that prints the names of all students
    that are above the specified minimum grade average
    for all of their assignment.

    See Assignment 6.1 for requirement details.
    """
    with open(filename) as csv_file: 
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for row in csv_reader:
            if calculate_average(row, 4 , len(row) - 4) >= min_grade:
                print(row[0])
            
            



def main ():
    # Simple find_alice test
    #print ("Found Alice", find_alice() , "times.")
    

    # Sample records that can be used to test calculate_avearge
    #clean_record = 'Student,80,68,75,81,85,93'.split (',')
    #dirty_record = 'Student,80,97.8,75,,85.4,a'.split (',')

    # calculate_average tests
    #print (calculate_average (clean_record, 1, 6)) # 80.3333333333
    #print (calculate_average (dirty_record, 1, 6)) # 56.3333333333

    # Test for deans_list
    deans_list ("data/full_grades_999.csv", 89)
    #deans_list("data/full_grades_100.csv", 82)
    #deans_list("data/full_grades_010.csv", 75)

if __name__ == "__main__":
    main ()
'''
Author: Andrew Apollo

This program will
    - return the top level data a streets.csv file
    - Create a class for an exam 
'''

#Imports
import csv

def streets(filename):
    '''
    This function will
        - return all the streets in the file
    Paramaters 
        - filename: name of file being opened 
    '''
    with open(filename) as file:
        streets = [] 
        csv_reader = csv.reader(file)
        next(csv_reader)
        for line in csv_reader:
            street_name = line[0]
            street_type = line[1]
            streets.append((street_name, street_type))
            
    return streets

class Exam:
    '''
    This class will 
        - keep track of students who take the exam 
        - keep track of total points 
        - keep track of points earned 
    '''
    __slots__ = ["__student_name", "__total_points", "__points_earned"]

    def __init__(self, name, total_points):
        '''
        This function will
            - initilize fields for Exam
        Paramaters
            - self: exam object to target
            - total_points: total points of exam object
        '''
        self.__student_name = name
        self.__total_points = total_points
        self.__points_earned = 0 
    
    def get_name(self):
        '''
        This function will
            - get the name of an object and return it
        Paramaters
            - self: object getting name from
        '''
        return self.__student_name

    def get_total_points(self):
        '''
        This function will
            - get the total points of an object and return it
        Paramaters
            - self: object getting name from
        '''
        return self.__total_points
    
    def get_earned_points(self):
        '''
        This function will
            - get the earned points of an object and return it
        Paramaters
            - self: object getting name from
        '''
        return self.__points_earned
    
    def set_earned_points(self, points_earned):
        '''
        This function will
            - set the number of earned points 
        Paramaters
            - self: object points are being set 
        '''
        self.__points_earned = points_earned

    def calculate_grade(self):
        '''
        This function will
            - calculate the grade of the student
        Paramaters
            - self: student getiing points from
        '''
        earned = self.__points_earned
        possible = self.__total_points
        grade = (earned/possible) * 100

def main():
    filename = "data/streets.csv"
    street_names = streets(filename)
    
    #Activity 2A will find how many DR are in the file 
    dr = []
    for street in street_names:
        if street[1] == "DR":
            dr.append(street)
    print("There are " + str(len(dr)-1) + " DR's in " + filename)
    print()

    #Activity 2B will find if there is a READ LEAD LN
    red_leaf = False
    for line in street_names:
        if line[0] == "RED LEAF" and line[1] == "LN":
            red_leaf = True
        
    if red_leaf == False:
        print("There is no READ LEAF LN in " + filename)
    else:
            print("There is a READ LEAF LN in "  + filename)
    print()

    #Activity 2C will list all the street types for vista
    vista = []
    for _ in street_names:
        if _[0] == "VISTA":
            vista.append((_[0], _[1]))
    
    print("These are all the street types for VISTA")
    for type in vista:
        print(type)
    print()

if __name__ == "__main__":
    main()
'''
Author: Andrew Apollo 

This module will plot grades for a single student or class average 

'''
#Import Statements 
import csv
import plotter 
import re


def plot_grades(filename , first_name , last_name):
    '''
    This program will look for a student and plot their grades using plotter

    Peramaters:
        filename: Name of the file the data is in that wee need to plot
        first_name: First name of the syudent we are looking for
        last_name: Last name of the student we are looking for
    
    '''
    plotter.init(first_name +" " + last_name , "Grade Item" , "Score")
    with open(filename) as csv_file:
        reader = csv.reader(csv_file)
        next(csv_file)
        for row in reader:
            split = re.findall('[\w]+[a-z]{3,9}' , row[0]) #Splits the combined name string 
            if split[1] == first_name and split[0] == last_name:
                for col in row:
                    try:
                        plotter.add_data_point(float(col))
                    except:
                        pass
            else:
                #next(csv_file)
                continue
            
    plotter.plot()

def get_average(filename , column):
    '''
    This function will take in a specific row and calculaste the class average 

    Paramaters:
        filename: name of the csv file we are getting the data from 
        column: The colum that we want to get the data from 
    
    '''
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        grade = 0
        count = 0 
        for row in csv_reader:
            try:
                if row[column] == '': #skips the values that dont have any input 
                    continue
                grade += float(row[column])
                count += 1
            except:
                pass
        average = grade/count
        plotter.add_data_point(average)


def plot_class_average(filename): 
    '''
    This function will call get avg to calculate the avg for each colum and plot 
    them with plotter 

    Paramaters:
        filename: name of the file we want to get our data from
    
    '''
    plotter.init("Class avg" + filename,"Grade Item","Average")
    with open(filename) as csv_file:
        for avg in range(3,29): 
            get_average(filename, avg)
            
    plotter.plot()
            
def main():
    '''
    This function runbs the functions that are called 
    '''
    plot_grades("data/full_grades_010.csv" , "Sion" , "Lobasso" )
    plot_grades("data/full_grades_010.csv" , "Endre" , "Foell" )
    #input("Press enter to exit")
    #get_average("data/full_grades_010.csv" , 3)
    plot_class_average("data/full_grades_999.csv")
    input("Press enter to exit")
main()



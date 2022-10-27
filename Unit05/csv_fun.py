#Author: Andrew Apollo

#Import statements 
import csv
import re

def opener(filename):
    try:
        with open(filename) as file:
            return True
    except:
        print("File cannot be opened ", filename)
        return False
    
def names_and_adresses(filename):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_file)
        for row in csv_reader:
            print("Name: " , row[0] , "address" , row[1])

def first_only(filename):
    with open(filename) as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            print(row[0])

def average(filename, colum):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        sum = 0
        count = 0
        for row in csv_reader:
            if row[colum] == "":
                continue
            sum += float(row[colum])
            count += 1
        average = sum/count
        return round(average , 2)
def zip_check(filename):
    zips = "[7-9]\d[4]"
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for record in csv_reader:
            adress = record[1]
            if re.findall(zips , adress):
                print(record[0], adress)
def main():
    '''
    filename = input("Enter a filename: ")
    if opener(filename):
        print("File was opened ")
    else:
        print("File cannot be open ")
    
    names_and_adresses("data/full_grades_010.csv")
    
    #first_only("data/full_grades_010.csv")
    
    for i in range(3,29):
        print(str(i) + "average" , average("data/full_grades_010.csv", i))
    '''
    zip_check("data/full_grades_010.csv")
main()
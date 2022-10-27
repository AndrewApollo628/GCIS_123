#Author: Andrew Apollo 

#Imports 
import math
import turtle
import csv

#Activity 13.1.2

#A. E:/users/optimus/primes.txt
#   E:/users/optimus/hello.py
#   E:/Program Files/Python/python.exe
#   E:/Program Files/Git/git-bash.exe

#B. cd users/optimus

#C. cd.. 

#D. ls E:/Program Files/

#E. notepad info.txt

#F. rm hello.py 

#Activity 13.1.3

'''
A. git status 
B. git add names.txt
C. git commit -m "comment"
D. git push
E. git pull

git status, add, commit, push
git log > log.txt
'''

#Activity 13.1.5
def deets():

    print("Andrew Apollo")
    print("Hometown: Guilderland NY")
    print("GCIS 123: 4 Credits")
    print("NSSA 102: 3 Credits")
    print("Discrete Math: 4 Credits")
    print("Web and Mobile I: 3 credits")
    print("Communications: 3 crdits")

#Activity 13.1.6
def mathmatics(): 
    x = float(input("Enter value for X: "))
    y = float(input("Enter a value for Y: "))

    print("x^y" , x ** y)
    print("y^x", y ** x)

    radius = (x+y) / 2
    print("Area of a circle:", math.pi*radius*radius)
    print("Area of triange", (0.5*x*y))

#Activity 13.1.7
def circles(radius):
    print("Radius: ", radius)
    print("Diamater of circle: ", radius * 2)
    print("Area of circle: ", math.pi * radius ** 2 )
    print("Circumfrence: ", math.pi * radius * 2)
    print("Volume: ", (3/4) * math.pi * radius ** 3)

#Activity 13.1.8
def distance(x1, y1, x2, y2):
    return ((x2-x1) ** 2 + (y2-y1) ** 2) ** 0.5

#Activity 13.1.9
def triangle(x1, y1, x2, y2, x3, y3, color = "blue"):
    turtle.up()
    turtle.speed(5)
    turtle.fillcolor("color")
    turtle.setpos(x1, y1)
    turtle.down()
    turtle.begin_fill()
    turtle.setpos(x2, y2)
    turtle.setpos(x3, y3)
    turtle.setpos(x1, y1)
    turtle.end_fill()
    turtle.up

    return distance(x1, y1, x2, y2) + distance(x2, y2, x3, y3) + distance(x3, y3, x1, y1)

#Activity 13.1.11
def chop_chop(a_string):
    evens = ""
    odds = ""
    index = 0

    while index < len(a_string):
        evens += a_string[index]
        if index +1 < len(a_string):
            odds += a_string[index +1]
        index += 2 

    return evens + odds

#Activity 13.1.9
def unchop(a_string):
    length = len(a_string)
    first_odd = length - length // 2

    original = ""

    for index in range(0, first_odd):
        original += a_string[index]
        odd = first_odd + index
        if odd < length:
            original += a_string[odd]
    
    return original

#Activity 13.1.14
def starts_with(filename, letter):
    with open(filename) as file: 
        count = 0 
        word_set = set()
        for line in file:
            words = line.lower().split()
            for word in words:
                if word[0] == letter:
                    count += 1
                    word_set.add(word)
        return count

#Activity 13.1.15
def zip_lookup(filename, zip_code):
    with open(filename) as zip_database:
        csv_reader = csv.reader(zip_database)
        next(csv_reader)
        for record in csv_reader:
            if record[0] == zip_code:
                return record[1]
        raise ValueError("Unknown Zip code: ", zip_code)



def main():

    #deets()
    #mathmatics()
    #circles(5)
    #triangle(10)
    #chopped = chop_chop("Making Sausage!")
    #print(chopped)
    #print(unchop(chopped))
    '''
    for ascii in range(97, 123):
        letter = chr(ascii)
        print(letter, ":", starts_with("data/atotc.txt", letter))
    '''

    sentinel = True
    filename = "data/zip_codes.csv"
    while sentinel:
        zip_code = input("Enter zip code: ")
        if zip_code == "":
            sentinel = False
        else:
            try:
                city_state = zip_lookup(filename, zip_code)
                print(city_state)
            except ValueError:
                print("Invalid zip code: ", zip_code)
            except FileNotFoundError:
                print("Bad zip code database file", filename)


if __name__ == "__main__":
    main()

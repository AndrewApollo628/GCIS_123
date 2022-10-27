'''
Author: Andrew Apollo 

This Program Will
    - Turns a English word to piglatin 
    - draw a polygon using turtle with a givin number of sides 
'''

#Imports 
import turtle
import csv

def pig_latin_translator(english_word):
    '''
    This function will
        - turn an english word to pig latin 
    Paramaters
        - english_word: word being turned to piglain 
    '''
    for letter in english_word:
        letter = letter.lower()
        if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
            pig_latin_word = english_word + "ay"
            return pig_latin_word
        else:
            remove_letter = english_word[2:len(english_word)]
            first_letter = english_word[:2]
            pig_latin_word = remove_letter + first_letter + "ay"
            return pig_latin_word

def polygon(side_length, num_sides, color = "green"):
    '''
    This function will
        - Take in a side length, number of sides and a color 
        - than will draw a polygon using turtle
        - check to see if number of sides is greater than 3
    Paramaters
        - side_length: length of side being drawn
        - num_sides: number of sides being drawn
        - color: color of polygon defaulted to green 
    '''
    lcv = 0

    if num_sides <= 3:
        raise ValueError ("Number of sides needs to be greater than 3")

    turtle.color(color)
    turtle.fillcolor(color)
    turtle.begin_fill()
    while lcv < num_sides:
        turtle.forward(side_length)
        turtle.left(360/num_sides)
        lcv += 1
    turtle.end_fill()

def find_streets(filename , street_name):
    '''
    This program will
        - print out street information takin in by a file
    Paramaters
        - filename: name of file that the street name is in 
        - street_name: name of street 
    '''
    try:
        with open(filename) as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            for street in csv_reader:
                street_ = street[0]
                street_type = street[1]
                if len(street)> 2:
                    direction = street[2]
                else:
                    direction = ""
                if street_name == street_.upper():
                    print(street_ + " " + street_type + " " + direction)           
    except FileNotFoundError:
        print("Not a proper file")
        
def main():

    #word = input("Enter English Word: ")
    #print(pig_latin_translator(word))

    polygon(30,5)
    input()

    #find_streets("data/streets.csv", "MISSION BAY")

if __name__ == "__main__":
    main()
        
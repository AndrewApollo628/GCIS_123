'''
Author: Andrew Apollo 

This program will 
    - Define an animal class 
'''


import random

# Field Numbers
NAME = 0
SOUND = 1
COLOR = 2

ANIMALS = [
    ["tiger","roar","orange/black"],
    ["parrot","squawk","green"],
    ["shark","chomp","grey"],
    ["dog","ruff","brown"],
    ["snake","hiss","red/black"],
    ["sheep","bleat","white"],
    ["cat","meow","black"],
    ["mouse","squeak","grey"]
]

#Ark dictonary 
ARK = {

}

class Animal: 
    '''
    This class will
        - inialize an animal object 
    '''
    __slots__ = ["__name", "__sound", "__color"]

    def __init__(self, name, sound, color):
        '''
        This function will 
            - initalize the fields in Animal
        Paramaters
            - self: object refrence 
            - name: name of animal
            - sound: sound of animal
            - color: color of animal
        '''
        self.__name = name 
        self.__sound = sound
        self.__color = color

    def __eq__(self, other):
        '''
        This function will
            - check to see if two animals characteristics are the same
        Paramaters
            - self: animal being compared
            - other: animal being comapred too
        '''
        if self.__name == other.__name and self.__sound == other.__sound and self.__color == other.__color:
            return True
        else:
            return False

    def fill_ark():
        '''
        This function will 
            - put animals into the arch dictonary
        '''
        lcv = 0 
        while len(ARK) < 9:
            number = random.randint(0, len(ANIMALS))
            new_Animal = ANIMALS[number]
            an_object = Animal(new_Animal[NAME], new_Animal[SOUND], new_Animal[COLOR])
            key = Animal[NAME]
            if value < 1:
                value = 0 
            elif value == 1:
                value += 1
            ARK[key] = value

        print(ARK)

def main():
    Animal.fill_ark()
main()



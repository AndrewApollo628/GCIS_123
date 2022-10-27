#Author: Andrew Apollo 

CALORIES_PER_POUND = 3000
CALORIES_PER_MILE = 100

#Class activity 11.1.2
class Pet:
    __slots__ = ["__speices", "__name", "__weight", "__fur_color", "__age"]

    #Class activity 11.3.2
    def __init__(self, species, name, weigth, fur_color, age = 0):
        self.__speices = species
        self.__name = name
        self.__weight = weigth
        self.__fur_color = fur_color
        self.__age = age

    #Class activity 11.1.4
    def feed(self, calories):
        self.__weight += calories / CALORIES_PER_POUND

    #Class activity 11.1.5
    def walk(self, miles):
        self.__weight -= miles * CALORIES_PER_MILE / CALORIES_PER_POUND
    
    #Class activity 11.1.7
    def get_name(self):
        return self.__name
    
    def get_weight(self):
        return self.__weight
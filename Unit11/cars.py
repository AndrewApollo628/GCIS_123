#Author: Andrew Apollo

MAX_FUEL = 15 
MPG = 30

#Class activity 11.2.2
class Car:
    __slots__ = ["__vin", "__make", "__model", "__year", "__milage", "__fuel" ]

    #Class activities 11.3.2
    def __init__(self, vin, make, model, year):
        self.__vin = vin
        self.__make = make
        self.__model = model
        self.__year = year
        self.__milage = 0 
        self.__fuel = 0
    
    #Class activities 11.3.3
    def print_car(self):
        print("vin=", self.__vin, ", make=", self.__make, ", model=", self.__model, ", year=", self.__year, 
        ", milage=", self.__milage, ", fuel=", self.__fuel, sep="")

    #Class activities 11.3.4
    def filler_up(self, gallons):
        self.__fuel += gallons
        if self.__fuel > MAX_FUEL:
            self.__fuel = MAX_FUEL

    #Class activities 11.3.5
    def drive(self, miles):
        max_miles = self.__fuel * MPG
        if miles > max_miles:
            miles = max_miles

        self.__milage += miles
        self.__fuel -= miles / MPG

    def __repr__(self):
        return "Car:\n" + \
            "\tVIN = " + self.__vin + "\n" + \
            "\tMake = " + self.__make + "\n" + \
            "\tModel = " + self.__model + "\n" + \
            "\tYear = " + str(self.__year) + "\n" + \
            "\tMilage = " + str(self.__milage) + "\n" + \
            "\tFuel = " + str(self.__fuel) 

    def __str__(self):
        return "Car [VIN=" +self.__vin + ", make=" + self.__make + \
            ", model=" + self.__model + "]"

    def __eq__(self, other):
        if type(self) != type(other):
            return False

        return self.__vin == other.__vin

    def __lt__(self, other):
        if type(self) != type(other):
            return False
        
        return self.__vin < other.__vin

    def __le__(self, other):
        if type(self) != type(other):
            return False
        
        return self.__vin <= other.__vin

    def __gt__(self, other):
        if type(self) != type(other):
            return False
        
        return self.__vin > other.__vin

    def __ge__(self, other):
        if type(self) != type(other):
            return False
        
        return self.__vin >= other.__vin

    def __hash__(self):
        return hash(self.__vin)
    
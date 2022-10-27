'''
Author: Andrew Apollo 

This program will 
    - Declare a sphere class 

'''

#Imports
import math

class Sphere: 
    __slots__ = ["__radius"]

    def __init__ (self, radius):
        '''
        This function will
            - ininialize radius 
        '''
        self.__radius = radius

    def get_radius(self):
        '''
        This function will 
            - get the radius of the Sphere object and return it 
        Paramaters 
            - self: Sphere object to get radius from 
        '''
        return self.__radius

    def get_circumfrence(self):
        '''
        This function will 
            - get the circumfrence of the Sphere object and return it 
        Paramaters 
            - self: Sphere object to get circumfrence from 
        '''
        c = 2 * math.pi * self.__radius  
        return round(c, 2)

    def get_surface_area(self):
        '''
        This function will 
            - get the surface area of the Sphere object and return it 
        Paramaters 
            - self: Sphere object to get surface area from 
        '''
        surface_area = 4 * math.pi * self.__radius ** 2 
        return round(surface_area, 2)

    def get_volume(self):
        '''
        This function will 
            - get the volume of the Sphere object and return it 
        Paramaters 
            - self: Sphere object to get volume from 
        '''
        volume= (4/3) * math.pi * self.__radius ** 3
        return round(volume, 2)

    def __str__(self):
        '''
        This function will 
            - Print out the attributes of a spher object
        '''
        return "Sphere: R=" + str(self.get_radius()) + ", C=" + str(self.get_circumfrence()) + \
            ", A=" + str(self.get_surface_area()) + ", V=" + str(self.get_volume())

    def __eq__(self, other):
        '''
        This function will
            - See if two sphere objects are equal 
        Paramaters 
            self: object being compared
            other: object being compared to
        '''
        if self.__radius != other.__radius:
            return False
        else:
            return True

    def __gt__(self, other):
        '''
        This function will
            - comapre two objects to see if self is greater than other
        Paramaters 
            self: object being compared
            other: object being compared to
        '''
        if self.__radius > other.__radius:
            return True
        else:
            return False
    
    def __ge__(self, other):
        '''
        This function will
            - comapre two objects to see if self is greater than or equal to other
        Paramaters 
            self: object being compared
            other: object being compared to
        '''
        if self.__radius > other.__radius or self.__radius == other.__radius:
            return True
        else:
            return False
    
    def __lt__(self, other):
        '''
        This function will
            - comapre two objects to see if self is less than other
        Paramaters 
            self: object being compared
            other: object being compared to
        '''
        if self.__radius < other.__radius:
            return True
        else:
            return False

    def __le__(self, other):
        '''
        This function will
            - comapre two objects to see if self is Less than or equal to other
        Paramaters 
            self: object being compared
            other: object being compared to
        '''
        if self.__radius < other.__radius or self.__radius == other.__radius:
            return True
        else:
            return False

def main():
    print(Sphere(8))

    #Equal to tests 
    print(Sphere(8)== Sphere(9))
    print(Sphere(8)== Sphere(8))
    print()

    #greater than and less than tests 
    print(Sphere(8) > Sphere(9))
    print(Sphere(8) < Sphere(9))
    print()

    #>= and <= test 
    print(Sphere(8) <= Sphere(9))
    print(Sphere(8) >= Sphere(9))
    
main()
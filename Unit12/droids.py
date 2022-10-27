'''
Author: Andrew Apollo  

This program will 
    - Declare a constant for each droid that will be made 
'''

PROTOCAL_DROID = ["p_head", "p_chassis", "p_right_arm", "p_left_arm", "p_lreft_leg", "p_right_leg"]
ASTROMECH_DROID = ["a_dome", "a_body", "a_left_leg", "a_center_leg", "a_right_leg"]

class Droid: 
    '''
    This class will
        - define a generic droid 
    '''
    __slots__ = ["__serial_num", "__droid_type", "__parts"]

    def __init__(self, serial_num, droid_type):
        '''
        This function will
            - Initialize fields of a droid 
        Paramaters
            - self: droid object
            - serial_num: serial number of the droid 
            - type; type of droid 
        '''
        self.__serial_num = serial_num
        self.__droid_type = droid_type
        self.__parts = []

    def needs_part(self, part):
        '''
        This function will 
            - check to see if there is a specific part needed 
        Paramters 
            - self: droid being checked 
            - part: object that is being checked if it is on teh droid 
        '''
        if part in self.__parts:
            return True
        else: 
            return False

    def install_part(self, part):
        '''
        This function will
            - Install a part onto teh droid
            - If the part is already installed it will not install the part
            - If the part is not for that type of droid it will not install the part
        Paramters 
            - self: droid part is being installed too
            - part: part being installed 
        '''
        if self.needs_part == True:
            self.__parts.append(part)
        else:
            raise ValueError("Part already installed or wrong part")

    def is_complete(self):
        '''
        This program will
            - check to see if the droid is complete
        Paramaters
            - self: droid being checked for completion 
        '''
        if self.__droid_type == PROTOCAL_DROID:
            if len(self.__parts) -1 == len(PROTOCAL_DROID) - 1:
                return True
            else: 
                return False
        elif self.__droid_type == ASTROMECH_DROID:
            if len(self.__parts) -1 == len(ASTROMECH_DROID) - 1:
                return True
            else: 
                return False

    def __repr__(self):
        '''
        This function will
            - print out a detailed list of a droid 
        Paramaters 
            - self: droid being printed 
        '''
        return  self.__droid_type + ":" + \
                "Serial number " + self.__serial_num + \
                self.__parts

    def __str__(self):
        '''
        This function will
            - return a compact string of the droid 
        Paramaters
            - self: droid being printed 
        '''
        return self.__serial_num + self.is_complete
'''
Author: Andrew Apollo 

This program will
    - Identifies clusters of the string passed in 
    - returns a set of (X, Y, Z) coordinite values in create_particles
'''

#Import Statements 
import random
from typing import Dict

def fusion(a_list):
    '''
    This function will 
        - Identifies clusters of the string passed in 
        - converts clusters to a key:value pair
        - and the length of teh key value

    Paramaters 
        -a_list: list being passed in
    '''
    sorted_list = sorted(a_list)
    sorted_list_copy = sorted_list[:]
    a_dictonary = {}

    for i in range(len(sorted_list)-1):
        if sorted_list[i + 1] == sorted_list[i] + 1:
            sorted_list_copy[i+1] = sorted_list_copy[i]

    for value in sorted_list_copy:
        if value in a_dictonary:
            a_dictonary[value] += 1
        else:
            a_dictonary[value] = 1

    return a_dictonary

def create_particles(max_coordinate):
    '''
    This function will 
        - returns a set of (X, Y, Z) coordinite values
        - cordinite values are random between 1 and max_coordinate

    Paramaters
        - max_coordinate: max coordinate value 
    '''
    n = max_coordinate ** 3
    lcv = 0
    particles = set()
    
    while lcv < n: 
        x = random.randint(0 , max_coordinate)
        y = random.randint(0 , max_coordinate)
        z = random.randint(0 , max_coordinate)
        particles.add((x , y, z))
        lcv += 1

    return particles

def build_dict_xy(a_set_particles):
    '''
    This function will
        - taek in a set of particles
        - get the (X, Y) of the particle and set it as the key 
        - append each Z to the key value it goes with
    '''
    a_dic = {}
    for i in a_set_particles: 
        key = i[0:2]
        value = i[2]
        try:
            a_dic[key].append(value)
        except KeyError:
            a_dic[key] = [value]

    return a_dic
    
def fusioned_particles(a_dictonary):
    '''
    This function will 
        - take in a dictonary 
        - find the "mega" particle using the fusion module
    
    Paramaters:
        - a_dictonary: dictonary being passed in 
    '''
    a_dic = {}
    for i in a_dictonary:
        key_list  = a_dictonary[i]
        fusion_call = fusion(key_list)
        for value in fusion_call:
            new_key = (i[0] , i[1], value)
            try:
                a_dic[new_key] += fusion_call[value]
            except KeyError:
                 a_dic[new_key] = fusion_call[value]

    return a_dic

def main():

    #Main took from document of 
    random.seed(1) 
    max_coordinate = 20 
    particles = create_particles(max_coordinate)
    print(particles)
    print("Total number of particles:" , len(particles))
    a_dict = build_dict_xy(particles)
    print(a_dict)

    fusioned_dict = fusioned_particles(a_dict)
    print("Mega particles whose weight is larger than 10:")
    for key in fusioned_dict:
        if fusioned_dict[key] > 10:
            print(key, ":" , fusioned_dict[key])
main()
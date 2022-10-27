'''
Author: Andrew Apollo

This program will
    - Make a database for pokemon
    - makje a pack of 10 pokemon
    
'''

#import staements 
import csv 
import random
from typing import Collection

def make_database(filename): 
    '''
    This function will
        - take in a file 
        - make a dictionary 
        - add tuples for pokemon from file 

    Paramaters 
        - filename: name of file being passed into function
    '''
    population = {} 
    with open(filename) as a_file:
        csv_file = csv.reader(a_file)
        next(csv_file)
        for line in csv_file:
            population[int(line[1])] = (line[0] , line[1], line[2])

        return population

def make_pack(database):
    '''
    This program will 
        - Take in a database of pokemon
        - Make a deck of 10 pokemon

    Paramaters  
        - database: database of pokemon made with male_database
    
    '''
    pack = set()
    while len(pack) < 10:
        randomNum = random.randint(1 , len(database))
        pack.add(database[randomNum]) 
    
    return pack

def build_basic_collection(database):
    '''
    This function will 
        - build a card collection with packs
        - adds cards to the collection
        - calculates the num of cards
    
    Paramaters  
        - database: database being passed in 
    '''
    card_collection = {}
    num = 0

    while len(card_collection) != len(database):
        pack = make_pack(database)
        num += 1
        for pokemon in pack:
            key = int(pokemon[1])
            card_collection[key] = pokemon           
            
    return card_collection , num
        
def build_counting_collection(database): 
    '''
    This function will
        - take in a database 
        - gets teh number of cards and number of times teh card shows up 
        - returns teh collection of cards the record of cards and total card count

    Paramaters 
        - database: database being passed in 
    '''
    collection = {}
    record = {}
    total_card_count = 0

    while len(collection) < len(database):
        pack = make_pack(database)
        for pokemon in pack: 
            key = int(pokemon[1])
            collection[key] = pokemon 
            total_card_count += 1
            try:
                record[key] += 1    
            except KeyError:
                record[key] = 1 

    return collection , record , total_card_count
        
def main():
    
    #test for activity 2 
    #print(make_database("data/pokemon.csv"))

    #test for actiivty 3
    #print(make_pack(make_database("data/pokemon.csv")))

    #test for part 4
    '''
    total = 0 
    lcv = 0
    while lcv < 1000:
        collection , num = build_basic_collection(make_database("data/pokemon.csv"))
        total += num
        lcv += 1
    print("Total = " , total // 1000)
    print(collection)
    '''
    collection , record , total_card_count = build_counting_collection(make_database("data/pokemon.csv"))
    most_times = 0 
    most_key = 0
    
    for key in range(1, 103):
        print(collection[key] , "Number of times:" , record[key])
        if record[key] > most_times:
            most_times = record[key]
            most_key = key
    
    print("Most:" , collection[most_key], "=",  most_times)
    print("Total:" , total_card_count)
main()
'''
This program will test functions in Drawings.py 

Author:Andrew Apollo 
'''
import drawings 

def test_valid_input_1(): # Function used to test if the number 1 is valid 
    valid = len(drawings.characters[1])
    assert (valid == 1)

def test_valid_input_2(): # Function used to test if the number 2 is valid 
    valid = len(drawings.characters[2])
    assert (valid == 1)

def test_valid_input_3(): # Function used to test if the number 3 is valid 
    valid = len(drawings.characters[3])
    assert (valid == 1)

def test_valid_input_4(): # Function used to test if the number 4 is valid 
    valid = len(drawings.characters[4])
    assert (valid == 1)

def test_valid_input_5(): # Function used to test if the number 5 is valid 
    valid = len(drawings.characters[5])
    assert (valid == 1)

def test_valid_input_6(): # Function used to test if the number 6 is valid 
    valid = len(drawings.characters[6])
    assert (valid == 1)

def test_valid_input_7(): # Function used to test if the number 7 is valid 
    valid = len(drawings.characters[7])
    assert (valid == 1)

def test_valid_input_8(): # Function used to test if the number 8 is valid 
    valid = len(drawings.characters[8])
    assert (valid == 1)

def test_valid_input_9(): # Function used to test if the number 8 is valid 
    valid = len(drawings.characters[9])
    assert (valid == 1)

def test_valid_input_A(): # Function used to test if the number 8 is valid 
    valid = len(drawings.characters['A'])
    assert (valid == 3)
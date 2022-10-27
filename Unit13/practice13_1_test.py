'''
Author: Andrew Apollo 

This program will
    - test the functions from practice13_1.py 
'''

#Imports
import practice13_1

def test_pig_latin_translator_she(): #Tests the word she 
    word = "she"
    outcome = practice13_1.pig_latin_translator(word)
    expectation = 'eshay'
    assert outcome== expectation

def test_pig_latin_translator_andrew(): #Tests the word andrew 
    word = "andrew"
    outcome = practice13_1.pig_latin_translator(word)
    expectation = 'andreway'
    assert outcome== expectation

def test_pig_latin_translator_the(): #Tests the word andrew 
    word = "the"
    outcome = practice13_1.pig_latin_translator(word)
    expectation = 'ethay'
    assert outcome== expectation
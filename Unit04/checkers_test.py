"""
This program is used to test the functions implimented into cheackers.py

Author: Andrew Apollo 

"""

#Imports 
import checkers

def test_draw_row_pix():
    row = checkers.draw_row_pix()
    assert(row == "true")
'''
Author: Andrew Apollo

This program will
    - Test cards.py and see if the functions are working properly 

'''

#Import statements
import cards

'''
def test_make_card():
    card = cards.make_card(14, "Clubs")
    rank = "Ace"
    suit = "Clubs"
    assert (card == (rank , suit))

def test_make_card_name():
    card = cards.make_card(14 , "Clubs")
    rank = "Ace"
    suit = "Clubs"
    assert ( card == "Ace of Clubs")
'''
def test_make_card_shorthand():
    card = cards.make_card(14 , "Clubs")
    rank = "Ace"
    suit = "Clubs"
    assert card == " AC"
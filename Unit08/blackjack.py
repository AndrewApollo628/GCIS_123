'''
Author: Andrew Apollo

This program will create a game of blackjack
'''
#Import Statements 
import cards

def hand_score(hand):
    '''
    This function will 
        - Take in a hand of cards 
        - Check the values of the hand and add the score
        - Then will return the score of the hand

    Paramaters
        - hand: hand being passed in
    '''
    score = 0
    
    if hand[0] == 2:
        score += 2
    if hand[4] == 2:
        score += 2
    if hand[0] == 3:
        score += 3
    if hand[4] == 3:
        score += 3
    if hand[0] == 4:
        score += 4
    if hand[4] == 4:
        score += 4
    if hand[0] == 5:
        score += 5
    if hand[4] == 5:
        score += 5
    if hand[0] == 6:
        score += 6
    if hand[4] == 6:
        score += 6
    if hand[0] == 7:
        score += 7
    if hand[4] == 7:
        score += 7
    if hand[0] == 8:
        score += 8
    if hand[4] == 8:
        score += 8
    if hand[0] == 9:
        score += 9
    if hand[4] == 9:
        score += 9
    if hand[0] == 10 or hand[0] == "Jack" or hand[0] == "Queen" or hand[0] == "King":
        score += 10
    if hand[4] == 10 or hand[4] == "Jack" or hand[4] == "Queen" or hand[4] == "King":
        score += 10
    if hand[0] == "Ace":
        if score <= 10:
            score += 11 
        elif score > 10:
            score += 1
    if hand[4] == "Ace":
        if score <= 10:
            score += 11 
        elif score > 10:
            score += 1
    
    return score

def main():
    hand = cards.make_card(11 , "Clubs") + cards.make_card(10 , "Clubs")
    print(hand)
    print(hand_score(hand))
main()
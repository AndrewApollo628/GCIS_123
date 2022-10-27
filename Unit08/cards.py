'''
Author: Andrew Apollo 

This program will 
    - create and return a new playing card using the given rank and suit.

'''
#Import statements
import random 
import sorts


def make_card(rank , suit): 
    '''
    This function will
        -  create and return a new playing card using the given rank and suit.

    Paramaters:
        - rank: rank of the card 2-14 
        - suit: what suit the card is "Spades, dimonds, hearts and clubs" 
    '''
    #If statements to set the rank of the card that is passed in 
    if rank == 2:
        rank = 2
    elif rank == 3:
        rank = 3
    elif rank == 4:
        rank = 4
    elif rank == 5:
        rank = 5
    elif rank == 6:
        rank = 7
    elif rank == 8:
        rank = 9
    elif rank == 10:
        rank = 10
    elif rank == 11:
        rank ="Jack"
    elif rank == 12:
        rank = "Queen"
    elif rank == 13:
        rank = "King"
    elif rank == 14:
        rank = "Ace"
    
    #If statements that 
    if suit == "Clubs":
        suit = "Clubs"
    if suit == "Hearts":
        suit = "Hearts"
    if suit == "Spades":
        suit = "Spades"
    if suit == "Dimounds":
        suit = "Dimounds"

    #Sets the name of the card with rank and suit 
    name = str(str(rank) + " of " + suit)

    numrank = ""
    suitrank = ""

    #if statements check to see what the rank is and sets it to a 2 character string
    if rank == 2:
        numrank = " 2"
    elif rank == 3:
        numrank = " 3"
    elif rank == 4:
        numrank = " 4"
    elif rank == 5:
        numrank = " 5"
    elif rank == 6:
        numrank = " 6"
    elif rank == 7:
        numrank = " 7"
    elif rank == 8:
        numrank = " 8"
    elif rank == 9:
        numrank = " 9"
    elif rank == 10:
        numrank = "10"
    elif rank == "Jack":
        numrank = " J"
    elif rank == "Queen":
        numrank = " Q"
    elif rank == "King":
        numrank = " K"
    elif rank == "Ace":
        numrank = " A"

    #If statements check the suit and set it to a single character 
    if suit == "Clubs":
        suitrank = "C"
    if suit == "Hearts":
        suitrank = "H"
    if suit == "Spades":
        suitrank = "S"
    if suit == "Dimounds":
        suitrank = "D"

    shorthand = str(numrank + suitrank) #Puts the characters together from the if statements
    
    '''
    if suitrank == "C" or suitrank == "S": #Prints Suits Clubs or spades blue 
        print("\033[34m" , shorthand , "\033[37m")
    else: #Prints Suits Hearts or Dimounds red
        print("\033[31m", shorthand ,"\033[37m")
    '''
    return rank, suit, name, shorthand

def make_deck():
    '''
    This function will
        - Make a deck of cards by iterating through make_card
    '''
    i = 2
    deck = []
    while i < 15:
        deck.append(make_card(i , "Clubs"))
        deck.append(make_card(i , "Hearts"))
        deck.append(make_card(i , "Spades"))
        deck.append(make_card(i , "Dimounds"))
        i += 1

    return deck
    
def shuffle(deck):
    '''
    This function will
        - Shuffle the deck of cards passed in by deck

    Paramaters
        - Deck: Deck of cards to be shuffled
    '''
    for index in range(len(deck)):
        j = random.randint(0 , 51)
        sorts.swap(deck , index , j)
    return deck

def draw(deck , hand):
    '''
    This function will
        - Create a hand 
        - Draw a card out of the deck and put the card into your hand

    Paramaters
        - deck: deck of cards made from make_deck
        - hand: list where cards from deck will be placed
    '''
    hand = []
    if len(deck) == 0:
        return None
    else:
        hand = deck.pop(random.randint(0 , len(deck)))
        return hand 

def deal(deck , numcards):
    '''
    This function will
        - make 2 hands
        - will add a card in each hand for the number cards

    Paramaters
        - deck: deck passed in by make_deck
        - numcards: number of cards in each deck
    '''
    hand_1 = []
    hand_2 = []
    deck = shuffle(deck)
    index = 0
    
    while index < numcards:
        hand_1.append(deck.pop())
        hand_2.append(deck.pop())
        index += 1

    return ("Deck 1: " , hand_1 , "Deck 2: " , hand_2)

def cut(deck):
    '''
    This program will
        - Take in a deck of cards 
        - Cut the deck into 2 seperate decks 
    
    Paramaters
        - deck: deck of cards being passed in 
    '''
    if len(deck) == 1 or len(deck) == 0:
        return ValueError
    d1 = slice(0,len(deck)//2)
    d2 = slice(len(deck)//2, len(deck))
    
    top_half = deck[d1]
    bottom_half = deck[d2]
    
    return "Deck 1: " , top_half ,  "Deck 2: " , bottom_half

def main():
    #make_card(14, "Clubs")
    #make_card(3,"Hearts")
    #print("\033[31m", make_card(14, "Clubs") ,"\033[37m")
    #print(make_deck())
    #print(shuffle(make_deck()))
    #print(draw(make_deck() , 1))
    #print(deal(make_deck() , 7))
    deck = make_deck()
    print(cut(deck))
main()
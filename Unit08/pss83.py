import cards

# helper function
def print_shorthand(cards):
    for card in cards:
        print(card[3], end=" ")
    print()

"""
Problem 1
"""
def slices():
    deck = cards.make_deck()
    print_shorthand(deck)

    # first 5 cards
    first_five = deck[:5]
    print_shorthand(first_five)

    # last 5 cards in the deck
    length = len(deck)
    last_five = deck[length-5:]
    print_shorthand(last_five)

    # the centermost 5
    length = len(deck)
    center = length // 2
    center_five = deck[center-2:center+3] # may also use -3/+2
    print_shorthand(center_five)

    # first third
    length = len(deck)
    third = length // 3
    first_third = deck[:third]
    print_shorthand(first_third)

    # every other
    every_other = deck[::2]
    print_shorthand(every_other)

"""
Problem 2
There are several ways to potentially accomplish this. This is written to
most closely match the instructions.
"""
def win_lose_or_draw(p_score, d_score):
    # if both bust, it's a draw
    if (p_score > 21 and d_score > 21):
        print("Game ends in a draw.")
    # if both scores are equal, it's a draw
    elif p_score == d_score:
        print("Game ends in a draw.")
    # if the player busts, the dealer wins
    elif p_score > 21:
        print("Dealer wins.")
    # if the dealer busts, the player wins
    elif d_score > 21:
        print("You win!")
    # if the dealer's score is higher, the dealer wins
    elif d_score > p_score:
        print("Dealer wins.")
    # player's score must be higher than the dealer's score
    else:
        print("You win!")

"""
Problem 3
Again, there are several ways to do this, but this most closely matches the
instructions.
"""
def dealer_hit_or_stand(p_score, d_score):
    # if player has busted, stand
    if p_score > 21:
        return False
    # if the dealer is under 17 or has a lower score, hit
    elif d_score < 17 or d_score < p_score:
        return True
    # otherwise, stand
    else:
        False

"""
Problem 4
This algorithm assumes that there is only one Ace in the hand. This will not
be the case in the assignment.
"""
def hand_score(hand):
    score = 0
    ace = False
    for card in hand:
        rank = card[0]
        if rank <= 10:
            score += rank
        elif rank < 14:
            score += 10
        else:
            ace = True
    
    if ace:
        if score + 11 < 21:
            score += 11
        else:
            score += 1
    
    return score


def main():
    slices()

if __name__ == "__main__":
    main()
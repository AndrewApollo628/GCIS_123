'''
Author: Andrew Apollo 

This program will prompt the user to enter didgits and compare it to 
the first 100 didgits od PI
'''


#Global Varibles 
PI = '3 1 4 1 5 9 2 6 5 3 5 8 9 7 9 3 2 3 8 4 6 2 6 4 3 3 8 3 2 7 9 5 0 2 8 8 4 1 9 7 1 6 9 3 9 9 3 7 5 1 0 5 8 2 0 9 7 4 9 4 4 5 9 2 3 0 7 8 1 6 4 0 6 2 8 6 2 0 8 9 9 8 6 2 8 0 3 4 8 2 5 3 4 2 1 1 7 0 6 7 9'


def pi_tester():
    '''
    This function will 
       -Accept user input (up to 100 inputs) and compare the input to the first 100 didgits of PI
       -If the input is correct it will ask for the next Didgit 
       -If the input is wrong it will print the correct Didgit
       -keep track of the correct answers and return the total

    '''
    letter = input("Enter didgit of PI: ")
    total = 0
    
    for compare_letter in PI.split():#Letters split from PI become compare_letter 
    
        if total <= 100:
            if letter == compare_letter:#compares letters 
                letter = input("Enter Next digit: ")
                total = total +1
               
            else:
                print("Incorrect Letter the correct Letter is " , compare_letter)
                display_score(total)#takes in the Display_score function and passes total as the score           
                break

    return total

def display_score(score):
    '''
    This function 
        -calculates the score from pi-tester 
        -assigns the player a Level based on the score 

    Paramaters 
        Score: used to evalute the players level 
    '''

    if score <= 4:
        print("Score is " , score, ":" , " Level is PI Neophyte")
    elif 5 < score < 9:
        print("Score is " , score, ":" , " Level is PI Novice")
    elif 10 < score < 24:
        print("Score is " , score, ":" , " Level is PI Journeymen")
    elif 25 < score < 49:
        print("Score is " , score, ":" , " Level is PI Enthusiast")
    elif 50 < score < 96:
        print("Score is " , score, ":" , " Level is PI Connoisseur")
    elif 97 < score < 100:
        print("Score is " , score, ":" , " Level is PI Expert")
    elif score > 100:
        print("Score is " , score, ":" , " Level is PI Imposter")

def main():

    pi_tester()
    
main()

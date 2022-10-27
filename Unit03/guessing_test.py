'''
Author: Andrew Apollo 

This program will take in input from a user and check to see if the input is the number the user is supposed to guess 
'''
import random

def check_guess(correct , guess): #sets the answer and the guess 
    

    if int(guess) < 1: #if statement to print if the guess is out of range 
        print("Guess out of range")
    

    if int(guess) > 10:  #if statement to print if the guess is out of range 
        print("Guess out of range")
       

    if int(guess) < correct:  #if statement to print if the guess is lower than the answer  
        print("Too low")
 
    
    if int(guess) > correct:  #if statement to print if the guess is higher than the answer  
        print("Too high")
    

    if int(guess) == correct: #if statement to print of the guess is correct 
        print("correct")
        return main()
    
def main():
    randomnum = random.randint(1,10)

    check_guess(randomnum, int(input("Enter Guess: ")))# sets the answer to have random number and gets input from the user
    
    check_guess(randomnum, int(input("Enter Guess: ")))# sets the answer to have random number and gets input from the user
    
    check_guess(randomnum, int(input("Enter Guess: ")))# sets the answer to have random number and gets input from the user
    
    print("The answer is :" , randomnum) # prints the correct answer 
    print("GameOver!")
    
main()


#all tests that have been done 
def test_check_guess_range_low(): #tests to see if the guess is lower than 1
    guess = check_guess(5,0)

    assert (guess == "none")

def test_check_guess_range_high(): #tests to see if the guess is higher than 10
    guess = check_guess(5,11)

    assert (guess == "one")

def test_check_guees_lower_correct(): #tests to see if the guess is lower than the answer 
    guess = check_guess(5,4)

    assert (guess == "low")

def test_check_guees_higher_correct(): #tests to see if the guess is higher than the answer 
    guess = check_guess(5,6)

    assert (guess == "high")

def test_check_guees_correct():#tests to see if the guess is = to the answer 
    guess = check_guess(5,5)

    assert (guess == "correct")
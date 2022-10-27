#Author Andrew Apollo

import random

def is_correct(answer , guess):
    return (guess == answer)

def check_guess(guess,answer):
    if (guess < 1 or guess > 10):
       return (-1)
    elif (answer - guess) >=0:
        return (answer - guess)
    else:
        return (guess - answer)

def main(): 
    choice = random.randint(1,10)
    responce = int(input("Please enter a number: "))
    result = is_correct(responce,choice)
    if result < 0:
        print("Guess out of range game over!")
    elif result == 0:
        print("You guessesd the number")
    else:
        print("your guess was " , str(result) , "away from the answer")
    

#main()

if __name__ == "__main__":
        main()

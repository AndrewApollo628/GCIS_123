'''
Author: Andrew Apollo

This program will take in values and divide them and return a string 
 '''

def precise_divison(numerator , denominator , precision):
    '''
    This function takes in vlaues for the paramaters and divides them and return the value as a sting

    Paramaters
      numerator: is the numerator of the divison problem
      denominator: is the denominator of the division problem 
      precison: is the remainder of Numerator/dominator 
    '''
    precision  = numerator % denominator
    answer = (numerator) / (denominator / precision)
    print (answer)
    return answer

def main():
    numbers = input("Enter divison numbers: ")
    num = numbers.split() #splits the numbers  

    n = num[0]#assigns N to as the first number in the string 
    d = num[1]#assigns d to as the second number in the string 
    p = num[2]#assigns p to as the third number in the string 

    precise_divison(int(n) , int(d) , int(p))


main()
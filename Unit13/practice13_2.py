'''
Author: Andrew Apollo 

This prograsm will
    - Checks to see if a number is divisible by 3 or 5 
'''
#Imports
import arrays

number_list = []

def num_check(k= 0, n=0):
    '''
    This function will 
        - Check to see if a number is divisible by 5 or 3 but not both 
        - if it is divisible it will add it to a list
    Paramaters
        - k: number being checked 
        - n: last number to be checked 
    '''
    if k > n:
        return number_list

    if 3<=k and k<=n:
        if k%5 ==0 and k%3 ==0:
            k+=1
            num_check(k, n)
        elif k%5 ==0 or k%3 ==0:
            number_list.append(k)
            k += 1
            num_check(k,n)
        else:
            k +=1
            num_check(k,n) 
    return number_list

def find_words(filename, letter, number):
    '''
    This function will
        - look for words in a file 
        - see what words start with the letter 
        - add the word to an array
    Paramaters
        - filename: name of file being opened
        - letter: letter being looked for
        - number: size of array
    '''
    index = 0
    an_array = arrays.Array(number)
    with open(filename) as file:
        for line in file:
            for word in line.split():
                if word[0] == letter:
                    if index < number:
                        an_array[index] = word
                        index += 1
   
    return an_array 

def make_month(weekday, num_days):
    '''
    This function will
        - Create a calander givin the start date
        - and givin the number of days 
    Paramaters 
        - weekday: weekday month is starting on
        - num_days: total number of days in the month
    '''
    start_date = get_day(weekday)
    lcv = 1
    
    month = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ']]

    for week in month:
        for day in week:
            if start_date < 7 and lcv < num_days+1:
                week[start_date] = lcv
                start_date += 1
                lcv +=1
        start_date = 0
        print(week, sep=" ")

def get_day(day):
    '''
    This function will
        - get the day of the week
    Paramaters
        - day: day of the week to get
    '''
    if day.lower() == "sunday":
        num = 0 
    elif day.lower() == "monday":
        num = 1
    elif day.lower() == "tuesday":
        num = 2
    elif day.lower() == "wednesday":
        num = 3
    elif day.lower() == "thursday":
        num = 4
    elif day.lower() == "friday":
        num = 5 
    elif day.lower() == "saturday":
        num = 6

    return num

def main():
    '''
    print(num_check(3, 20))

    print(find_words("data/atotc.txt", "a", 5))
    '''

    make_month("monday", 31)

if __name__ == "__main__":
    main()
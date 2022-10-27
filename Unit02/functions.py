'''
Author: Andrew Apollo 

This program promts the user to enter information and then calculates and prints the rsult

'''

def main():

    #Asking user for current values for year and month 
    current_Year = input("What is the current year? ")
    current_Month = input("What is the current month (in number form)? ")
   
    #Asking user for user birth year and month 
    birth_Year = input("What year were you born? ")
    birth_month = input("What month were you born (in number form)? ")

    #Calculating age in months and prining it 
    print("Your age in months: ", (int(current_Year) - int(birth_Year)) * 12 + (int(current_Month) - int(birth_month)))

    days_per_month = 30.4 #setting average days per month 

    #Asking for current month and day 
    month = input("Enter the month: ")
    day = input("Enter the day of the month: ")

    #calculating the approximate day of the year 
    print("The approximate day of the year is: ", (int(month) * int(days_per_month) + int(day)))

main()
#Author: Andrew Apollo 

def countdown(number):
    lcv = number 
    sum = 0
    while lcv >= 0:
        print(str(lcv))
        if number != -1:
            sum = sum + lcv
        lcv = lcv - 1
    print ("Sum: " , str(sum))

def print_range(a_range):
    index = 0
    while index < len(a_range):
        print(a_range[index], end= " ")
        index += 1
    print()

def main():
    print_range(range(0, 11))
    print_range(range(0, 21 , 2))
    print_range(range(5, 16 , 2))
    print_range(range(10, -1,-1))
    countdown(5)
main()
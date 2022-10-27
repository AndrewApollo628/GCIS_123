#Author:Andrew Apollo 

def numbers():
    total_sum = 0
    while True:
        filename = input("Enter file name: ")
        if filename == "":
            break
        try:
            with open(filename) as file:
                sum = 0
                for number in file:
                    try:
                        number = number.strip()
                        sum += int(number)
                    except:
                        print("Skipping non numeric data ", number)
                print("Sum of numbers" , sum)
                total_sum += sum
        except FileNotFoundError:
            print("File does not exist: " , filename) 
        '''
        except ValueError:
            print("File contains non-numeric data. ") 
        '''                 
    print("Total sum: " , total_sum)

def divison():
    errors = 0
    while True:
        numerator = input("Enter numerator: ")
        denominator = input("Enter a denominator: ")

        if numerator == "" or denominator == "":
            break
        
        try:
           numerator = float(numerator)
           denominator = float(denominator)
           
           print("Result of divison = ", (numerator / denominator))
        except ValueError as ve:
            errors += 1
            if errors >= 3:
                raise ve
            print("Non-numeric value entered ")
        except ArithmeticError as ae:
            errors += 1
            if errors >= 3:
                raise ae
            print("Cant divide by 0")

def password():
    paswsd = input("Enter password: ")
    length =len(paswsd)
    if length < 10 or length > 20:
        raise ValueError("Passwod must be between 10 and 20 characters")
    
    confirm = input("Confirm your password: ")
    if paswsd != confirm:
        raise ValueError("Passwords do not match!")

    

def main():
    
    #numbers() #no exception handleing 
    divison()
    #password()

main()

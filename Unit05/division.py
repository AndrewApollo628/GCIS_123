#Author: Andrew Apollo 

def divison():
    while True:
        numerator = input("Enter numerator: ")
        denominator = input("Enter a denominator: ")

        if numerator == "" or denominator == "":
            break
        
        try:
           numerator = float(numerator)
           denominator = float(denominator)
           
           print("Result of divison = ", (numerator / denominator))
        except ValueError:
            print("Non-numeric value entered ")
        except ArithmeticError:
            print("Cant divide by 0")

def main():
    divison()
main()
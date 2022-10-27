#author: Andrew Apollo 

PI = 3.14159

def add(firstnum , secondnum ):
    return firstnum + secondnum

def subtract(firstnum , secondnum):
    return firstnum - secondnum

def multipy(firstnum , secondnum):
    return firstnum * secondnum

def divide(firstnum,secondnum):
    return firstnum / secondnum

def circumference(radius):
    return 2 * PI * radius

def area_of_circle(radius):
    return PI * radius ** 2

def main():
    num1 = int(input("First num: "))
    num2 = int(input("Second num: "))
    rad = float(input("Enter the radius of a circle: "))
    
    sum = add(num1,num2)
    diffrence = subtract(num1,num2)
    product = multipy(num1,num2)
    div = divide(num1,num2)
    cir = circumference(rad)
    area = area_of_circle(rad)
   
    print(sum)
    print(diffrence)
    print(product)
    print(div)
    print(cir)
    print(area)

main()
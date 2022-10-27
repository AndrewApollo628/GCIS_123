'''
Author: Andrew Apollo 

This program will ask for user input for radius, height and width and will use that informaton to calculate area and volume for varoius shapes.

'''
def main():

    def area_of_circle(): # Area of a circle function
    
        PI = 3.14592 #setting the value of PI
        radius = input("Enter the radius: ")
        formula_area_circle = (float(radius) ** 2 * float(PI)) # Formula for area of a circle 
    
        print("Circle: ", "r = ",radius, "," , "Area = ", formula_area_circle ) # prints the information of the circle 

    area_of_circle()


    def volume_of_sphere(): #Volume of a sphere function
    
        PI = 3.14592 #setting the value of PI
        radius_s = input("Enter the radius : ")
        formula_vol_sphere = ((float(radius_s) ** 3) * (4 / 3 * PI)) #Formula for volume of a shere 
    
        print("Sphere", "r =", radius_s, "," , " volume = ", formula_vol_sphere) #prints the information of the sphere

    volume_of_sphere()


    def area_of_rectangle():

        height_r = input("Enter the height: ") 
        width_r = input("Enter the width: ")
        formula_area_recatngle = (int(height_r) * int(width_r)) #Formula for area of rectangle 

        print("Recatngle: ", "height = ", height_r, "," , "width = ", width_r, "," , "area = ", formula_area_recatngle) #prints information of the Rectangle 

    area_of_rectangle()


    def area_of_square(): #Area of square function 
    
        side_s = input("Enter the side length: ")
        formula_area_square = ( int(side_s) ** 2) #formula for area of a square 

        print("Square: ", "side length = ", side_s, ",", "The area of thw square is: ", formula_area_square) #Prints the information of the square 

    area_of_square()


    def area_of_ITtriangle(): #Area of a isosceles triangle
    
        length_i = input("Enter the side length: ")
        height_i = input("Enter the height: ")
        formula_area_ITriangle = (float(length_i) * float(height_i) / 2 ) #Area formula for isosceles triangle 
    
        print("Isosceles Tringle: ", "side = ", length_i, "," , "height = ", height_i, "," , "area =  ", formula_area_ITriangle) #Prints the informtion of the isosceles triangle

    area_of_ITtriangle()


    def area_of_EqTriangle(): #Area of a eqilateral triangle 
    
        side_e = input("Enter teh side Length: ")
        formula_area_EqTriangle = ((3 ** 0.5 / 4) * (float(side_e) ** 2)) #Area formula for an Equilateral triangle 

        print("Equilateral Triangle: ", "side = ", side_e, "," , "area = ", formula_area_EqTriangle) #Prints information about the  eqilateral triangle

    area_of_EqTriangle()

    def area_of_trapezoid(): # Area of trapiziod function 

        base_1 = input("Enter base 1: ")
        base_2 = input("Enter base 2: ")
        height_t = input("Enter height: ")
        formula_area_trapizoid = ((float(base_1) + float(base_2)) / 2 * float(height_t)) #Formula for area of a trapiziod 

        print("Trapizoid: ", "base 1 =", base_1, "," , "base 2 = ", base_2, "," , "height = ", height_t, "," , "area = ", formula_area_trapizoid ) #prints information of trapizoid 

    area_of_trapezoid()


main()

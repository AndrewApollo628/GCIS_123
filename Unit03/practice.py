'''
Author: Andrew Apollo 

This program will take in the users height in inches and convert it to feet
Thisa program also takes Km and converts it to Miles , feet and in 
This program draws a snowman 
'''
import turtle 

def convert_height():
    height = input("Enter your height in inches: ")
    feet_tall = int(height)//12 #Calculates the ft part of the height   
    inches_tall = int(height)%12 #Calculates the in part of the height 

    print("You are " , feet_tall , "' " , inches_tall , '"' , " tall" , sep =(""))



def convert_distance(kilometers):
    miles = int(kilometers) * 39370.1 / 63360 #converts KM to MI 
    feet = int(kilometers) * 39370.1 % 63360 // 12 #converts teh remainder of Mi to Ft
    inches = feet % 12  #converts the remander of ft to in 
    

    print(kilometers , "kilometers is ," , int(miles) , "miles , " , int(feet) , "feet ,", int(inches) , "inches")

def snow_man( x , y , bottomradius): #draws the snowman 
    turtle.up()
    turtle.goto( x , y)
    turtle.down()
    draw_circle(bottomradius)
    draw_circle(bottomradius * .75)
    draw_circle(bottomradius * .5625)
    turtle.hideturtle()
    
    
    
def draw_circle(radius ): #creates a helperfunction to draw a circle 
    turtle.bgcolor("cyan")
    turtle.fillcolor("white")
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.up()
    turtle.left(90)
    turtle.forward(radius * 2)
    turtle.down()
    turtle.right(90)
    


def main():
    convert_height()

    convert_distance(123.5)
    convert_distance(60)
    convert_distance(96.56061)
    
    snow_man(0 , -200 , 100)
    
    input( "Press enter to exit: " )
main()
'''
Author: Andrew Apollo 

This program will draw squares inside on each square that is previously drawn 

'''

import turtle
import math

def draw_squares(side): #sets side to be paramater of draw_squares
   
   inner_squares(side , "red")
   turtle.left(45)
   side2 = math.sqrt((side/2) ** 2 + (side/2)**2) #gets the side length for side 2 
   inner_squares(side2, "orange")
   turtle.left(45)
   side3 = math.sqrt((side2/2) ** 2 + (side2/2)**2) #gets the side length for side 3
   inner_squares(side3, "yellow")
   turtle.left(45)
   side4 = math.sqrt((side3/2) ** 2 + (side3/2)**2)#gets the side length for side 4
   inner_squares(side4, "green")
   turtle.left(45)
   side5 = math.sqrt((side4/2) ** 2 + (side4/2)**2)#gets the side length for side 5
   inner_squares(side5, "blue")
   turtle.left(45)
   side6 = math.sqrt((side5/2) ** 2 + (side5/2)**2)#gets the side length for side 6
   inner_squares(side6, "purple")   
   
   print("smallest square length is: " , side6)
   return side6
   
   print("smallest square length is: " , side6)

def inner_squares(length, color): # sets the paramaters and codes the turtle to draw a square 
   
   turtle.fillcolor(color)
   turtle.begin_fill()
   turtle.forward(length)
   turtle.left(90)
   turtle.forward(length)
   turtle.left(90)
   turtle.forward(length)
   turtle.left(90)
   turtle.forward(length)
   turtle.left(90)
   turtle.forward(length/2)
   turtle.end_fill()

def main():
   
   draw_squares(200) #draws all sqaures from the users input 
   input("press enter to exit")
      
main()

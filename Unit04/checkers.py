'''
This program will use my pixart.py program and draw a 20x20 checkerboard 

Author: Andrew Apollo 

'''

#Imports
import pixart
import turtle

def draw_cheacker_board(): 
    '''
    This function takes in helper functions and creates the cheackerboard 
    using a while loop
    '''
    control = 0 

    turtle_start_point(-300 , 300)

    while control < 10: #
       draw_row1_pix()
       new_row()
       draw_row2_pix()
       new_row()
       control = control + 1

def draw_row1_pix():
    '''
    This function draws a single row of pixels 20 pixels long with alternating red 
    and black colors starting with red 
    '''
    lcv  = 0
    while lcv < 10 :
       pixart.draw_pixel_by_code("0") 
       pixart.draw_pixel_by_code('2')
       lcv = lcv + 1
       #return "true"

def draw_row2_pix():
    '''
    This function draws a single row of pixels 20 pixels long with alternating red 
    and black colors starting with red 
    '''
    lcv  = 0
    while lcv < 10 :
        pixart.draw_pixel_by_code("2") 
        pixart.draw_pixel_by_code('0')
        lcv = lcv + 1
        
def new_row():
    '''
    This function will move the turtle back to start a new row of pixels 
    '''
    turtle.left(180)
    turtle.forward(pixart.PIXEL_SIZE *20)
    turtle.left(90)
    turtle.forward(pixart.PIXEL_SIZE)
    turtle.left(90) 

def turtle_start_point(x , y):
    '''
    This function will move the turtle to the right spot to begin drawing 
    also sets the speed of the turtle 
    Paramaters:
        x: X coordinit of the turtle
        Y: Y coordinit of the turtle
    '''
    turtle.speed(500)
    turtle.up()
    turtle.goto(x,y)
    turtle.down()

def main():
   draw_cheacker_board()
   input("Press Enter to exit: ")
main()
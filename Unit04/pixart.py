'''
This program initattes a turtle and draws a pixel 

Author: Andrew Apollo 
'''
#Imports 
import turtle

#Global Varibles 
PIXEL_SIZE = 30
ROWS = 20
COLUMNS = 20

def init():
    '''
    This function Initates the starting paramaters of the Turtle 
    '''
    turtle.penup()
    turtle.goto(-300,300)
    turtle.speed(100)
    #turtle.pencolor("black")
    #turtle.fillcolor("white")

def draw_pixel():
    '''
    This function Draws a single pixel using turtle 
    '''
    lcv = 0 
    turtle.begin_fill()
    turtle.pendown()
    while lcv < 4:
        turtle.forward(PIXEL_SIZE)
        turtle.right(90)
        lcv = lcv +1 
    turtle.penup()
    turtle.end_fill()
    turtle.forward(PIXEL_SIZE)

def draw_pixel_by_code(color):
    '''
    This function will draw a single pixel with the color coming from a supplied character 
    
    Paramaters: 
         color: determines the color based on the supllied character 
    '''

    #if/elif statements will compare supplied char to determine fill color 
    if color == '0': #0 = black 
        turtle.fillcolor('black')
        #return "0"
    elif color == '1': #1 = white 
        turtle.fillcolor('white')
        #return "1"    
    elif color == '2': #2 = red
        turtle.fillcolor('red')
        #return "2"
    elif color == '3': #3 = yellow
        turtle.fillcolor('yellow')
        #return "3"
    elif color == '4': #4 = orange 
        turtle.fillcolor('orange')
        #return "4"
    elif color == '5': #5 = green
        turtle.fillcolor('green')
        #return "5"
    elif color == '6': #6 = yellowgreen
        turtle.fillcolor('yellowgreen')
        #return '6'
    elif color == '7': #7 = sienna 
        turtle.fillcolor('sienna')
        #return '7'
    elif color == '8': #8 = tan
        turtle.fillcolor('tan')
        #return '8'
    elif color == '9': #9 = grey
        turtle.fillcolor('grey')
        #return '9'
    elif color == 'A': #A = darkgrey
        turtle.fillcolor('darkgrey')
        #return 'A'

    #Staements draw a single pixel 
    lcv = 0 
    turtle.pendown()
    turtle.begin_fill()
    while lcv < 4:
        turtle.forward(PIXEL_SIZE)
        turtle.right(90)
        lcv = lcv +1 
    turtle.penup()
    turtle.end_fill()
    turtle.forward(PIXEL_SIZE)

#4.3.2 Class Activity 
def move(row ,col):
    #return 0 

    #xcor
    xcor = -COLUMNS/2*PIXEL_SIZE
    xcor += PIXEL_SIZE*col
    #ycor
    ycor = ROWS/2*PIXEL_SIZE
    ycor -= PIXEL_SIZE*row
    turtle.setpos(xcor,ycor)

def main():
    #draw_pixel()
    draw_pixel_by_code('6')
    input("Press enter to exit: ")

if __name__ == "__main__":
    main()

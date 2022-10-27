'''
This program will take in a string and draw pixels based on the value of the string and what color that value represents
Author: Andrew Apollo 
'''
#Import Statements 
import turtle
import pixart 

#global varibles 
characters = ""

def user_input():
    '''
    This function loops user input and then breaks if user inputs nothing
    '''

    while True:
       characters =  input("enter chars: ")
       
       if characters == "":
        break

def draw_row_string():
    '''
    This function draws a row of pixels based on the input of colors 
    ''' 
    user_input()
    lcv = 0
    turtle_init(-300,300,500)
    while (lcv < len(characters)):
        pixart.draw_pixel_by_code(characters[lcv])
        lcv = lcv + 1

        if lcv == 20:
            next_row()
        if lcv == 40:
            next_row()
        if lcv == 60:
            next_row()
        if lcv == 80:
            next_row()        
        if lcv == 100:
            next_row()
        if lcv == 120:
            next_row()
        if lcv == 140:
            next_row()
        if lcv == 160:
            next_row()
        if lcv == 180:
            next_row()        
        if lcv == 200:
            next_row()  
        if lcv == 220:
            next_row()
        if lcv == 240:
            next_row()
        if lcv == 260:
            next_row()
        if lcv == 280:
            next_row()        
        if lcv == 300:
            next_row()
        if lcv == 320:
            next_row()
        if lcv == 340:
            next_row()
        if lcv == 360:
            next_row()
        if lcv == 380:
            next_row()        
        if lcv == 400:
            next_row()      

def next_row():
    '''
    This function tells the turtle to go to the next row 
    
    '''
    turtle.left(180)
    turtle.forward(pixart.PIXEL_SIZE * 20)
    turtle.left(90)
    turtle.forward(pixart.PIXEL_SIZE)
    turtle.left(90)
    
def turtle_init(x,y,speed):
    '''
    This function initalizes the turtle 

    paramaters:
        X: Xcord 
        Y: Ycord 
        Speed: speed of turtle
    
    '''
    turtle.speed(speed)
    turtle.up()
    turtle.goto(x,y)
    turtle.down()

    #if statements validate inputed Characters 
    '''
    if characters[1]:
        return "true"
    elif characters[2]:
        return "true"
    elif characters[3]:
        return "true"
    elif characters[4]:
        return "true"
    elif characters[5]:
        return "true"
    elif characters[6]:
        return "true"
    elif characters[7]:
        return "true"
    elif characters[8]:
        return "true"
    elif characters[9]:
        return "true"
    elif characters['A']:
        return "true"
    '''
def main():
    '''
    This function runns all functions within the file 
    '''
    
    draw_row_string()
    input("press enter to stop program: ")
    
if __name__ == "__main__":
    main()

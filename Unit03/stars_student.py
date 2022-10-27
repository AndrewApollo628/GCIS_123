"""
Draws a sky filled with stars and planets.

@author: Andrew Apollo
"""

import random
import turtle

def tweak(speed, tracer):
    """
    Adjust the turtle's speed and tracer settings so that it can be sped up
    or slowed down as needed for visual debugging.
    """
    turtle.speed(speed)
    turtle.tracer(tracer)

def random_yellow():
    """
    Sets the turtle's fill color to a random shade of yellow using RGB values.
    """
    # the random.random() function returns a floating point value between
    # 0.1 and 1.0. This expression guarantees that the red value will be
    # between 0.5 and 1.0.
    red = 0.5 + random.random() * 0.5
    green = red
    blue = red / 2

    # the turtle color can be set using RGB values ranging from 0.0 to 1.0. In
    #  this case the red and green values are between 0.5 and 1.0 and the blue
    # value is half the value - this guarantees a shade of yellow.
    turtle.color(red, green, blue)
    turtle.fillcolor(red, blue, green)

def random_move():
    """
    Moves the turtle to a random location and orientation on the screen.
    """
    x = random.randint(-1000, 1000)
    y = random.randint(-1000, 1000)
    '''
    Syntax error 
    Missing the , between -1000 and 1000. 
    vs code highlighted the problem 
    '''
    turtle.goto(x, y)
    '''
    Semantic error 
    The y was left out of the cordinate 
    found by looking at the code and it didnt look right
    ''' 

    angle = random.randint(0, 360)

def draw_star(x , y , length, angle): #sets new peramaters for draw star
    '''
    Syntax error 
    Missing the : after the function definition
    vs code highlighted the problem
    '''
    """
    Draws a star at the turtle's current location and orientation.
    """
    turtle.pencolor("yellow")
    '''
    Runtime error 
    set color to yellow 
    vs code would not execute the program because the color was not getting a value
    '''
    right_angle = 108 #sets the angle of 108 for the turtle to move right 
    left_angle= 36 #sets the angle of 36 for the turtle to move left
    
    turtle.up()
    turtle.goto(x,y)
    turtle.right(angle)

    turtle.down()
    turtle.fillcolor("yellow")
    turtle.begin_fill()

    turtle.forward(length)
    turtle.left(left_angle)
    turtle.forward(length)
    turtle.right(right_angle)

    turtle.forward(length)
    turtle.left(left_angle)
    turtle.forward(length)
    turtle.right(right_angle)

    turtle.forward(length)
    turtle.left(left_angle)
    turtle.forward(length)
    turtle.right(right_angle)

    turtle.forward(length)
    turtle.left(left_angle)
    turtle.forward(length)
    turtle.right(right_angle)

    turtle.forward(length)
    turtle.left(left_angle)
    turtle.forward(length)
    turtle.right(right_angle)

    turtle.end_fill()    

def random_star():
    draw_star(random.randint(-200,200) ,random.randint(-200,200) , random.randint(5,10) , random.randint(-90, 90))

def draw_world(x,y,radius,fill):
    
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.fillcolor(fill)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_celestial_bodies():
    #draw 3 random palnets 
    draw_world(random.randint(-200 , 200), random.randint(-200 , 200) , random.randint(50 , 200), "blue" )
    draw_world(random.randint(-200 , 200), random.randint(-200 , 200) , random.randint(50 , 200), "red" )
    draw_world(random.randint(-200 , 200), random.randint(-200 , 200) , random.randint(50 , 200), "green" )

#draw 100 random stars 
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()


def main():
    """
    Should ultimately draw a night sky filled with stars and planets.
    """
    turtle.bgcolor("black")
    tweak(True, 100)
    #length = int(input("Enter length of star to draw (e.g. 100): "))
    '''
    Semantic Error 
    had to concatrnate the input as a Int 
    After running the program it didnt work bc you cant multiply a string
    '''
    #draw_star(length)
    draw_celestial_bodies()
    
    tweak(True, 1)
    turtle.hideturtle()
    '''
    runtime error 
    had to be turtle.turtlehide()
    vs code told me when iu ran the program
    
    '''
    input("Press enter to continue...")

main()
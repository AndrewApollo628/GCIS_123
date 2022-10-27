'''
This program will test functions in pixart 

Author: Andrew Apollo 
'''
#import turtle
import pixart 
import math
import turtle

#in class test 
'''
def test_init():
    pixart.init()
    assert (turtle.speed() == 0)
    assert (turtle.xcor() == -300)
    assert (turtle.ycor() == 300)
    assert (turtle.isdown() == False)
    assert (turtle.pencolor() == "black")
    assert (turtle.fillcolor() == "white")
'''
'''
#HW 4.2 Turtle color tests 
def test_color_black(): #function tests to see if the color is black  
    black = pixart.draw_pixel_by_code('0')
    assert(black == "0")

def test_color_white(): #function tests to see if the color is white
    white = pixart.draw_pixel_by_code('1')
    assert(white == "1")

def test_color_red(): #function tests to see if the color is red
    red = pixart.draw_pixel_by_code('2')
    assert(red == "2")

def test_color_yellow(): #function tests to see if the color is yellow
    yellow = pixart.draw_pixel_by_code('3')
    assert(yellow == "3")

def test_color_orange(): #function tests to see if the color is orange
    orange = pixart.draw_pixel_by_code('4')
    assert(orange == "4")

def test_color_green(): #function tests to see if the color is green 
    green = pixart.draw_pixel_by_code('5')
    assert(green == "5")

def test_color_yellowgreen(): #function tests to see if the color is yellowgreen 
    yellowgreen = pixart.draw_pixel_by_code('6')
    assert(yellowgreen == "6")

def test_color_sienna(): #function tests to see if the color is sienna  
    sienna = pixart.draw_pixel_by_code('7')
    assert(sienna == "7")

def test_color_tan(): #function tests to see if the color is tan  
    tan = pixart.draw_pixel_by_code('8')
    assert(tan == "8")

def test_color_grey(): #function tests to see if the color is grey  
    tan = pixart.draw_pixel_by_code('9')
    assert(tan == "9")

def test_color_darkgrey(): #function tests to see if the color is darkgrey  
    darkgrey = pixart.draw_pixel_by_code('A')
    assert(darkgrey == "A")
'''
#4.3.2 Class Activity 
def assertle(x,y,color,fillcolor):
     assert math.isclose(x, turtle.xcor())
     assert math.isclose(y , turtle.ycor())

def test_move():
    pixart.init()
    pixart.move(5,4)
    assertle(-180 , 150, "black" , "white")
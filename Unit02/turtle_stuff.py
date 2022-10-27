#Andrew Apollo 2.3.5 class activity 

import turtle

angle = 45

def test_drive():
    turtle.forward(100)
    turtle.left(87)
    turtle.setheading(127)
    turtle.up()
    turtle.goto(50,50)
    turtle.down()
    turtle.home()
    turtle.circle(25)

def turtle_state():
    print(turtle.isdown())
    print(str(turtle.heading()) + " degreea")
    print(str(turtle.xcor()) + "," + str(turtle.ycor()))

def square(side , angle, pencolor, fillcolor):
    turtle.pensize(4)
    turtle.color(pencolor)
    turtle.fillcolor(fillcolor)
    turtle.begin_fill()
    turtle.left(angle)
    turtle.forward(side)
    turtle.right(90)
    turtle.forward(side)
    turtle.right(90)
    turtle.forward(side)
    turtle.right(90)
    turtle.forward(side)
    turtle.right(90)
    turtle.right(angle)
    turtle.end_fill()

def main():
    
    turtle_state()
    #test_drive()
    turtle.bgcolor("pink")
    square(50 , 22.5 , "red" , "blue")
    square(100 , 45 , "orange" , "black")
    square(200 , 60.5 , "white" , "red")
    turtle_state()
    input("Press Enter to continue: ")

main()
'''
Author: Andrew Apollo 

This program import the turtle function and uses paramaters to draw shapes. 
Then uses these shapes to draw a picture 

'''
import turtle

def rectangle( x , y , height , width , pencolor , fill): #set paramaters for rectangle
    
    turtle.up()
    turtle.goto( x, y ) 
    turtle.down()
    turtle.pensize(5)
    turtle.color(pencolor)
    turtle.fillcolor(fill)
    turtle.begin_fill()
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.end_fill()

def triangle( x , y ,base , pencolor , fill): #set paramaters for triangle 
    
    turtle.up()
    turtle.goto( x, y ) 
    turtle.down()
    turtle.pensize(5)
    turtle.color(pencolor)
    turtle.fillcolor(fill)
    turtle.begin_fill()
    turtle.forward(base)
    turtle.left(135)
    turtle.forward(base)
    turtle.left(90)
    turtle.forward(base)
    turtle.left(135)
    turtle.forward(base)
    turtle.end_fill()

def circle(x , y , radius , pencolor , fill): #set paramaters for circle 
    
    turtle.up()
    turtle.goto( x, y ) 
    turtle.down()
    turtle.pensize(5)
    turtle.color(pencolor)
    turtle.fillcolor(fill)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def main():
    #screen needs to be fullscreen to view 
   
    # Skyline 
    rectangle( -850 , -200 , 1200 , 1750 , "skyblue" , "skyblue")
    
    #sun 
    circle(-550 , 250 , 200 , "orange" , "yellow")    
    
    #cloud1 
    circle(0 , 200 , 50 , "white" , "white")
    circle(50 , 225 , 50 , "white" , "white")
    circle(100 , 200 , 50 , "white" , "white")
    
    #cloud2 
    circle(-250 , 250 , 50 , "white" , "white")
    circle(-200 , 275 , 50 , "white" , "white")
    circle(-150 , 250 , 50 , "white" , "white")
    circle(-200 , 225 , 50 , "white" , "white")
    
    #cloud3
    circle(-750 , 250 , 50 , "white" , "white")
    circle(-700 , 275 , 50 , "white" , "white")
    circle(-650 , 250 , 50 , "white" , "white")
    circle(-700 , 225 , 50 , "white" , "white")
    
    #feild 
    rectangle( -850 , -500 , 300 , 1750 , "green" , "green")
    
    #house
    rectangle(-200 , -300 , 250 , 250 , "black" , "darkgoldenrod") #frame
    rectangle(-150 , -300 , 150 , 100 , "black" , "red") #door
    circle(-125 , -250 , 5 , "black" , "black") 
    triangle(-150 , -50 , 250 , "black" , "grey") #roof
    
    #tree 
    rectangle(175 , -300 , 300 , 25 , "peru" , "peru") #trunck 
    circle(187 , 0 , 150 , "green" , "green") #leaves 
    
    #fence 
    rectangle(-300 , -300 , 50 , 25 , "goldenrod" , "goldenrod" )#post
    triangle(-295 , -250 , 25 ,"goldenrod" , "goldenrod" )#top of post 
    rectangle(-400 , -300 , 50 , 25 , "goldenrod" , "goldenrod" )#post
    triangle(-395 , -250 , 25 ,"goldenrod" , "goldenrod" )#top of post 
    rectangle(-500 , -300 , 50 , 25 , "goldenrod" , "goldenrod" )#post
    triangle(-495 , -250 , 25 ,"goldenrod" , "goldenrod" )#top of post 
    rectangle(-600 , -300 , 50 , 25 , "goldenrod" , "goldenrod" )#post
    triangle(-595 , -250 , 25 ,"goldenrod" , "goldenrod" )#top of post 
    rectangle(-700 , -300 , 50 , 25 , "goldenrod" , "goldenrod" )#post
    triangle(-695 , -250 , 25 ,"goldenrod" , "goldenrod" )#top of post 
    rectangle(-800 , -300 , 50 , 25 , "goldenrod" , "goldenrod" )#post
    triangle(-795 , -250 , 25 ,"goldenrod" , "goldenrod" )#top of post 
    rectangle(-800 , -300 , 50 , 25 , "goldenrod" , "goldenrod" )#post
    triangle(-895 , -250 , 25 ,"goldenrod" , "goldenrod" )#top of post 
    rectangle(-900 , -265, 5 , 700 , "goldenrod" , "goldenrod") #cross section
    rectangle(-900 , -290, 5 , 700 , "goldenrod" , "goldenrod") #cross section 2

    #stops program 
    input("Press enter to exit: ")
    
main()


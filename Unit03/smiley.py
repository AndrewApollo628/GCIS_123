#class activty 3.1.2 Andrew Apolo 

import turtle

def draw_circle( x , y , radius , fill):
   turtle.up()
   turtle.goto(x , y)
   turtle.down
   turtle.pencolor("black")
   turtle.fillcolor(fill)
   turtle.begin_fill()
   turtle.circle(radius)
   turtle.end_fill()

def draw_centered_circle( x , y , radius , fill):
   #raise pen
   turtle.up()
   #rotate pen by 90 degrees left
   turtle.right(90)
   #move the turtle by the radius 
   turtle.goto( x , y)
   turtle.forward(radius)
   #rotate the turtle 90 right
   turtle.left(90) 
   #put the pen down
   turtle.down()
   #set pencolor
   turtle.pencolor("black")
   #set fill color
   turtle.fillcolor(fill)
   #begin fill
   turtle.begin_fill()
   #draw circle
   turtle.circle(radius)
   #end fill
   turtle.end_fill()

def draw_smiley( x , y , headradius , headcolor , nosecolor, eyecolor, mouthcolor):
    draw_centered_circle(x , y , headradius , headcolor)
    draw_centered_circle(0 , 0 , headradius * .10 , nosecolor)
    draw_eye( x - headradius * 0.35 , y + headradius * 0.35 , headradius *0.2 , eyecolor)
    draw_eye( x + headradius * 0.35 , y + headradius * 0.35 , headradius *0.2 , eyecolor)
    draw_mouth( x , y - headradius *.30 , headradius * .60 , mouthcolor)

def tweak(speed , traceronoff):
    turtle.speed(speed)
    turtle.tracer(traceronoff)

def draw_eye( x , y , eyeradius , iriscolor):
    draw_centered_circle( x , y , eyeradius , "white")
    draw_centered_circle( x , y , eyeradius * 0.5 , iriscolor)
    draw_centered_circle( x , y , eyeradius * 0.25 , "black")
    turtle.hideturtle()

def draw_mouth( x , y , radius , fill):
    mouthradius = radius* 0.60
    turtle.up()
    turtle.goto( x , y - radius * 0.85)
    turtle.color(fill)
    turtle.fillcolor(fill)
    turtle.begin_fill()
    turtle.down()
    turtle.circle(radius , 90)
    turtle.left(90)
    turtle.forward(radius * 2 )
    turtle.left(90)
    turtle.circle(radius , 90)
    turtle.end_fill()
    turtle.up()

def main():
  
   draw_smiley(0 , 0 , 100 ,"yellow" , "pink" , "blue" , "black")
   draw_smiley(200 , -200 , 50 ,"yellow" , "pink" , "green" , "black")
   draw_smiley(-150 , 200 , 100 ,"yellow" , "pink" , "red" , "black")
   draw_smiley(300 , 150 , 100 ,"yellow" , "pink" , "pink" , "black")
   #draw_mouth(0 , 0 ,100 , "green")
   tweak(20 , True)
   input("Press enter to exit: ")

main()

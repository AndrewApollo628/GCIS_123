#Author: Andrew Apollo 

import turtle
import review01

#Class activity 13.1.8/9
def test_distance():
    x1, y1 = 0, 3
    x2, y2 = 4, 0
    expected = 5

    actual = review01.distance(x1,x2,y1,y2)

    assert expected == actual

#Class activity 13.1.10
def test_triangle():
    x1, y1 = 0, 0
    x2, y2 = 0, 300
    x3, y3 = 400, 0
    color = "red"
    expected = 1200

    actual = review01.triangle(x1, y1, x2, y2, x3, y3, color)

    assert x1 == turtle.xcor()
    assert y1 == turtle.ycor()
    assert not turtle.isdown()
    assert 5 == turtle.speed()
    assert color == turtle.fillcolor()
    assert expected == actual
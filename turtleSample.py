from turtle import *

#stars, octagons
# function for each shape

def rectangle_right(size1 , size2, fcolor, pcolor):
    begin_fill()
    fillcolor(fcolor)
    pencolor(pcolor)
    forward(size1)
    right(90)
    forward(size2)
    right(90)
    forward(size1*2)
    right(90)
    forward(size2)
    right(90)
    forward(size1*2)
    end_fill()
rectangle_right(400, 50, "green", "green")

def rectangle_left(size1 , size2, fcolor, pcolor):
    begin_fill()
    fillcolor(fcolor)
    pencolor(pcolor)
    left(90)
    forward(size2)
    left(90)
    forward(size1)
    left(90)
    forward(size2)
    left(90)
    forward(size1)
    end_fill()
rectangle_left(800, 300, "blue", "blue")

def square(size, fcolor, pcolor):
    begin_fill()
    fillcolor(fcolor)
    pencolor(pcolor)
    left(90)
    forward(size)
    left(90)
    forward(size)
    left(90)
    forward(size)
    left(90)
    forward(size)
    left(90)
    forward(size)
    end_fill()
# square(800, "blue", "blue")
square(150, "brown", "brown")

def triangle(size, size2, fcolor, pcolor):
    begin_fill()
    fillcolor(fcolor)
    pencolor(pcolor)
    left(45)
    forward(size)
    left(90)
    forward(size)
    left(135)
    forward(size2)
    end_fill()
triangle(106, 150, "yellow", "yellow")    

def tornado(width, length, fcolor, pcolor):
    

input()
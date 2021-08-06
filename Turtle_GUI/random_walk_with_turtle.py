import turtle
from turtle import Turtle,Screen
import random

turtle.colormode(255)

t = Turtle()
t.shape("turtle")
t.pensize(15)
t.pendown()
t.speed('fastest')
angles = [90, 270]

def rand_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


while 1<2:

    coin = random.randint(0, 1)
    rand_color()
    t.color(rand_color())
    if coin == 0:
        t.right(random.choice(angles))
        t.forward(50)
    else:
        t.left(random.choice(angles))
        t.forward(50)


scrn = Screen()
scrn.exitonclick()


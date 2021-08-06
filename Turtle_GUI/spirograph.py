import turtle as t
import random
t.colormode(255)
t.bgcolor('black')
t.speed('fastest')
t.pendown()
t.hideturtle()
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)


while 1<2:
    t.color(random_color())
    t.circle(100)
    t.left(10)










t.exitonclick()




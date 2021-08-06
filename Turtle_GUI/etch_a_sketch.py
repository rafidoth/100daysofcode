import turtle as tt
tt.listen()
tt.shape("turtle")

def move_forward():
    tt.forward(20)

def move_backward():
    tt.backward(20)

def turn_left():
    tt.left(25)

def turn_right():
    tt.right(25)



tt.onkey(fun=move_forward, key="Up")
tt.onkey(fun=move_backward, key="Down")
tt.onkey(fun=turn_left, key="Left")
tt.onkey(fun=turn_right, key="Right")













tt.exitonclick()
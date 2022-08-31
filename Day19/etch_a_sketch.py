from turtle import Turtle, Screen

painter = Turtle()
screen = Screen()


def move_forward():
    painter.forward(10)

def move_backward():
    painter.backward(10)

def turn_left():
    painter.left(10)

def turn_right():
    painter.right(10)
    

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=screen.resetscreenw)



screen.exitonclick()
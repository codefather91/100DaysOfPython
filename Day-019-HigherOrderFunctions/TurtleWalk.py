from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

screen.listen()

def move_forwards():
    tim.forward(10)
    return

def move_backwards():
    tim.backward(10)
    return

def turn_left():
    tim.left(90)
    return

def turn_right():
    tim.right(90)
    return

def clear_screen():
    tim.home()
    tim.clear()

screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear_screen, "c")
screen.exitonclick()

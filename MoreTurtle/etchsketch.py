from turtle import Turtle, Screen

tim = Turtle()


def move_for():
    tim.forward(30)


def move_back():
    tim.back(30)


def turn_clock():
    tim.right(15)


def turn_count():
    tim.left(15)

def t_clear():
    tim.reset()

screen = Screen()
screen.listen()
screen.onkey(move_for, "w")
screen.onkey(move_back, "s")
screen.onkey(turn_clock, "d")
screen.onkey(turn_count, "a")
screen.onkey(t_clear, "c")
screen.exitonclick()

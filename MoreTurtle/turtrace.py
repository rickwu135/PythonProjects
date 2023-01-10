import turtle
from turtle import Turtle, Screen
import random

is_race = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make you bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-120, -90, -60, -30, 0, 30]
all_turtles = []

for i in range(0,6):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-230, y= y_positions[i])
    all_turtles.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} is the winner")
            else:
                print(f"You've lost! The {winning_color} is the winner")
        distance = random.randint(0, 10)
        turtle.forward(distance)

screen.exitonclick()

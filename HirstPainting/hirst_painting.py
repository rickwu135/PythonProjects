import turtle
import random
import colorgram

color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123),
              (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
              (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
              (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64),
              (107, 127, 153), (176, 192, 208), (168, 99, 102)]

t = turtle.Turtle()
turtle.colormode(255)
t.speed(0)

for i in range(10):
    t.penup()
    t.goto(-200, (i*50) - 250)
    t.pendown()
    for i in range(10):
        t.color(random.choice(color_list))
        t.dot(20)
        t.penup()
        t.forward(50)
        t.pendown()

t.hideturtle()

screen = turtle.Screen()
screen.exitonclick()
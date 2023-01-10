from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

x = 1

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()

score = Score()

screen.listen()
screen.onkey(r_paddle.f, "Up")
screen.onkey(r_paddle.b, "Down")

screen.onkey(l_paddle.f, "w")
screen.onkey(l_paddle.b, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()

    # detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect L paddle miss
    if ball.xcor() < -360:
        ball.reset_pos()
        score.r_point()

    # detect R paddle miss
    if ball.xcor() > 360:
        ball.reset_pos()
        score.l_point()




screen.exitonclick()

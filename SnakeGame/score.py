from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.score = 0
        self.write(f"Score: {self.score}", align="center", font=('Courier', 16, 'normal'))

    def increase(self):
        self.score += 1
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align="center", font=('Courier', 16, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align="center", font=('Courier', 16, 'normal'))
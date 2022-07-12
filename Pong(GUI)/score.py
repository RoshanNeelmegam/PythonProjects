from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self, x, y):
        self.score = 0
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(x, y)
        self.write(f"{self.score}", align="center", font=("Arial", 25, "normal"))


    def score_plus(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", align="center", font=("Arial", 25, "normal"))

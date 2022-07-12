from turtle import Turtle
import random

# Ball class made by inheriting the Turtle class
class Ball(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.speed(0)
        self.color("red")
        self.shape("circle")
        self.goto(x, y)
        self.speed("slowest")
        self.xdir = 1
        self.ydir = 1

    def move(self, xcor = 10, ycor = 5):
        self.goto(self.xcor() + (4 * self.xdir), self.ycor() + (2 * self.ydir))

    def bounce(self, paddle):
        if self.distance(paddle) < 30 and self.xcor() > 340 or self.distance(paddle) < 30 and self.xcor() < -340 :
            self.xdir *= (-1)

    def wallBounce(self):
        if self.ycor() > 285 or self.ycor() < -285:
            self.ydir *= (-1)

from turtle import Turtle

# Paddle class made by inheriting the Turtle class
class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(5, 1)
        self.goto(x, y)
        self.speed(0)
        self.x = self.xcor()

    def Up(self):
        if self.ycor() < 240:
         self.goto(self.x, self.ycor() + 35)

    def Down(self):
        if self.ycor() > -240:
            self.goto(self.xcor(), self.ycor() - 35)

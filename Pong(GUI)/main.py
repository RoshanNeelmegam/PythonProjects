# importing stuffs
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time

# initializing the screen for the game
screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
# turning off screen animation and using update method to turn on animation when required for smoother frames.
screen.tracer(0)

# initializing paddles
paddle1 = Paddle(360.0, 0.0)
paddle2 = Paddle(-370.0, 0.0)

# initializing ball
ball = Ball(0.0, 0.0)

# initializing scoreboard
score1 = Scoreboard(-20, 270)
score2 = Scoreboard(20, 270)
screen.update()

# listening for keypresses
screen.listen()
screen.onkeypress(paddle1.Up, "Up")
screen.onkeypress(paddle2.Up, "w")
screen.onkeypress(paddle1.Down, "Down")
screen.onkeypress(paddle2.Down, "s")

is_game_on = True
while is_game_on:
    screen.update()
    ball.move()
    ball.bounce(paddle1)
    ball.bounce(paddle2)
    ball.wallBounce()
    if ball.xcor() > 385:
        ball.goto(0,0)
        score1.score_plus()
    if ball.xcor() < -390:
        ball.goto(0,0)
        score2.score_plus()



screen.exitonclick()

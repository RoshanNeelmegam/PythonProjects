from turtle import Screen, Turtle
from snakebody import Snake
from scoreboard import Scoreboard
from food import Food
import time

# creatig and setting up the screen for the game.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
# With tracer set to 0, the animation on the screen is stopped which means no turtles will be shown or animated.
# This is essential in our cade as we have multiple turtle blocks and while moving, animation might appear choppy
# To deal with this, we could turn on animation only when all the blocks have moved.
screen.tracer(0)

# creating snake, food and scoreboard object
snake = Snake()
food = Food()
score = Scoreboard()
# This resumes and paused animation of the moment. So everytime we need to see the updated animation, we could use this update() method.
# Since we called the snake object in the previous line, turtle blocks would be placed on the screen. Since tracer is off, it wont be shown.
# But as soon as we update the screen, we would be able to see the turtle blocks on the screen.
screen.update()

#listening for keystrokes and responding to it.
screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")
is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.099)
    snake.move()
    score.collisionWithFood(snake, food)
    if score.collisionWithWall(snake) == 1:
        is_game_on = False

    #detecting collisions with itself
    for segments in snake.snake_body:
        if snake.snake_body.index(segments) == 0:
            pass
        elif snake.snake_body[0].distance(segments) < 10:
            is_game_on = False
            score.end_score()



screen.exitonclick()

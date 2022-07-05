from turtle import Turtle

class Scoreboard(Turtle):
      def __init__(self):
            super().__init__()
            self.score = 0
            self.color("white")
            self.hideturtle()
            self.penup()
            self.goto(0, 270)
            self.write(f"Score: {self.score}", align="center", font=("Arial", 20, "normal"))
 
      def score_update(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 20, "normal"))
      
      def collisionWithFood(self, snake, food):
           # The .distance method returns the distance between the other turtle
           if snake.snake_body[0].distance(food) <= 25:
             food.update()
             snake.extend()
             self.score_update()

      def collisionWithWall(self, snake):
          if snake.snake_body[0].xcor() > 295 or snake.snake_body[0].xcor() < -295 or snake.snake_body[0].ycor() > 295 or snake.snake_body[0].ycor() < -295:
            self.end_score()
            return 1
          else:
            return 0

      def end_score(self):
        self.clear()
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 25, "normal"))
        self.goto(0, -30)
        self.write(f"Score is {self.score}", align="center", font=("Arial", 18, "normal"))


 

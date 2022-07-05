from turtle import Turtle

# creating a snake class
class Snake:
    
    # creating a list to store body's of snake.
    snake_body = []

    # on initializing the object, we need to create a sanke body. 
    def __init__(self):
        # defining co-ordinates which will be used by turtle to position the body.
        x = 0.0
        y = 0.0
        
        for turtles in range(3):
            t1 = Turtle()
            t1.shape("square")
            t1.color("white")
            t1.shapesize(1.0, 1.0, 0)
            t1.penup()
            t1.setpos(x, y)
            t1.speed("fastest")
            # since size of one turtle is 20 by default, shifting the blocks by 20.
            x -= 20
            self.snake_body.append(t1)
    
    # snake's function to move and extend it's body.
    def move(self):
        for i in range(len(self.snake_body), 0, -1):
            if i == 1:
                # skipping the below lines as head of the snake is anyways moved at the end.
                # # The next line is important in the sense that it helps in keeping the bodies of the snake separate by moving the head.
                # self.snake_body[0].forward(18)
                pass
            else:
                self.snake_body[i-1].setheading(self.snake_body[i-2].heading())
                self.snake_body[i-1].setpos(self.snake_body[i-2].xcor(), self.snake_body[i-2].ycor())
        # This line is important as the head has to move before the other parts can be moved
        self.snake_body[0].forward(18)
        
    def up(self):
        if self.snake_body[0].heading() == 90:
            pass
        elif self.snake_body[0].heading() == 0:
            self.snake_body[0].left(90)
        elif self.snake_body[0].heading() == 180:
            self.snake_body[0].right(90)
        else:
            pass

    def down(self):
        if self.snake_body[0].heading() == 0:
            self.snake_body[0].right(90)
        elif self.snake_body[0].heading() == 90:
            pass
        elif self.snake_body[0].heading() == 180:
            self.snake_body[0].left(90)
        else:
            pass

    def left(self):
        if self.snake_body[0].heading() == 0:
            pass
        elif self.snake_body[0].heading() == 90:
            self.snake_body[0].left(90)
        elif self.snake_body[0].heading() == 180:
            pass
        else:
            self.snake_body[0].right(90)

    def right(self):
        if self.snake_body[0].heading() == 0:
            pass
        elif self.snake_body[0].heading() == 90:
            self.snake_body[0].right(90)
        elif self.snake_body[0].heading() == 180:
            pass
        else:
            self.snake_body[0].left(90)
        
    def extend(self):
        t1 = Turtle()
        t1.shape("square")
        t1.color("white")
        t1.shapesize(1.0, 1.0, 0)
        t1.penup()
        t1.goto(self.snake_body[-1].position())
        t1.speed("fastest")
        self.snake_body.append(t1)


      
   

    
        

    


    


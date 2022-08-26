from turtle import Turtle, Screen

class Snake():
    turtles = []
    snake_size = 20
    def __init__(self):
        self.create_initial_snake()
        pass
    
    def create_initial_snake(self):
        for _ in range (0,3):
            snake_body = Turtle()
            snake_body.color("white")
            snake_body.shape("square")
            if _ > 0:
                print(self.turtles[-1].pos())
                snake_width = 20
                print(snake_width)
                snake_body.setpos(x=int(self.turtles[-1].pos()[0]-self.snake_size),y=0.0)
            self.turtles.append(snake_body)


    def attach_body(self):
        snake_body = Turtle()
        snake_body.color("white")
        snake_body.shape("square")
        snake_body.setpos(x=int(self.turtles[-1].pos()[0]-self.snake_size),y=0.0)
        self.turtles.append(snake_body)

    def move_one(self):
        for snake_bodypart in self.turtles:
            snake_bodypart.forward(100)

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
snake = Snake()

snake.attach_body()
snake.move_one()
screen.exitonclick()


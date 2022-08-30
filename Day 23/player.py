from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.create_player()

    def create_player(self):
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.goto(0,-270)
        self.setheading(90)

    def check_if_level_finished(self):
        return self.ycor() >290
    
    def move(self):
        self.forward(10)
    
    def reset_level(self):
        self.goto(0,-270)
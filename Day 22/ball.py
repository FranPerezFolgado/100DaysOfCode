from tabnanny import check
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.y_move = 10
        self.x_move = 10
        self.move_speed =0.1

    
    def create_ball(self):
        self.color("white")
        self.shape("circle")
        self.penup()
    
   
            
    def move(self):
        if self.ycor() == 290 or  self.ycor() == -290:
            self.bounce()
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move

        self.goto(x=new_x,y=new_y)

    def bounce(self):
        self.y_move *= -1

    def check_collision(self, coords: tuple):
        print(self.distance(coords))
        if (self.xcor() >= 340 or self.xcor() <= -340) and self.distance(coords) <= 50:
            self.x_move *= -1
            self.move_speed *= 0.9


    def check_out_of_bounds(self):
        return self.xcor() > 370 or self.xcor() < -370
    
    def reset_position(self):
        self.goto(0,0)
        self.move_speed(0.1)
        self.x_move *= -1
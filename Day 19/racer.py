from turtle import Turtle
starting_position_y=-200 +(400/10)
class Racer():
    def go_to_initial_pos(self, y):
       # print(self.num_racer)
#
       # y = starting_position_y +((self.num_racer*30))
       # print(y)
      #  y = -(50 + ((self.num_racer*10) +100 ))

        self.turtle.goto(x=-230, y=y)
    
    def __init__(self, num_racer,colors, y):
        self.num_racer = num_racer
        self.color = colors[num_racer]
        self.turtle = Turtle(shape="turtle")
        self.turtle.penup()
        self.turtle.color(self.color)
        self.go_to_initial_pos(y)
    
    def move_forward(self,distance):
        self.turtle.forward(distance=distance)

    def win(self, max_x):
        print(self.turtle.pos())
        return self.turtle.pos()[0] >= max_x

 

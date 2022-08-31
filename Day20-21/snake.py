from turtle import Turtle

MOVE_DISTANCE = 20
headings ={
    "east":0,
    "north":90,
    "west":180,
    "south":270
}

class Snake():
    

    def __init__(self):
        self.segments = []
        self.snake_size=20
        self.create_initial_snake()
        self.head = self.segments[0]

    
    def create_initial_snake(self):
        for i in range (0,3):
            snake_body = Turtle()
            snake_body.color("white")
            snake_body.shape("square")
            snake_body.penup()
            if i > 0:
                snake_body.setpos(x=int(self.segments[-1].pos()[0]-self.snake_size),y=0.0)    
            self.segments.append(snake_body)
    
    def reset(self):
        for segment in self.segments:
            segment.goto(10000,10000)
        self.segments.clear()
        self.create_initial_snake()
        self.head = self.segments[0]



    def attach_body(self):
        snake_body = Turtle()
        snake_body.color("white")
        snake_body.shape("square")
        snake_body.penup()
        snake_body.goto(self.segments[-1].pos())
        self.segments.append(snake_body)

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading() != headings["south"]:
            self.segments[0].setheading(headings["north"])
    def down(self):
        if self.head.heading() != headings["north"]:
            self.segments[0].setheading(headings["south"])
    def right(self):
        if self.head.heading() != headings["west"]:
            self.segments[0].setheading(headings["east"])
    def left(self):
        if self.head.heading() != headings["east"]:
            self.segments[0].setheading(headings["west"])

    def detect_collision_with_wall(self):
        return self.head.xcor() > 280 or self.head.xcor() < -280 or  self.head.ycor() > 280 or  self.head.ycor() < -280
        




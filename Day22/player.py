from turtle import Turtle

POSITIONS = {
    "LEFT":(-350, 0),
    "RIGHT":(350, 0)
}
class Player(Turtle):

    def __init__(self, position):
        super().__init__()
        self.create_player()
        self.goto(POSITIONS[position])
        

    def create_player(self):
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        if not self.check_if_limit_screen("UP"):
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)
    
    def down(self):
        if not self.check_if_limit_screen("DOWN"):
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)


    def check_if_limit_screen(self, mode:str) -> bool:
        y = self.ycor() 
        if mode == "UP":
            y += 50
            if y >= 280:
                return True
        elif mode == "DOWN":
            y -= 50
            if y <= -270:
                return True
        

            return False

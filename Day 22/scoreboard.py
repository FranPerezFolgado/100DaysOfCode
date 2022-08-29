from turtle import Turtle
ALIGNMENT = "center"
FONT=("Arial", 16, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = {"right":0,"left":0}
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=0,y=270)
        
        self.update_scoreboard()
    

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.score["left"], align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.score["right"], align="center", font=("Courier", 80, "normal"))

    def add_score(self, side):
        self.score[side] += 1
        self.update_scoreboard()

    
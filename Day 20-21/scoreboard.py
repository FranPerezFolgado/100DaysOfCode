from http.client import FORBIDDEN
from turtle import Turtle
ALIGNMENT = "center"
FONT=("Arial", 16, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=0,y=270)
        
        self.write(f"Score: {self.score}",align=ALIGNMENT, move=False, font=FONT)
    

    def add_score(self):
        self.score +=1
        self.undo()
        self.write(f"Score: {self.score}",align=ALIGNMENT, move=False,  font=FONT)

    def game_over(self):
        self.goto(x=0,y=0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
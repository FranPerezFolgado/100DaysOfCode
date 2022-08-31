
from turtle import Turtle
ALIGNMENT = "center"
FONT=("Arial", 16, "normal")
SCORE_FILE = "Day20-21/score.txt"
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=0,y=270)
        self.highscore = 0
        with open(SCORE_FILE) as score_file:
            self.highscore = int(score_file.read())
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}. High score: {self.highscore}",align=ALIGNMENT, move=False, font=FONT)
    
    def add_score(self):
        self.score +=1
        self.update_scoreboard()

    def game_over(self):
        self.goto(x=0,y=0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        
        
        if self.score > self.highscore:
            self.highscore = self.score
            with open(SCORE_FILE, mode="w") as score_file:
                score_file.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()
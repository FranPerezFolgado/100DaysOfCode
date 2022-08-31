from turtle import Turtle
FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(x=-220,y=250)
        self.update_scoreboard()
    

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level {self.level}", align="center", font=FONT)
        

    def add_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)

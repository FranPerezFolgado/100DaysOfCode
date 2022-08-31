import lib
from player import Player
from ball import Ball
from scoreboard import Scoreboard
import time

screen = lib.setup_screen()
player1 = Player("LEFT")
player2 = Player("RIGHT")
ball = Ball()
scoreboard = Scoreboard()
screen.onkeypress(player1.up, "Up")
screen.onkeypress(player1.down, "Down")
screen.onkeypress(player2.up, "w")
screen.onkeypress(player2.down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    #Detect collision with players
    ball.check_collision(player1.position())
    ball.check_collision(player2.position())

    #Detect players miss
    if ball.check_out_of_bounds():
        if ball.xcor() > 0:
            scoreboard.add_score("left")
        else:
            scoreboard.add_score("right")
        ball.reset_position()

    
screen.exitonclick()
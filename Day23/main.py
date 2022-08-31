import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle crossing")
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_random_cars()
    car_manager.move_cars()

    #check if player on top
    if player.check_if_level_finished():
        #restart game
        scoreboard.add_level()
        car_manager.add_level()
 
        player.reset_level()


    
    #check if player collision with cars
   
    if car_manager.check_cars_collision(player):
        scoreboard.game_over()
        game_is_on = False
        #game over

screen.exitonclick()
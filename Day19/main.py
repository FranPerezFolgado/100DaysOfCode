from tkinter import N
from turtle import Turtle, Screen, colormode, position
from racer import Racer
from calculate_position import PositionCalculator
import random


def random_color():
    
    R = random.randrange(0, 257, 10)
    B = random.randrange(0, 257, 10)
    G = random.randrange(0, 257, 10)
    return (R, G, B)

def create_board(num_racers):
    colors = []
    calculator = PositionCalculator(height=height, margin=30, num_racers=num_racers)
    positions = calculator.calculate_position()

    for _ in range(0, num_racers):
        colors.append(random_color())


    racers = []
    for _ in range(0, num_racers):
        racer = Racer(_, colors,positions[_])
        racers.append(racer)

    return racers

is_race_on = False
height = 500
width =500
screen = Screen()
screen.setup(width=width, height=height)
colormode(255)
num_racers = int(screen.textinput(title="How many racers",
                                  prompt="How many racers will be in this race?"))
user_bet = int(screen.textinput(
    title="Make your bet", prompt=f"Which turtle will win the race? Enter a number from(1 to {num_racers})")) - 1
racers = create_board(num_racers=num_racers)
winner = 0
if user_bet:
    is_race_on = True
while is_race_on:
    for racer in racers:
        rand_distance = random.randint(0,10)
        racer.move_forward(rand_distance)
        if racer.win((width/2) - (40/2)):
            winner = racer.num_racer
            is_race_on = False

if user_bet == winner:
    print("You win!")
else:
    print("You lost :(")
print(f"The winner was {winner}")




screen.exitonclick()

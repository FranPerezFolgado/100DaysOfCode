from turtle import color
from colorgram import extract, Color
from turtle import Turtle, Screen, colormode, forward
import random

def extract_colors_in_tuple(num_colors):
    def check_if_color_white(color: tuple):
        return color[0] > 200 and color[1] > 200 and color[2] > 200
    
    colors_extracted = extract("Day 18\hirst.jpg", num_colors)
    colors= []
    for color  in colors_extracted:
        if not check_if_color_white(color.rgb):
            colors.append((color.rgb[0],color.rgb[1],color.rgb[2]))
    return colors


def create_painter():
    painter = Turtle()
    painter.speed(0)
    painter.pensize(20)
    colormode(255)
    painter.penup()
    painter.ht()
    return painter
def initial_position(painter: Turtle, num_of_dots:int):
    painter.setheading(225)
    painter.forward((num_of_dots/2)*50)
    painter.setheading(0)
def move_to_next_y(painter: Turtle, num_of_dots: int):
    painter.setheading(90)
    painter.forward(50)
    painter.setheading(180)
    painter.forward(num_of_dots*50)
    painter.setheading(0)

colors = extract_colors_in_tuple(40)
num_of_dots = 10
painter =create_painter()
initial_position(painter,num_of_dots)



for y  in range(0,num_of_dots):
    for x in range(0,num_of_dots):
        painter.dot(20, random.choice(colors))
        painter.forward(50)
    move_to_next_y(painter, num_of_dots)




screen = Screen()

screen.exitonclick()
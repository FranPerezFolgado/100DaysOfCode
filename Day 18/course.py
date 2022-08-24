from turtle import Turtle, Screen, colormode, forward
import random

tim = Turtle()
tim.shape("circle")
tim.color("forest green")
tim.pensize(1)
tim.speed(0)
tim.shapesize(0.1)

colours= ["LightSkyBlue","LightSteelBlue", "PaleTurquoise3", "LightSeaGreen","PaleGreen4", "gray70"]
angles = [0, 90, 180, 270]
#for _ in range(0,4):
#    tim.forward(100)
#    tim.right(90)

#for ic in range(0,15):
#    print(ic)
#    if ic % 2 == 0:
#        tim.up()
#    else:
#        tim.down()
#    tim.forward(10)

#print(colormode())
#colormode(255)

def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(0, num_sides):
        tim.forward(100)
        tim.right(angle)
def random_color():
    colormode(255)
    R = random.randrange(0, 257, 10)
    B = random.randrange(0, 257, 10)
    G = random.randrange(0, 257, 10)
    return (R, G, B)

for angle in range(0,360, 2):
    tim.color(random_color())
    tim.circle(200)
    tim.setheading(angle)
#for _ in range(0,200):
#while True:
#    tim.forward(40)
#    #tim.color(random.choice(colours))
#    tim.color(random_color())
#    tim.setheading(random.choice(angles))
    #tim.right(random.choice(angles))
#for _ in range(3,11):
#    random_color()
#    print(f"sides :{_}") 
#    draw_shape(_)



screen = Screen()
screen.exitonclick()


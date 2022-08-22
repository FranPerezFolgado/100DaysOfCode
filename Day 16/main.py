#from turtle import Turtle, Screen
#import prettytable
#
#fran = Turtle()
#nat = Turtle()
#
#fran.shape("turtle")
#fran.color("#6495ED")
#fran.forward(100)
#my_screen = Screen()
#
#print(my_screen.canvheight)
#my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu","Squirtle","Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

print(table)
from turtle import Turtle
import random
import time
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    
    def __init__(self):
        self.cars = []
        self.create_cars = True
        self.move_distance = STARTING_MOVE_DISTANCE
        
        
    def create_random_cars(self):
        if self.should_gen_car():
            num_cars = random.randint(1,2)
            print(num_cars)
            for _ in range(0,num_cars):
                self.cars.append(Car(random.choice(COLORS)))

    def should_gen_car(self) -> int:
        rand = random.randint(0,6)
        return rand == 1

    def move_cars(self):
        for car in self.cars:
            car.forward(self.move_distance)
        
    def check_cars_collision(self, player: Turtle) -> bool:
        for car in self.cars:
            print(car.distance(player))
            if car.distance(player) < 20:
               return True

        return False


    def add_level(self):
        self.move_distance += MOVE_INCREMENT



class Car(Turtle):
    def __init__(self,color:str):
        super().__init__()
        self.color(color)
        self.create_initial_car()
        

    def create_initial_car(self):
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setheading(180)
        rand_y= random.randint(-240,240)
        self.goto(300,rand_y)
from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
MAX_PIXELS_FROM_CENTER = 250
STARTING_X_POS = 300
COLLISION_POINT_DISTANCE = 20


class CarManager():
    
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 5)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-MAX_PIXELS_FROM_CENTER, MAX_PIXELS_FROM_CENTER)
            new_car.goto(STARTING_X_POS, random_y)
            self.all_cars.append(new_car)
            
    def move_cars(self):
        for car in self.all_cars:

            car.backward(self.car_speed)


    def check_distance(self, object):
        for car in self.all_cars:
            if car.distance(object) < 20:
                return True
            else:
                return False

    def level_up(self):
        self.car_speed += MOVE_INCREMENT





import time
from turtle import Turtle
import random


COLORS = ["red", "orange", "green", "blue", "grey", "yellow", "black", "purple"]


class Obstacles:
    def __init__(self):
        self.all_obstacles = []
        self.speed = 5

    def create_obstacle(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_obstacle = Turtle("square")
            new_obstacle.penup()
            new_obstacle.shapesize(stretch_wid=1, stretch_len=2)
            new_obstacle.color(random.choice(COLORS))
            new_obstacle.goto(x=350, y=random.randint(-300, 300))
            self.all_obstacles.append(new_obstacle)

    def move_obstacle(self):
        for obstacle in self.all_obstacles:
            obstacle.backward(self.speed)

    def collision_detection(self, turtle):
        for obstacle in self.all_obstacles:
            if turtle.distance(obstacle) < 24:
                return False
        return True

    def clear_obstacles(self):
        for obstacle in self.all_obstacles:
            obstacle.penup()
            obstacle.hideturtle()

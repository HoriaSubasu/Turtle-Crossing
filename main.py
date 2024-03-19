# Imports
import time
from turtle import Turtle
from turtle import Screen
from obstacles import Obstacles

# Variables

screen = Screen()
turtle = Turtle("turtle")
text = Turtle()
obstacles = Obstacles()
lvl = 1

# Functions


def fd():
    turtle.setheading(90)
    turtle.forward(15)
# moves the turtle object forward with 25


def bd():
    turtle.setheading(270)
    turtle.forward(15)
# moves the turtle object backward with 25


def reset():
    screen.resetscreen()
    text.penup()
    text.hideturtle()
    turtle.penup()
    turtle.setheading(90)
    obstacles.clear_obstacles()
    text.goto(x=-330, y=330)
    text.write(f"Level: {lvl}", True, align="left", font=('Arial', 10, 'bold'))
    turtle.goto(x=0, y=-332)
# resets the screen to the original position and changes the level entry.


def game_over():
    screen.resetscreen()
    text.penup()
    text.hideturtle()
    turtle.penup()
    turtle.hideturtle()
    text.goto(x=-40, y=0)
    text.write("Game Over.", True, align="left", font=('Arial', 10, 'bold'))

# Settings


screen.setup(700, 700)
screen.bgcolor("white")
screen.tracer(0)
turtle.penup()
text.penup()
text.hideturtle()
turtle.setheading(90)
turtle.goto(x=0, y=-332)
text.goto(x=-330, y=330)
text.write(f"Level: {lvl}", True, align="left", font=('Arial', 10, 'bold'))

screen.onkey(fd, "Up")
screen.onkey(bd, "Down")
screen.listen()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    obstacles.create_obstacle()
    obstacles.move_obstacle()
    game_is_on = obstacles.collision_detection(turtle=turtle)
    if turtle.ycor() > 329:
        lvl += 1
        obstacles.speed += obstacles.speed / 2 - 1
        reset()

game_over()

screen.exitonclick()

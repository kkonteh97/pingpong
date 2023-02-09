from turtle import Turtle
import random
import time

move_distance = 10

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.shapesize(0.5)
        self.setheading(45)
        self.penup()
        self.speed(10)
        self.goto((-250, 0))
        self.move()
        self.refresh()

    def refresh(self):
        self.hideturtle()
        self.goto((0,0))
        self.showturtle()
    def move(self):
        self.forward(move_distance)

    def bounce_h(self):
        num = random.randint(355, 365)
        heading = self.heading()
        self.setheading(num-heading)

    def bounce_v(self):
        num = random.randint(175, 185)
        heading = self.heading()
        self.setheading(num-heading)





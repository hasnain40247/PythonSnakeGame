import random
from turtle import Turtle
colors=["red","orange","purple","green","yellow"]

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(0.9,0.9)
        self.color(colors[random.randint(0,4)])
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.color(colors[random.randint(0, 4)])
        self.goto(random_x, random_y)

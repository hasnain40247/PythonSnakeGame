import random
from turtle import Turtle
UP=90
DOWN=270
RIGHT=0
LEFT=180
cols=['#C7980A', '#F4651F', '#82D8A7', '#CC3A05', '#575E76', '#156943', '#0BD055', '#ACD338']
class Snake:
    def __init__(self):
        self.positions = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []
        self.create_snake()
        self.speed=20
        self.head=self.segments[0]

    def create_snake(self):
        for position in self.positions:
            self.add_segment(position)


    def add_segment(self,position):
        newsegment = Turtle(shape="square")
        newsegment.color(cols[random.randint(0, 7)])
        newsegment.penup()
        newsegment.goto(position)
        self.segments.append(newsegment)

    def extend(self):
        self.add_segment(self.segments[-1].position())
    def move(self):
        for segment_num in range(len(self.segments) - 1, 0, -1):
            new_X = self.segments[segment_num - 1].xcor()
            new_Y = self.segments[segment_num - 1].ycor()
            self.segments[segment_num].goto(new_X, new_Y)
        self.speedUp()


    def speedUp(self):
        self.segments[0].forward(self.speed)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
             self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)



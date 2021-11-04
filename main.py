import random
import time
from turtle import  Turtle, Screen

from Food import Food
from Snake import Snake
from data import Scoreboard

screen=Screen()
screen.setup(600.600)
screen.bgcolor("black")
screen.title("Snake Game")

input="yes"
while input=="yes":
    screen.tracer(0)
    snake=Snake()
    food=Food()
    score=Scoreboard()
    screen.listen()
    screen.onkey(snake.up,"Up")
    screen.onkey(snake.right,"Right")
    screen.onkey(snake.down,"Down")
    screen.onkey(snake.left,"Left")
    is_Game_on=True
    while is_Game_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
        if snake.head.distance(food)<15:
            food.refresh()
            score.updateScore()
            snake.extend()

        if snake.head.xcor()>580 or snake.head.xcor()<-580 or snake.head.ycor()>340 or snake.head.ycor()<-340:
            is_Game_on=False
        for segment in snake.segments:
            if segment!= snake.head:
                if snake.head.distance(segment)<10:
                    is_Game_on=False
    screen.clear()
    screen.bgcolor("black")

    score.goto(0,0)
    score.displayScore()
    time.sleep(3)
    score.clear()
    input=screen.textinput(f"Your Score Is: {score.score}","Play Again?")
screen.exitonclick()

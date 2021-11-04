from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.hideturtle()
        self.goto(0,350)
        self.color("white")
        self.displayScore()

    def displayScore(self):
        self.clear()
        self.write(f"Score: {self.score}",align="center", font=("Calibri", 22, "bold"))

    def updateScore(self):
        self.score+=1
        self.displayScore()

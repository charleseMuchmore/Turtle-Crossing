from turtle import Turtle
FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0

    def update_scoreboard(self):
        self.goto(-280, 260)
        self.write(f"score: {self.score}", align="left", font=FONT)

    def add_point(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()


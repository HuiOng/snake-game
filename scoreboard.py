from turtle import Turtle
FONT = "Arial",20,"normal"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"Score is: {self.score}", False, align="center", font=(FONT))
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score is: {self.score}",False,align = "center", font=(FONT))

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", False, align="center", font=(FONT))

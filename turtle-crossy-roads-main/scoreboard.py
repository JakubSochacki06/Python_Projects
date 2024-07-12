from turtle import Turtle
FONT = ("Courier", 24, "normal")
SCORE = 0


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0 , 260)
        self.hideturtle()
        self.write(SCORE , False , align="center" , font=FONT)
        self.color("white")


    def increase_score(self):
        global SCORE
        self.clear()
        SCORE += 1
        self.write(SCORE, False, align="center", font=FONT)

    def game_over(self):
        global SCORE
        self.clear()
        self.goto(0 , 0)
        self.write(f"GAME OVER SCORE: {SCORE}", False, align="center", font=FONT)
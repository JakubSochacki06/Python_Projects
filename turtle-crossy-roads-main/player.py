from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(0 , -280)

    def move_up(self):
        self.goto(self.xcor() , self.ycor() + MOVE_DISTANCE)

    def check_position(self):
        if self.xcor() == 0 and self.ycor() == FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True
        else:
            return False



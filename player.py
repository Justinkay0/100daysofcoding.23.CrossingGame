from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.setheading(90)
        self.penup()
        self.new_level()

    def moving(self):
        if self.ycor() < FINISH_LINE_Y:
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(x=0, y=new_y)

    def new_level(self):
        self.setpos(STARTING_POSITION)

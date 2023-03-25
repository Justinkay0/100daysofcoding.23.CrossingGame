from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.penup()
        self.shape('square')
        self.color(random.choice(COLORS))
        self.setx(300)
        self.sety(random.randint(-260, 260))
        self.shapesize(stretch_wid=1, stretch_len=1.5)

    def car_moving(self, level):
        new_x = self.xcor() - (STARTING_MOVE_DISTANCE + ((level - 1) * MOVE_INCREMENT))
        self.goto(x=new_x, y=self.ycor())



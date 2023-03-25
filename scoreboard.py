from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.hideturtle()
        self.setpos(x=-280, y=280)
        self.level = 0
        self.update()

    def update(self):
        self.level += 1
        self.clear()
        self.write(arg=f'Level : {self.level}', font=FONT, align='left')

    def game_over(self):
        self.setpos(0, 0)
        self.write(arg=f'GAME OVER, you managed to beat level {self.level - 1}', font=FONT )

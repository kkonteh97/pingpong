from turtle import Turtle

def center():
    center_line = Turtle('square')
    center_line.hideturtle()
    center_line.color('white')
    center_line.penup()
    center_line.goto(0, -308)
    for i in range(1000):
        center_line.setheading(90)
        center_line.forward(7)
        center_line.pendown()
        center_line.forward(15)
        center_line.penup()


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_r = 0
        self.score_l = 0
        self.style = ('Arial', 20, 'normal')
        self.score = -1
        self.penup()
        self.setposition(0,160)

        self.color('white')
        self.hideturtle()
        self.write(f'{self.score_l}       {self.score_r}', font=self.style, align='center')
        self.rtrack()
        self.ltrack()
        center()

    def rtrack(self):
        self.score_r += 1
        self.clear()
        self.write(f'{self.score_l}       {self.score_r}', font=self.style, align='center')

    def ltrack(self):
        self.score_l += 1
        self.clear()
        self.write(f'{self.score_l}       {self.score_r}', font=self.style, align='center')
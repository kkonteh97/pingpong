from turtle import Turtle

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180








class Paddle:
    postion = [(270, 20), (270, 0), (270, -20), (-270, 0), (-270, 20), (-270, -20)]
    def __init__(self):
        self.pads = []
        self.new_paddle()
        self.paddle1 = self.pads[0]
        self.paddle1_mid = self.pads[1]
        self.paddle1_bot = self.pads[2]
        self.paddle2_top = self.pads[3]
        self.paddle2_mid = self.pads[4]
        self.paddle2_bot = self.pads[5]

        self.paddle2 = self.pads[3]

        self.heading()

    def heading(self):
        if self.paddle1_mid.ycor() == 180:
            self.paddle1_mid.setheading(DOWN)


    def add_paddle(self, position):
        paddle = Turtle('square')
        paddle.penup()
        paddle.setheading(UP)
        paddle.color('white')
        paddle.speed(5)
        paddle.goto(position)
        paddle.turtlesize(.4, 1, 1)
        self.pads.append(paddle)


    def move(self):
        new_x = self.paddle1_mid.xcor()
        new_y = self.paddle1_mid.ycor()
        self.paddle1.goto(new_x, new_y+10)
        self.paddle1_bot.goto(new_x, new_y-10)
        #self.paddle1_mid.forward(10)

        new_x = self.paddle2_mid.xcor()
        new_y = self.paddle2_mid.ycor()
        self.paddle2_top.goto(new_x, new_y + 10)
        self.paddle2_bot.goto(new_x, new_y - 10)
        self.paddle2_mid.forward(10)




    def new_paddle(self):
        for i in self.postion:
            self.add_paddle(i)


    def rebound(self):

        self.paddle1_mid.heading(DOWN)



    def up(self):
        self.paddle1_mid.forward(15)

    def down(self):
        self.paddle1_mid.backward(15)


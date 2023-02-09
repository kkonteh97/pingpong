from turtle import Screen, Turtle
from paddles import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=400)
screen.bgcolor("black")
screen.title("snake")
screen.tracer(8,25)



kato = Ball()
score = Scoreboard()
paddle = Paddle()

screen.onkey(paddle.up, "Up")
screen.onkey(paddle.down, "Down")
screen.listen()
game_one = True
while game_one:
    screen.update()
    time.sleep(.04)
    kato.move()
    paddle.move()
    if paddle.paddle2_mid.ycor() == 170:
        paddle.paddle2_mid.setheading(270)
    if paddle.paddle2_mid.ycor() == -170:
        paddle.paddle2_mid.setheading(90)
    if paddle.paddle1_mid.ycor() == 170:
        paddle.paddle1_mid.setheading(270)
    if paddle.paddle1_mid.ycor() == -170:
        paddle.paddle1_mid.setheading(90)
    if kato.xcor() > 290:
        kato.bounce_v()
        score.rtrack()
        kato.refresh()
    if kato.xcor() < -290:
        score.ltrack()
        kato.refresh()
        kato.bounce_v()
    if kato.ycor() > 180 or kato.ycor() < -180:
        kato.bounce_h()
    for t in paddle.pads:
        if t.distance(kato) <= 10 or paddle.paddle2.distance(kato) <= 10:
            kato.bounce_v()

screen.exitonclick()

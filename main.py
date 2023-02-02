from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game = True
while game:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce()


screen.exitonclick()

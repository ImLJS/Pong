from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game = True
while game:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() >= 285 or ball.ycor() <= -285:
        ball.bounce_y()

        # Detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x_r_paddle()

        # Detect collision with left paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x_l_paddle()

    if ball.xcor() > 380:
        ball.reset_position()
        ball.bounce_x()
        score.l_score += 1
        score.update_score()

    if ball.xcor() < -380:
        ball.reset_position()
        ball.bounce_x()
        score.r_score += 1
        score.update_score()

    if score.l_score == 10 or score.r_score == 10:
        game = False
        score.game_over()

screen.exitonclick()

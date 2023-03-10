# Import Statements
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

# Paddle Starting Position
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

# Key Press Listener
screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

# Main Game Loop
game = True
while game:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with Top and Bottom Wall
    if ball.ycor() >= 285 or ball.ycor() <= -285:
        ball.bounce_y()

        # Detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x_r_paddle()

        # Detect collision with left paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x_l_paddle()

        # Detect If Ball Miss Right Paddle
    if ball.xcor() > 380:
        ball.reset_position()
        ball.bounce_x_r_paddle()
        score.l_score += 1
        score.update_score()

        # Detect If Ball Miss Left Paddle
    if ball.xcor() < -380:
        ball.reset_position()
        ball.bounce_x_l_paddle()
        score.r_score += 1
        score.update_score()

        # Detect if Score is 10
    if score.l_score == 10 or score.r_score == 10:
        game = False
        score.game_over()

screen.exitonclick()

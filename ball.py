from turtle import Turtle


class Ball(Turtle):

    # Ball Appearance
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.pu()
        self.color('white')
        self.y_move = 10
        self.x_move = 10
        self.speed = 0
        self.move_speed = 0.1

    # Ball Movement
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # Ball Bounce from Top and Bottom Walls
    def bounce_y(self):
        self.y_move *= -1

    # Ball Bounce from Left Paddle
    def bounce_x_l_paddle(self):
        self.x_move = (abs(self.x_move))
        self.move_speed *= 0.9

    # Ball Bounce from Right Paddle
    def bounce_x_r_paddle(self):
        self.x_move = -(abs(self.x_move))
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1

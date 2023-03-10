from turtle import Turtle


class Paddle(Turtle):

    # Paddle Appearance
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.pu()
        self.goto(position)

    # Paddle Up Movement
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    # Paddle Down Movement
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


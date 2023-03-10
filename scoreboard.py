from turtle import Turtle


class Scoreboard(Turtle):

    # Scoreboard Appearance
    def __init__(self):
        super().__init__()
        self.color('white')
        self.pu()
        self.hideturtle()
        self.goto(0,280)
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    # Score Update
    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align='center', font=('Courier', 80, 'normal'))
        self.goto(100, 200)
        self.write(self.r_score, align='center', font=('Courier', 80, 'normal'))

    # Game Over Screen
    def game_over(self):
        self.goto(0,0)
        self.write('Game Over', align='center', font=('Courier', 80, 'normal'))

from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.setposition(x=-100, y=190)
        self.write(arg=self.l_score, align="center", font=("Courier", 40, "normal"))
        self.setposition(x=100, y=190)
        self.write(arg=self.r_score, align="center", font=("Courier", 40, "normal"))

    def update_l_point(self):
        self.l_score += 1
        self.update_score_board()

    def update_r_point(self):
        self.r_score += 1
        self.update_score_board()
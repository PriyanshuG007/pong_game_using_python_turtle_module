from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_position):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setposition(x=x_position, y=0)
        self.move_up()
        self.move_down()

    def move_up(self):
        new_y = self.ycor() + 30
        self.setposition(x=self.xcor(), y=new_y)

    def move_down(self):
        new_y = self.ycor() - 30
        self.setposition(x=self.xcor(), y=new_y)






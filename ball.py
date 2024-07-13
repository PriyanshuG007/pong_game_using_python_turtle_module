from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_movement = 10
        self.y_movement = 10
        self.ball_speed = 0.1

    def move_ball(self):
        random_x = self.xcor() + self.x_movement
        random_y = self.ycor() + self.y_movement
        self.setposition(x=random_x, y=random_y)

    def bounce_y(self):
        self.y_movement *= -1

    def bounce_x(self):
        self.x_movement *= -1
        self.ball_speed *= 0.95

    def reset_position(self):
        self.setposition(x=0, y=0)
        self.ball_speed = 0.1
        self.bounce_x()

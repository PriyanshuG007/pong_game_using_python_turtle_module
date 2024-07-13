from turtle import Screen
from paddles import Paddle
from ball import Ball
from score_board import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=500)
screen.title("Pong Game")
screen.tracer(0)

paddle_r = Paddle(x_position=360)
paddle_l = Paddle(x_position=-360)

ball = Ball()
score = ScoreBoard()

screen.listen()
screen.onkey(paddle_r.move_up, "p")
screen.onkey(paddle_r.move_down, ".")

screen.onkey(paddle_l.move_up, "w")
screen.onkey(paddle_l.move_down, "z")

game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move_ball()

    if ball.ycor() > 230 or ball.ycor() < -220:
        ball.bounce_y()

    if ball.distance(paddle_r) < 50 and ball.xcor() > 335:
        ball.bounce_x()

    if ball.distance(paddle_l) < 50 and ball.xcor() < -335:
        ball.bounce_x()

    if ball.xcor() > 370:
        ball.reset_position()
        score.update_l_point()

    if ball.xcor() < -370:
        ball.reset_position()
        score.update_r_point()


screen.exitonclick()

from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

turtle = Turtle()
screen = Screen()
scoreboard = Scoreboard()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong Game")
screen.tracer(0)
sp_x = 10
sp_y = 10

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")


taps=0
speed=0.04

game_is_on = True

while game_is_on:
    time.sleep(speed)
    screen.update()
    ball.move(sp_x, sp_y)

    # detect collision with wall
    if (ball.ycor() > 280 or ball.ycor() < -280):
        sp_y = -sp_y


    # detect collision with paddle
    if ((ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320)):
        sp_x = -(sp_x)



    # if ball goes out of bounds
    if (ball.xcor() > 390):
        ball.refresh()
        scoreboard.l_update()
        sp_x = -sp_x

    if (ball.xcor() < -390):
        ball.refresh()
        scoreboard.r_update()
        sp_x = -sp_x

screen.exitonclick()

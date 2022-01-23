from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle((375, 0))
left_paddle = Paddle((-375, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # ball needs to bounce back
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 350:
        ball.bounce_x()

    if ball.distance(left_paddle) < 50 and ball.xcor() < -350:
        ball.bounce_x()

    # If a player misses
    if ball.xcor() > 395:
        ball.reset_position()
        scoreboard.left_point()

    if ball.xcor() < -395:
        ball.reset_position()
        scoreboard.right_point()

screen.exitonclick()

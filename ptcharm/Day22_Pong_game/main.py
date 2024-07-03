from turtle import Turtle, Screen
import time
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
scoreboard = Scoreboard()
ball = Ball()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

run_game = True

while run_game:
    time.sleep(0.05)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.bounce_y()

    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.bounce_x()
        ball.home()

    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.bounce_x()
        ball.home()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


screen.exitonclick()
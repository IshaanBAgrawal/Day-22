from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard
from game_icons import WinnerTurtle, ExitGame


screen = Screen()
screen.tracer(0)
paddle_r = Paddle(350, 0)
paddle_l = Paddle(-350, 0)
ball = Ball()
scoreboard = ScoreBoard()
winner_turtle = WinnerTurtle()
exit_game = ExitGame()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("The Pong Game")

screen.listen()
screen.onkey(paddle_r.move_up, "Up")
screen.onkey(paddle_l.move_up, "W")
screen.onkey(paddle_l.move_up, "w")

screen.onkey(paddle_r.move_down, "Down")
screen.onkey(paddle_l.move_down, "S")
screen.onkey(paddle_l.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        screen.tracer(0)
        ball.bounce_x()
        ball.goto(x=0, y=0)
        scoreboard.l_point()
        ball.move_speed = 0.1
        time.sleep(1.0)

    if ball.xcor() < -380:
        screen.tracer(0)
        ball.bounce_x()
        ball.goto(x=0, y=0)
        scoreboard.r_point()
        ball.move_speed = 0.1
        time.sleep(1.0)

    if scoreboard.score_l == 10:
        game_is_on = False
        scoreboard.l_status = "Win"
        scoreboard.r_status = "Lose"

    if scoreboard.score_r == 10:
        game_is_on = False
        scoreboard.r_status = "Win"
        scoreboard.l_status = "Lose"

if scoreboard.r_status == "Win":
    winner_turtle.r_win()
if scoreboard.l_status == "Win":
    winner_turtle.l_win()

exit_game.exit()

screen.exitonclick()

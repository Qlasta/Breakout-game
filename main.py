from turtle import Turtle, Screen
from ball import Ball
from paddle import Paddle
import time
from wall import Bricks
from score import Score

# screen
screen = Screen()
screen.bgcolor("black")
screen.setup(600,400)
screen.title("Breakout game")
screen.tracer(0)

# game elements
paddle = Paddle()
ball = Ball()
wall = Bricks()
points = Score()
lives = Score()
points.write_points()
lives.write_lives()

# game controls
screen.listen()
screen.onkey(paddle.move_right,"Right")
screen.onkey(paddle.move_left,"Left")

game_is_on = True

# game rules

while game_is_on:
    time.sleep(ball.speed)
    ball.ball_move()
    ball_top_y = ball.ycor() + 10
    ball_bottom_y = ball.ycor() - 10
    ball_left_x = ball.xcor() - 10
    ball_right_x = ball.xcor() + 10
    ball_x = ball.xcor()
    # bounces wall
    if ball_right_x == 300 or ball_left_x == -300:
        ball.bounce_vertical()
    # bounces paddle
    if ball_bottom_y == -170 and (paddle.xcor()-50 <= ball_right_x and ball_left_x <= paddle.xcor()+50):
        ball.bounce_horizontal()
    # touches the abyss
    if ball_bottom_y == -190:
        time.sleep(3)
        ball.start_position()
        ball.bounce_horizontal()
        lives.write_lives()
    # touches top
    if ball_top_y == 250:
        ball.bounce_horizontal()

    for brick in wall.wall:
        brick_start_x = brick.xcor() - 30
        brick_end_x = brick.xcor() + 30
        brick_y = brick.ycor()
        # touches brick on bottom
        if brick_y == ball_top_y and brick_end_x >= ball_x >= brick_start_x:
            wall.wall.remove(brick)
            brick.goto(1000,1000)
            points.write_points()
            ball.bounce_horizontal()
        # touches brick on top
        if brick_y == ball_bottom_y and brick_end_x >= ball_x >= brick_start_x:
            wall.wall.remove(brick)
            brick.goto(1000, 1000)
            points.write_points()
            ball.bounce_horizontal()
        # ball touches brick on side
        if (brick_start_x == ball_right_x or brick_end_x == ball_left_x) and brick_y-10 < ball_top_y:
            ball.bounce_vertical()
            wall.wall.remove(brick)
            brick.goto(1000, 1000)
            points.write_points()
    # there are no bricks left
    if len(wall.wall) == 0:
        points.you_won()
        game_is_on = False
    # there are no lives left
    if lives.lives == 0:
        lives.game_over()
        game_is_on = False

    screen.update()


screen.exitonclick()
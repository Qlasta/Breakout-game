from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        """ Creates ball, sets speed, moving step size, puts to position. """
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.speed = 0.05
        self.step_x = 10
        self.step_y = 10
        self.start_position()


    def ball_move(self):
        """ Moves ball from current x, y postions adding step and dirrection"""
        self.goto(self.xcor()+self.step_x, self.ycor()+self.step_y)

    def bounce_horizontal(self):
        """ Changes to the opposite direction to up or down."""
        self.step_y *= -1

    def bounce_vertical(self):
        """ Changes to the opposite direction to left or right."""
        self.step_x *= -1

    def start_position(self):
        """ Puts to start position."""
        self.setposition(0, -160)
        self.speed *= 0.9



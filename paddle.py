from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        """ Creates paddle on screen bottom, size 1:5"""
        super().__init__()
        self.shape("square")
        self.fillcolor("white")
        self.shapesize(1, 5)
        self.penup()
        self.setposition(0, -180)

    def move_right(self):
        """ Move paddle right by 20px"""
        current_x = self.xcor()
        self.goto(current_x + 20, self.ycor())

    def move_left(self):
        """ Move paddle right by 20px."""
        current_x = self.xcor()
        self.goto(current_x - 20, self.ycor())

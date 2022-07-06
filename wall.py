from turtle import Turtle

class Bricks():
    def __init__(self):
        """ Adds three rows of bricks."""
        self.wall = []
        self.add_brick_row("green", 1)
        self.add_brick_row("yellow", 2)
        self.add_brick_row("red",3)

    def add_brick_row(self, color, row):
        """ Adds bricks in the row and adds to the bricks list, you need to set color and row number (1 is top row)"""
        b = 0
        row_position = row * 30
        for n in range(9):
            brick = Turtle()
            brick.shape("square")
            brick.shapesize(1,3)
            brick.penup()
            brick.setposition(-265 + b, 200 - row_position)
            b += 65
            brick.color(color)
            self.wall.append(brick)


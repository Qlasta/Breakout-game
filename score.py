from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        """Creates Lives or Points turtle,set color to white and set starting points and lives."""
        super().__init__()
        self.penup()
        self.hideturtle()
        self.lives = 4
        self.score = -1
        self.color("white")

    def write_points(self):
        """ Add one point and writes new amount."""
        self.clear()
        self.score += 1
        self.setposition(240,-180)
        self.write(f"Points: {self.score}")

    def write_lives(self):
        """ Removes one life and writes new amount."""
        self.clear()
        self.lives -= 1
        self.setposition(-280, -180)
        self.write(f"Lives: {self.lives}")

    def game_over(self):
        """ Writes 'game over'. """
        self.clear()
        self.setposition(0,0)
        self.color("red")
        self.write("GAME OVER", False, "center", ("Ariel", 30, "normal"))

    def you_won(self):
        """ Writes 'you won'. """
        self.clear()
        self.setposition(0, 0)
        self.color("green")
        self.write("YOU WON!", False, "center", ("Ariel", 30, "normal"))





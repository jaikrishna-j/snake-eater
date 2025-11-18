import random
import turtle


class Food:
    def __init__(self):
        self.body = turtle.Turtle()
        self.body.speed(0)
        self.body.shape("circle")
        self.body.color("#ffcc00")
        self.body.penup()
        self.body.hideturtle()

    def reposition(self):
        x = random.randint(-290, 270)
        y = random.randint(-240, 240)
        self.body.goto(x, y)

    def show(self):
        self.body.showturtle()

    def hide(self):
        self.body.hideturtle()

    def distance_to(self, other):
        return self.body.distance(other)


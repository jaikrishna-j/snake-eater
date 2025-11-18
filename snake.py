import turtle


OPPOSITE_DIRECTIONS = {
    "up": "down",
    "down": "up",
    "left": "right",
    "right": "left",
}


class Snake:
    MOVE_DISTANCE = 20

    def __init__(self):
        self.head = turtle.Turtle()
        self.head.speed(0)
        self.head.shape("square")
        self.head.color("#4cd964")
        self.head.penup()
        self.head.hideturtle()
        self.segments = []
        self.direction = "stop"

    def reset(self):
        self.direction = "stop"
        self.head.goto(0, 0)
        self.head.showturtle()
        for segment in self.segments:
            segment.hideturtle()
            segment.goto(1000, 1000)
        self.segments.clear()

    def hide(self):
        self.head.hideturtle()
        for segment in self.segments:
            segment.hideturtle()

    def set_direction(self, new_direction):
        if new_direction == OPPOSITE_DIRECTIONS.get(self.direction):
            return
        self.direction = new_direction

    def move(self):
        if self.direction == "stop":
            return

        for index in range(len(self.segments) - 1, 0, -1):
            x = self.segments[index - 1].xcor()
            y = self.segments[index - 1].ycor()
            self.segments[index].goto(x, y)

        if len(self.segments) > 0:
            x = self.head.xcor()
            y = self.head.ycor()
            self.segments[0].goto(x, y)
            for segment in self.segments:
                segment.showturtle()

        if self.direction == "up":
            self.head.sety(self.head.ycor() + self.MOVE_DISTANCE)
        elif self.direction == "down":
            self.head.sety(self.head.ycor() - self.MOVE_DISTANCE)
        elif self.direction == "left":
            self.head.setx(self.head.xcor() - self.MOVE_DISTANCE)
        elif self.direction == "right":
            self.head.setx(self.head.xcor() + self.MOVE_DISTANCE)

    def grow(self):
        segment = turtle.Turtle()
        segment.speed(0)
        segment.shape("square")
        segment.color("yellow")
        segment.penup()
        segment.goto(1000, 1000)
        self.segments.append(segment)

    def collided_with_self(self):
        for segment in self.segments:
            if self.head.distance(segment) < 20:
                return True
        return False


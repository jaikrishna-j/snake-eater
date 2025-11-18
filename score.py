import turtle


class ScoreBoard:
    def __init__(self, screen):
        self.screen = screen
        self.score = 0
        self.high_score = 0

        self.score_writer = turtle.Turtle()
        self.score_writer.speed(0)
        self.score_writer.color("white")
        self.score_writer.penup()
        self.score_writer.hideturtle()

        self.overlay_writer = turtle.Turtle()
        self.overlay_writer.hideturtle()
        self.overlay_writer.penup()

        self.play_button = turtle.Turtle()
        self.play_button.hideturtle()
        self.play_button.penup()

        self.button_bounds = {"left": -80, "right": 80, "top": -200, "bottom": -240}
        self.button_active = False

        self.update_score_display()

    def update_score_display(self):
        self.score_writer.clear()
        self.score_writer.goto(0, 300)
        self.score_writer.write(
            f"Score : {self.score}    High Score : {self.high_score}",
            align="center",
            font=("courier", 24, "bold"),
        )
        self.screen.title("Snake Eater")

    def reset_score(self):
        self.score = 0
        self.update_score_display()

    def add_point(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
        self.update_score_display()

    def show_overlay(self, title, subtitle="", color="red"):
        self.overlay_writer.clear()
        self.overlay_writer.color(color)
        self.overlay_writer.goto(0, 40)
        self.overlay_writer.write(title, align="center", font=("Courier", 48, "bold"))
        if subtitle:
            self.overlay_writer.goto(0, -20)
            self.overlay_writer.write(
                subtitle, align="center", font=("Courier", 24, "bold")
            )
        self.draw_play_button()

    def show_start_screen(self):
        self.show_overlay("SNAKE EATER", "Click PLAY to start", color="white")

    def show_game_over(self):
        self.show_overlay("YOU DIED", f"Score : {self.score}", color="red")

    def hide_overlay(self):
        self.overlay_writer.clear()
        self.clear_play_button()

    def draw_play_button(self):
        self.play_button.clear()
        self.play_button.goto(self.button_bounds["left"], self.button_bounds["top"])
        self.play_button.pendown()
        self.play_button.begin_fill()
        self.play_button.fillcolor("#1c5f2c")
        for _ in range(2):
            self.play_button.forward(
                self.button_bounds["right"] - self.button_bounds["left"]
            )
            self.play_button.right(90)
            self.play_button.forward(
                self.button_bounds["top"] - self.button_bounds["bottom"]
            )
            self.play_button.right(90)
        self.play_button.end_fill()
        self.play_button.penup()
        text_y = (self.button_bounds["top"] + self.button_bounds["bottom"]) / 2 - 10
        text_x = (self.button_bounds["left"] + self.button_bounds["right"]) / 2
        self.play_button.goto(text_x, text_y)
        self.play_button.color("white")
        self.play_button.write("PLAY", align="center", font=("Courier", 20, "bold"))
        self.play_button.color("#28a745")
        self.button_active = True

    def clear_play_button(self):
        self.play_button.clear()
        self.button_active = False

    def is_play_button_clicked(self, x, y):
        return (
            self.button_active
            and self.button_bounds["left"] <= x <= self.button_bounds["right"]
            and self.button_bounds["bottom"] <= y <= self.button_bounds["top"]
        )


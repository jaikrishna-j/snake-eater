import turtle
import time

from food import Food
from score import ScoreBoard
from snake import Snake

screen = turtle.Screen()
screen.title("Snake Eater")
screen.setup(width=700, height=700)
screen.tracer(0)
screen.bgcolor("#020916")

# Soft grid background inside the border
bg = turtle.Turtle()
bg.hideturtle()
bg.speed(0)
bg.color("#101826")
bg.penup()
for x in range(-280, 301, 20):
    bg.goto(x, -240)
    bg.pendown()
    bg.goto(x, 240)
    bg.penup()
for y in range(-240, 241, 20):
    bg.goto(-300, y)
    bg.pendown()
    bg.goto(280, y)
    bg.penup()

# Creating border
border = turtle.Turtle()
border.hideturtle()
border.speed(0)
border.pensize(4)
border.penup()
border.goto(-310, 250)
border.pendown()
border.color("#ff3333")
for _ in range(2):
    border.forward(620)
    border.right(90)
    border.forward(520)
    border.right(90)
border.penup()

snake = Snake()
food = Food()
scoreboard = ScoreBoard(screen)

base_delay = 0.1
delay = base_delay
game_running = False


def start_game():
    global game_running, delay
    delay = base_delay
    snake.reset()
    food.reposition()
    food.show()
    scoreboard.reset_score()
    scoreboard.hide_overlay()
    game_running = True


def end_game():
    global game_running
    if not game_running:
        return
    game_running = False
    snake.hide()
    food.hide()
    scoreboard.show_game_over()


def handle_click(x, y):
    if not game_running and scoreboard.is_play_button_clicked(x, y):
        start_game()


screen.listen()
screen.onkeypress(lambda: snake.set_direction("up"), "Up")
screen.onkeypress(lambda: snake.set_direction("down"), "Down")
screen.onkeypress(lambda: snake.set_direction("left"), "Left")
screen.onkeypress(lambda: snake.set_direction("right"), "Right")
screen.onclick(handle_click)

scoreboard.show_start_screen()

try:
    while True:
        screen.update()
        if game_running:
            snake.move()

            if snake.head.distance(food.body) < 20:
                food.reposition()
                snake.grow()
                scoreboard.add_point()
                delay = max(0.02, delay - 0.001)

            if (
                snake.head.xcor() > 280
                or snake.head.xcor() < -300
                or snake.head.ycor() > 240
                or snake.head.ycor() < -240
            ):
                end_game()

            if snake.collided_with_self():
                end_game()

            time.sleep(delay)
        else:
            time.sleep(0.05)
except turtle.Terminator:
    pass
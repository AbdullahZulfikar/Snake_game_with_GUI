from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()

screen.setup(width=700, height=600)
screen.tracer(0)
screen.title("Snake Game")
screen.bgpic("background4.jpg")
screen.listen()

snake = Snake()
food = Food()
score = ScoreBoard()

screen.onkey(snake.Up, "w")
screen.onkey(snake.Down, "s")
screen.onkey(snake.Left, "a")
screen.onkey(snake.Right, "d")


is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.Move()
    # to check the detection
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extent()
        score.Score()
    if snake.head.xcor() > 299 or snake.head.xcor() < -299 or snake.head.ycor() < -250 or snake.head.ycor() > 250:
        snake.reset()
        score.reset()

    new_segments = snake.segments[1:]
    for segments in new_segments:
        if snake.head.distance(segments) < 15:
            snake.reset()
            score.reset()





screen.exitonclick()

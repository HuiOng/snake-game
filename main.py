from turtle import Turtle, Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
food.refresh()
scoreboard = Scoreboard()


snake.create_snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.update_score()

    #detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
#BUILDING MY OWN SNAKE GAME
#THINGS TO MAKE IT HAPPEN WITH CODE
#Create a snake body
#Move the snake
#Control the snake
#Detect collision with food
#Create a scoreboard
#Detect collision with wall
#Detect collision with tail


from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


#window that shows up

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")        #parameters: title string :- a string thst s shown in the titlebar of the turtle graphics window
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

#control the snakes
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


    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()


    # if Detect collision with tail
    for segment in snake.segment[1:]:

        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()







screen.exitonclick()















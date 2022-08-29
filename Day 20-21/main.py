from snake import Snake
from lib import setup_screen
from food import Food
from scoreboard  import Scoreboard
import time



screen = setup_screen()
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True
while game_is_on == True:
    snake.move()
    screen.update()
    time.sleep(0.09)

    if snake.head.distance(food) < 20:
        snake.attach_body()
        food.random_pos()
        scoreboard.add_score()
    
    if snake.detect_collision_with_wall():
        game_is_on =False
        scoreboard.game_over()
    
    for snake_body in snake.segments[1:]:
        if snake.head.distance(snake_body) < 10:
            game_is_on =False
            scoreboard.game_over()


screen.exitonclick()

from turtle import Screen, Turtle
# from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# snake = Snake()
# snake_segments = snake.segments

snake = []

for _ in range(3):
    t = Turtle()
    t.shape("square")
    t.color("white")
    t.penup()
    t.goto(x=-20 + (_ * 20), y=0)
    snake.append(t)

screen.update()

game_is_on = True
while game_is_on:
    screen.update()
    for seg_num in range(len(snake)-1, 0, -1):
        new_x = snake[seg_num - 1].xcor()
        new_y = snake[seg_num - 1].ycor()
        snake[seg_num].goto(new_x, new_y)
    snake[0].forward(20)

screen.exitonclick()

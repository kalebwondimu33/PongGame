from turtle import Screen
from paddle import Paddle
from ball import Ball
from scorebord import Scorebord
import time
screen=Screen()
r_padd=Paddle(350,0)
l_padd=Paddle(-350,0)
ball=Ball()
score=Scorebord()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("PongGame")
screen.tracer(0)
screen.listen()
screen.onkey(r_padd.go_up,"Up")
screen.onkey(r_padd.go_down,"Down")
screen.onkey(l_padd.go_up, "w")
screen.onkey(l_padd.go_down, "s")
game_on=True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    #detect collision with wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    #detct collisio with right paddle
    if ball.distance(r_padd)<50 and ball.xcor()>320 or ball.distance(l_padd)<50 and ball.xcor()<-320:
        ball.bounce_x()
    #detect r_paddle misses
    if ball.xcor()>380:
        ball.reset_position()
        score.l_point()
    #detect l_paddle misses
    if ball.xcor()<-380:
        ball.reset_position()
        score.r_point()
    ball.move()


screen.exitonclick()

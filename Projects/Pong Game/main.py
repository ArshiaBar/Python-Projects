from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from board import Score
import time


screen=Screen()
screen.tracer(0)

turtle=Turtle()

screen.setup(800,600)
screen.title("Pong Game")
screen.bgcolor("black")


turtle.hideturtle()
turtle.speed("fastest")
turtle.color("white")
turtle.penup()
turtle.goto(0,-270)
turtle.setheading(90)

for _ in range(28):
    turtle.pendown()
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)

paddle=Paddle((350,0))
paddle2=Paddle((-350,0))

screen.listen()
screen.onkey(paddle.up,"Up")
screen.onkey(paddle.down,"Down")
screen.onkey(paddle2.up,"w")
screen.onkey(paddle2.down,"s")

ball=Ball()

board=Score()

cont=True
while cont:
    screen.update()
    ball.move()
    if ball.ycor()==280 or ball.ycor()==-280:
        ball.bounce()
    if ball.xcor()==paddle.xcor()-10 and ball.distance(paddle)<=50 or ball.xcor()==paddle2.xcor()+10 and ball.distance(paddle2)<=50:
        ball.bouncex()
        ball.time*=0.9
    if ball.xcor()==400:
        ball.reset()
        ball.bouncex()
        board.sco2()
    if ball.xcor()==-400:
        ball.reset()
        ball.bouncex()
        board.sco()
    time.sleep(ball.time)

screen.exitonclick()
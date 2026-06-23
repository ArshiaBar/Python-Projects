from turtle import Turtle
from random import randint

class Obj(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5,0.5)
        self.color("blue")
        self.penup()
        self.speed("fastest")
        self.relocate()

    def relocate(self):
        self.goto(randint(-280,280),randint(-280,280))

from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.scor=0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.goto(0,270)
        self.writer()

    def writer(self):
        self.write(f"Score: {self.scor}",False,"center",("Courier",18,"normal"))

    def scorer(self):
        self.clear()
        self.scor += 1
        self.writer()

    def over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, "center", ("Courier", 18, "normal"))

from turtle import Turtle

class Snake:
    def __init__(self):
        self.squares=[]
        self.create_snake()
        self.head= self.squares[0]

    def create_snake(self):
        pos = [(0,0), (-20,0), (-40,0)]
        for _ in pos:
            self.extend(_)

    def extend(self, position):
        s = Turtle("square")
        s.color("white")
        s.penup()
        s.speed("fastest")
        s.goto(position)
        self.squares.append(s)

    def move(self):
        for _ in range(len(self.squares) - 1, 0, -1):
            self.squares[_].goto(self.squares[_ - 1].xcor(), self.squares[_ - 1].ycor())
        self.head.forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
    def left(self):
        if self.head.heading() !=0:
            self.head.setheading(180)
    def down(self):
        if self.head.heading() !=90:
            self.head.setheading(-90)

    def add(self):
        self.extend(self.squares[-1].position())



from turtle import Screen
import time

screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
cont = True
snake=Snake()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")
screen.onkey(snake.down,"Down")
object=Obj()
score=Score()

while cont:
    screen.update()
    snake.move()
    if snake.head.distance(object) < 15:
        object.relocate()
        score.scorer()
        snake.add()
    if snake.head.xcor()>290 or snake.head.xcor() <-290 or snake.head.ycor()>290 or snake.head.ycor() <-290:
        cont=False
        score.over()
    for square in snake.squares[1:]:
        if snake.head.distance(square) <10:
            cont = False
            score.over()
    time.sleep(0.1)

screen.exitonclick()
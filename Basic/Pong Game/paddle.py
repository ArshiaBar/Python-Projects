from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.speed("fastest")
        self.setheading(90)
        self.shape("square")
        self.shapesize(1,5)
        self.color("white")
        self.penup()
        self.goto(position)

    def up(self):
        self.goto(self.xcor(),self.ycor()+10)
    def down(self):
        self.goto(self.xcor(),self.ycor()-10)






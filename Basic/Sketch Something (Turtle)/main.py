from turtle import Turtle, Screen

m=Turtle()
screen=Screen()

def forward():
    m.forward(10)

def backward():
    m.backward(10)

def clock():
    m.right(10)

def counter():
    m.left(10)

def clear():
    m.home()
    m.clear()


screen.listen()
screen.onkey(forward, 'w')
screen.onkey(backward, 's')
screen.onkey(clock, 'd')
screen.onkey(counter, 'a')
screen.onkey(clear, 'c')


screen.exitonclick()
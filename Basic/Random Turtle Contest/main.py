from turtle import Turtle, Screen
from random import randint

colors=["red","blue","orange","purple","green","yellow"]
yaxes=[-125,-75,-25,25,75,125]
turtles=[]
cont=False
screen = Screen()

screen.setup(500,400)
c=screen.textinput("Make your bet","Which turtle color will win the race? ").lower()

for _ in range(6):
    tim=Turtle("turtle")
    tim.color(colors[_])
    tim.penup()
    tim.goto(-230, yaxes[_])
    turtles.append(tim)

if c:
    cont=True

while cont:
    for turtle in turtles:
        turtle.forward(randint(0,10))
        if turtle.xcor() >230:
            cont=False
            if c==turtle.pencolor():
                print("Win!")
            else:
                print("Lose!")
            print(f"winner's color is {turtle.pencolor()}.")

screen.exitonclick()
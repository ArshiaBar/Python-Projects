import turtle as t
import random as ra
import colorgram as c

t.colormode(255)

mouse=t.Turtle()
screen= t.Screen()

mouse.speed("fastest")
mouse.penup()
mouse.hideturtle()

colors=c.extract('spot.jpg', 30)


mouse.setheading(-45)
mouse.forward(300)
mouse.setheading(180)
mouse.forward(500)
mouse.setheading(0)

for _ in range(10):
    for _ in range(10):
        mouse.dot(20, ra.choice(colors).rgb)
        mouse.forward(50)

    mouse.setheading(90)
    mouse.forward(50)
    mouse.setheading(180)
    mouse.forward(500)
    mouse.setheading(0)


screen.exitonclick()
from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.scor=0
        self.scor2=0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.update()

    def sco2(self):
        self.scor2 +=1
        self.update()

    def sco(self):
        self.scor +=1
        self.update()

    def update(self):
        self.clear()
        self.goto(-50, 225)
        self.write(self.scor2, False, "center", ("Courier", 40, "normal"))
        self.goto(50, 225)
        self.write(self.scor, False, "center", ("Courier", 40, "normal"))



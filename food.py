from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("coral")
        self.speed("fastest")
        self.new_food()

    def new_food(self):
        random_xcor = random.randint(-280, 280)
        random_ycor = random.randint(-280, 280)
        self.goto(random_xcor, random_ycor)


import turtle as t
import random

tim = t.Turtle()

colors = ["red", "blue", "yellow", "green", "black"]
directions = [0, 90, 180,270]
tim.pensize(15)
tim.speed("fastest")

for n in range(200):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(directions))
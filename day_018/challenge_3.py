# Challenge 3 - Drawing Different Shapes

import turtle as t
import random

colors = ["red", "blue", "yellow", "green", "black"]
tim = t.Turtle()

tim = t.Turtle()

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
          tim.forward(100)
          tim.right(angle)

for n in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(n)


t.done()
# Challenge 2 - Draw a Dashed Line

import turtle as t

window = t.Screen()
pen = t.Turtle()

for _ in range(15):
    pen.forward(10)
    pen.penup()
    pen.forward(10)
    pen.pendown()

t.done()
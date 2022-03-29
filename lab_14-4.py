# Author: SMR (AMDG) 3/18/22

import turtle

# window size
window = turtle.Screen()

# name window
window.title("Lab 14-4")

# turtle customization
t = turtle.Turtle()
t.fillcolor("red")
t.speed(1)

# movement
t.stamp()
t.goto(120, 120)
t.fillcolor("purple")
t.begin_fill()
for x in range (4):
    t.forward(100)
    t.right(90)
t.end_fill()

window.mainloop()
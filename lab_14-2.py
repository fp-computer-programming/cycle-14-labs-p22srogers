# Author: SMR (AMDG) 3/17/22
import turtle

# Setting window size
window = turtle.Screen()
window.setup(500, 500)
window.screensize(425, 425)

# naming the turtle
t = turtle.Turtle()

# movement
t.right(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)

window.mainloop()
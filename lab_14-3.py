# Author: SMR (AMDG) 3/17/22

import turtle

# Window Size
window = turtle.Screen()
window.setup(500, 500)
window.screensize(400, 400)

# Background color + Name
turtle.Screen().bgcolor("blue")
window.title("Lab 14-3")

# turtles name as well as pen color
t = turtle.Turtle()
t.shape("turtle")
t.pencolor("red")

# movements to create triangle
for x in range(3):
    t.right(180)
    t.forward(200)
    t.left(60)

window.mainloop()
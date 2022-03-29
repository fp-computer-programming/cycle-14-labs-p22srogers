# Author: SMR (AMDG) 3/18/22
import turtle

# windows
window = turtle.Screen()

# turtle customization propts
t = turtle.Turtle()
color = window.textinput("Color", "Enter the turtle color: ")
t.color(color)
t.shapesize(window.numinput("Size", "Enter the turtles size: "))

# Square function
def draw_square():
    t.fillcolor(color)
    t.begin_fill()
    for x in range(4):
        t.right(90)
        t.forward(100)
    t.end_fill()


# Clicks
window.onclick(draw_square(), btn=1)

window.mainloop()
# Author: SMR (AMDG) 3/18/22
import turtle

# movement functions
def move_for():
    t.forward(50)
def move_back():
    t.back(50)
def turn_left():
    t.left(90)
def turn_right():
    t.right(90)

# window size
window = turtle.Screen()

# turtle customization
t = turtle.Turtle()
t.fillcolor("blue")
t.speed(0)

#  key pressing
window.onkey(move_for, "Up")
window.onkey(move_back, "Down")
window.onkey(turn_left, "Left")
window.onkey(turn_right, "Right")
window.listen()


window.mainloop()
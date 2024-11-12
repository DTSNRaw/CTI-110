# Your name
# 10/29/2024
# p4lab1
# Use turtle examples

# Import turtle library
import turtle

# Set up the window and turtle object
window = turtle.Screen()
window.bgcolor("black")
tom = turtle.Turtle()

# Change features of turtle
tom.pensize(5)
tom.pencolor("black")
tom.shape("arrow")

# Function to move the turtle up
def move_up():
    tom.setheading(90)  # Pointing up
    tom.forward(30)
    tom.pencolor("white")

# Function to move the turtle down
def move_down():
    tom.setheading(270)  # Pointing down
    tom.forward(30)
    tom.pencolor("purple")

# Function to move the turtle left
def move_left():
    tom.setheading(180)  # Pointing left
    tom.forward(30)
    tom.pencolor("pink")

# Function to move the turtle right
def move_right():
    tom.setheading(0)  # Pointing right
    tom.forward(30)
    tom.pencolor("magenta")

# Bind the arrow keys to the movement functions
window.listen()
window.onkey(move_up, "Up")
window.onkey(move_down, "Down")
window.onkey(move_left, "Left")
window.onkey(move_right, "Right")

# Keep the window open until closed by the user
window.mainloop()

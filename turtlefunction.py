import turtle
z = turtle.Screen()
z.setup(200,200)

import turtle

# Get the screen object, which is like the main window
screen = turtle.Screen()

# Set the screen's title (optional)
screen.title("My Turtle Program")

# Set the width and height of the window in pixels
screen.setup(width=200, height=200)

# Create a turtle to see on the screen
t = turtle.Turtle()
t.shape("turtle")
t.forward(50)

# Keep the window open until you click on it
screen.exitonclick()
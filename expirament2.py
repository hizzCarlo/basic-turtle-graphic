import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the background color
turtle.bgcolor("white")

# Set the pen color and fill color
t.color("blue", "white")

# Set the pen size
t.pensize(5)

# Draw a blue square with red border
t.penup()
t.goto(-100, 100)
t.pendown()
t.begin_fill()
for i in range(4):
    t.forward(200)
    t.right(90)
t.end_fill()

# Draw two white rectangles in an "H" shape
t.penup()
t.goto(-50, 50)
t.pendown()
t.color("white")
t.begin_fill()
for i in range(2):
    t.forward(100)
    t.right(90)
    t.forward(25)
    t.right(90)
    t.forward(100)
    t.left(90)
    t.forward(25)
    t.left(90)
t.end_fill()

# Hide the turtle object
turtle.done()
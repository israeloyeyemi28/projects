import turtle

# Create a turtle object
t = turtle.Turtle()

# Customize the turtle's appearance
t.shape("turtle")
t.color("blue")
t.speed(2)

# Draw a square
for _ in range(4):
    t.forward(100)
    t.right(90)

# Move the turtle
t.penup()
t.goto(150, 0)
t.pendown()

# Draw a circle
t.color("red")
t.circle(50)

# Close the turtle graphics window
turtle.done()
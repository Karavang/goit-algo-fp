from turtle import Screen, Turtle

LENGTH = 100
CURSOR_SIZE = 20


def scaleLength(length):
    return (2 * (length / 2) ** 2) ** 0.5


def drawSquare(t, length):
    t.shapesize(length / CURSOR_SIZE)
    t.stamp()


def pythTree(t, length, level):
    if level < 1:
        return

    drawSquare(t, length)

    if level < 2:
        return

    scaled_length = scaleLength(length)

    t.forward(length)
    t.left(90)
    t.forward(length / 2)
    t.right(45)

    pythTree(t, scaled_length, level - 1)

    t.right(135)
    t.forward(length)
    t.left(45)

    pythTree(t, scaled_length, level - 1)

    t.left(135)
    t.forward(length / 2)
    t.right(90)
    t.backward(length)


screen = Screen()
screen.tracer(False)

turtle = Turtle()
turtle.hideturtle()
turtle.setheading(90)
turtle.shape("square")
turtle.penup()

pythTree(turtle, LENGTH, 6)

screen.update()
screen.exitonclick()

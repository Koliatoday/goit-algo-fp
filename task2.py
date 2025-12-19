"""Implementation of a Pythagoras Tree fractal using turtle graphics."""
import math
import turtle


def pythagoras_tree(t: turtle.Turtle, length: int, depth: int):
    """
    Draws a Pythagoras Tree-like fractal using recursion.
    Args:
        t: turtle.Turtle instance
        length: branch length
        depth: recursion depth
    """
    if depth == 0:
        return

    # Draw main branch
    t.forward(length)

    # Left branch
    t.left(45)
    pythagoras_tree(t, length * math.sqrt(2) / 2, depth - 1)

    # Right branch
    t.right(90)
    pythagoras_tree(t, length * math.sqrt(2) / 2, depth - 1)

    # Restore orientation and position
    t.left(45)
    t.backward(length)


def main():
    """Create and display a Pythagoras tree fractal."""
    screen = turtle.Screen()
    screen.setup(width=900, height=900)
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.color("firebrick")
    t.width(2)

    # Start position (bottom center)
    t.penup()
    t.goto(0, -380)
    t.setheading(90)
    t.pendown()

    # Draw trunk
    trunk_length = 100
    t.forward(trunk_length)

    # Draw crown
    pythagoras_tree(t, length=200, depth=8)

    screen.mainloop()


if __name__ == "__main__":
    main()

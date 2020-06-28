import turtle


def logic(iters, axiom, rules):
    start_string = axiom
    if iters == 0:
        return axiom
    end_string = ""
    for _ in range(iters):
        end_string = "".join(
            rules[i] if i in rules else i for i in start_string)
        start_string = end_string

    return end_string


def drawLogic(t, instructions, angle, distance):
    for i in instructions:
        if i == 'F':
            t.forward(distance)
        elif i == '+':
            t.right(angle)
        elif i == '-':
            t.left(angle)


def main(iterations, axiom, rules, angle, length=10, size=1, y_offset=0,
         x_offset=0, offset_angle=0, width=500, height=500):

    inst = logic(iterations, axiom, rules)

    t = turtle.Turtle()
    wn = turtle.Screen()
    wn.setup(width, height)

    t.up()
    t.backward(-x_offset)
    t.left(90)
    t.backward(-y_offset)
    t.left(offset_angle)
    t.down()
    t.speed(10)
    t.pensize(size)
    drawLogic(t, inst, angle, length)
    t.hideturtle()

    wn.exitonclick()


if __name__ == "__main__":
    main(axiom="F-F-F-F",
         rules={"F": "F-F+F+F-F"},
         iterations=2,
         angle=90)

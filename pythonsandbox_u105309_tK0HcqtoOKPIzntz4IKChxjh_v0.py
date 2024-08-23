import turtle


screen = turtle.Screen()
screen.bgcolor("black")


pen = turtle.Turtle()
pen.speed(10)

def draw_moon(x, y, radius):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color("white")
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()


def draw_star(x, y, size):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color("white")
    pen.begin_fill()
    for _ in range(5):
        pen.forward(size)
        pen.right(144)
        pen.forward(size)
        pen.right(144)
    pen.end_fill()


def draw_house(x, y):
    
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color("brown")
    pen.begin_fill()
    for _ in range(4):
        pen.forward(100)
        pen.left(90)
    pen.end_fill()
    pen.goto(x, y + 100)
    pen.color("red")
    pen.begin_fill()
    pen.goto(x + 50, y + 150)
    pen.goto(x + 100, y + 100)
    pen.goto(x, y + 100)
    pen.end_fill()


def draw_tree(x, y):
    # Draw the trunk
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color("saddle brown")
    pen.begin_fill()
    for _ in range(2):
        pen.forward(20)
        pen.left(90)
        pen.forward(40)
        pen.left(90)
    pen.end_fill()
    pen.goto(x - 15, y + 40)
    pen.color("green")
    pen.begin_fill()
    pen.circle(30)
    pen.end_fill()


def draw_mountains(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color("gray")
    pen.begin_fill()
    pen.goto(x + 200, y + 150)
    pen.goto(x + 400, y)
    pen.goto(x, y)
    pen.end_fill()
draw_moon(200, 150, 50)

# Draw some stars
draw_star(-200, 200, 20)
draw_star(-100, 250, 15)
draw_star(100, 220, 10)
draw_star(0, 280, 25)
draw_mountains(-300, -100)
draw_mountains(100, -100)
draw_house(-50, -200)
draw_tree(150, -200)
turtle.done()

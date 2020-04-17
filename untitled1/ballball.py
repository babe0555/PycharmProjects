import math
import random
import turtle

font = ("arial", "10", "bold")
# Screen settings
screen = turtle.Screen()
screen.setup(600, 600, 600, 0)
screen.bgcolor("black")
screen.tracer(0)

cells_2 = []
cells_1 = []


# Classes
class Pen(turtle.Turtle):
    def __init__(self, ):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.hideturtle()
        self.color("yellow")


class Bord(turtle.Turtle):  # Defines natural field and boarders
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.pencolor("orange")
        self.pensize(2)
        self.penup()
        self.speed(0)
        self.setpos(-230, -230)
        self.pendown()
        self.hideturtle()

    def draw(self):
        for i in range(4):
            self.forward(460)
            self.left(90)


class Cell_1(turtle.Turtle):  # Defines single cell, and its atrributes, and natural reactions
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("circle")
        self.shapesize(0.3)
        self.pencolor("white")
        self.setheading(random.randrange(0, 360))
        self.speed(0)
        self.speed = 0.4
        self.setpos(random.randrange(-220, 200), random.randrange(-220, 200))
        self.x = self.xcor()
        self.y = self.ycor()

    def move(self):
        self.forward(self.speed)
        if self.xcor() >= 220:
            self.left(48)
        if self.xcor() <= -220:
            self.left(48)
        if self.ycor() >= 220:
            self.left(48)
        if self.ycor() <= - 220:
            self.left(48)

    def redirect(self):
        self.left(90)

    def adder(self):
        for cell_1 in range(1):
            cell_1 = Cell_1()
            cells_1.append(cell_1)


class Cell_2(turtle.Turtle):  # Defines single cell, and its atrributes, and natural reactions
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("circle")
        self.shapesize(0.3)
        self.pencolor("red")
        self.setheading(random.randrange(0, 360))
        self.speed(0)
        self.speed = 0.4
        self.setpos(random.randrange(-220, 200), random.randrange(-220, 200))
        self.x = self.xcor()
        self.y = self.ycor()

    def move(self):
        self.forward(self.speed)
        if self.xcor() >= 220:
            self.left(48)
        if self.xcor() <= -220:
            self.left(48)
        if self.ycor() >= 220:
            self.left(48)
        if self.ycor() <= - 220:
            self.left(48)

    def redirect(self):
        self.left(90)

    def adder(self):
        for cell_2 in range(1):
            cell_2 = Cell_2()
            cells_2.append(cell_2)


# General functions
pen1 = Pen()


def counter():
    count = 0
    global cells_1
    for i in cells_1:
        count += 1
        pen1.setpos(-290, 280)
        pen1.clear()
        pen1.write("White cells: " + str(count), font=font)


def is_contact(object_1, object_2):  # defining the collision between cells using pythagorean theorem
    a = object_1.xcor() - object_2.xcor()
    b = object_1.ycor() - object_2.ycor()
    distance = math.sqrt((a ** 2) + (b ** 2))
    if distance < 20:
        return True
    else:
        return False


counter()
# OBJECTS
bord = Bord()
bord.draw()
for cell_2 in range(1):
    cell_2 = Cell_2()
    cells_2.append(cell_2)
for cell_1 in range(1):
    cell_1 = Cell_1()
    cells_1.append(cell_1)

running = True
while running:
    screen.update()
    for cell_2 in cells_2:
        cell_2.move()
    for cell_1 in cells_1:
        cell_1.move()
    for cell_1 in cells_1:
        if is_contact(cell_1, cell_2):
            cell_1.redirect()
            cell_2.redirect()
            cell_1.adder()
            cell_2.adder()
            cell_1.speed += 0.2
            cell_2.speed += 0.2
            counter()

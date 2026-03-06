import turtle
import math

SCALE = 30  # 1 единица = 30 пикселей


def draw_system(x_min, x_max, y_min, y_max):
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.color("gray")

    # Рисуем ось X
    t.penup()
    t.goto(x_min * SCALE, 0)
    t.pendown()
    t.goto(x_max * SCALE, 0)
    t.write(" X", font=("Arial", 12, "bold"))

    # Засечки и числа на оси X
    for x in range(x_min, x_max + 1):
        t.penup()
        t.goto(x * SCALE, -5)
        t.pendown()
        t.goto(x * SCALE, 5)
        if x != 0:  # Чтобы не накладывать 0 друг на друга
            t.penup()
            t.goto(x * SCALE, -20)
            t.write(str(x), align="center")

    # Рисуем ось Y
    t.penup()
    t.goto(0, y_min * SCALE)
    t.pendown()
    t.goto(0, y_max * SCALE)
    t.write(" Y", font=("Arial", 12, "bold"))

    # Засечки и числа на оси Y
    for y in range(y_min, y_max + 1):
        t.penup()
        t.goto(-5, y * SCALE)
        t.pendown()
        t.goto(5, y * SCALE)
        if y != 0:
            t.penup()
            t.goto(-20, y * SCALE - 7)
            t.write(str(y), align="right")


def plot_function():
    t = turtle.Turtle()
    t.speed(0)
    t.color("blue")
    t.pensize(2)
    t.penup()

    x = -7.0
    first = True
    while x <= 11.05:
        # Уравнение функции
        if x <= -3:
            y = 3
        elif -3 < x <= 3:
            y = 3 - math.sqrt(max(0, 9 - x ** 2))
        elif 3 < x <= 6:
            y = -2 * x + 9
        else:
            y = x - 9

        t.goto(x * SCALE, y * SCALE)
        if first:
            t.pendown()
            first = False
        x += 0.1
    t.hideturtle()


screen = turtle.Screen()
screen.setup(800, 600)
draw_system(-8, 12, -4, 5)  # С запасом для подписей
plot_function()
screen.mainloop()
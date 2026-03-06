import turtle
import random
import math


def draw_grid(r, scale):
    """Рисует оси и разметку, адаптированную под масштаб"""
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.color("gray")

    # Определяем, сколько единиц рисовать на осях (чуть больше области генерации)
    limit_x = int(2.5 * r)
    limit_y_max = int(2.5 * r)
    limit_y_min = int(1.5 * r)

    # Ось X
    t.penup();
    t.goto(-limit_x * scale, 0);
    t.pendown();
    t.goto(limit_x * scale, 0)
    t.write(" X", font=("Arial", 12, "bold"))
    for x in range(-limit_x, limit_x + 1):
        if x == 0: continue
        t.penup();
        t.goto(x * scale, -5);
        t.pendown();
        t.goto(x * scale, 5)
        t.penup();
        t.goto(x * scale, -20);
        t.write(str(x), align="center")

    # Ось Y
    t.penup();
    t.goto(0, -limit_y_min * scale);
    t.pendown();
    t.goto(0, limit_y_max * scale)
    t.write(" Y", font=("Arial", 12, "bold"))
    for y in range(-limit_y_min, limit_y_max + 1):
        if y == 0: continue
        t.penup();
        t.goto(-5, y * scale);
        t.pendown();
        t.goto(5, y * scale)
        t.penup();
        t.goto(-25, y * scale - 7);
        t.write(str(y), align="right")


def monte_carlo_adaptive():
    # 1. Ввод данных
    try:
        r_val = float(input("Введите радиус R: "))
        n_points = int(input("Введите количество точек N (рекомендуется 2000-5000): "))
    except ValueError:
        print("Ошибка: введите числовые значения.")
        return

    # 2. Расчет адаптивного масштаба
    # Мы хотим, чтобы область 4R помещалась в 600 пикселей
    scale = 500 / (4 * r_val) if r_val != 0 else 50

    screen = turtle.Screen()
    screen.setup(800, 700)
    screen.tracer(0, 0)  # Мгновенная отрисовка

    draw_grid(r_val, scale)

    t = turtle.Turtle()
    t.hideturtle()
    t.penup()

    hits = 0
    # Границы генерации (Bounding Box)
    x_min, x_max = -2 * r_val, 2 * r_val
    y_min, y_max = -r_val, 2 * r_val

    s_box = (x_max - x_min) * (y_max - y_min)
    s_real = (1 / 4) * math.pi * r_val ** 2 + 2 * r_val ** 2

    # 3. Цикл испытаний
    for _ in range(n_points):
        px = random.uniform(x_min, x_max)
        py = random.uniform(y_min, y_max)

        # Условия из вашей задачи
        in_circle = (px + r_val) ** 2 + (py - r_val) ** 2 <= r_val ** 2
        in_rect = (0 <= px <= 2 * r_val) and (-r_val <= py <= 0)

        t.goto(px * scale, py * scale)
        if in_circle or in_rect:
            hits += 1
            t.dot(3, "green")
        else:
            t.dot(3, "red")

    # 4. Расчет и вывод текста
    s_est = (hits / n_points) * s_box
    precision = (s_est / s_real) * 100 if s_real != 0 else 0

    # Исправленный вывод текста (координаты теперь зависят от масштаба и R)
    t.color("black")
    t.goto(-350, 300)
    text = (f"Радиус R = {r_val}\n"
            f"Точек N = {n_points}\n"
            f"Реальная S = {s_real:.2f}\n"
            f"Оценка S = {s_est:.2f}\n"
            f"Точность = {precision:.2f}%")
    t.write(text, font=("Courier", 12, "bold"))

    screen.update()
    print(f"Расчет завершен. Оценка площади: {s_est:.4f}")
    screen.mainloop()


if __name__ == "__main__":
    monte_carlo_adaptive()
import turtle
import math


class PiecewiseGrapher:
    def __init__(self, width=800, height=600, scale=30):
        """Инициализация окна и графического исполнителя"""
        self.scale = scale  # Масштаб: 1 математическая единица = 30 пикселей

        # Настройка экрана
        self.screen = turtle.Screen()
        self.screen.setup(width, height)
        self.screen.title("Лабораторная №7: Кусочно-заданная функция")

        # Настройка черепашки
        self.t = turtle.Turtle()
        self.t.speed(0)
        self.t.hideturtle()

    def draw_system(self, x_min, x_max, y_min, y_max):
        """Рисование координатных осей, засечек и подписей чисел"""
        self.t.color("gray")
        self.t.pensize(2)

        # Рисуем ось X
        self.t.penup()
        self.t.goto(x_min * self.scale, 0)
        self.t.pendown()
        self.t.goto(x_max * self.scale, 0)
        self.t.write(" X", font=("Arial", 12, "bold"))

        # Засечки и числа на оси X
        for x in range(x_min, x_max + 1):
            self.t.penup()
            self.t.goto(x * self.scale, -5)
            self.t.pendown()
            self.t.goto(x * self.scale, 5)
            if x != 0:
                self.t.penup()
                self.t.goto(x * self.scale, -20)
                self.t.write(str(x), align="center")

        # Рисуем ось Y
        self.t.penup()
        self.t.goto(0, y_min * self.scale)
        self.t.pendown()
        self.t.goto(0, y_max * self.scale)
        self.t.write(" Y", font=("Arial", 12, "bold"))

        # Засечки и числа на оси Y
        for y in range(y_min, y_max + 1):
            self.t.penup()
            self.t.goto(-5, y * self.scale)
            self.t.pendown()
            self.t.goto(5, y * self.scale)
            if y != 0:
                self.t.penup()
                self.t.goto(-20, y * self.scale - 7)
                self.t.write(str(y), align="right")

    def calculate_y(self, x):
        """Математическая логика кусочно-заданной функции"""
        if x <= -3:
            return 3
        elif -3 < x <= 3:
            return 3 - math.sqrt(max(0, 9 - x ** 2))
        elif 3 < x <= 6:
            return -2 * x + 9
        else:
            return x - 9

    def plot_function(self, start_x=-7.0, end_x=11, step=0.1):
        """Построение графика функции по точкам"""
        self.t.color("blue")
        self.t.pensize(2)
        self.t.penup()

        x = start_x
        first = True

        while x <= end_x:
            y = self.calculate_y(x)
            self.t.goto(x * self.scale, y * self.scale)

            if first:
                self.t.pendown()
                first = False

            x += step

    def run(self):
        """Запуск отрисовки координатной сетки, графика и удержание окна"""
        self.draw_system(-8, 12, -4, 5)  # Сетка с запасом для подписей
        self.plot_function()
        self.screen.mainloop()


# Точка входа в программу
if __name__ == "__main__":
    app = PiecewiseGrapher()
    app.run()

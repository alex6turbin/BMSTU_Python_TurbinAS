import tkinter as tk
from tkinter import messagebox
import math

class TaylorGraphApp:
    def __init__(self, root):
        """Инициализация главного окна и начальных параметров"""
        self.root = root
        self.root.title("Ввод параметров с клавиатуры")

        # Размер окна на 70% от ширины и 60% от высоты монитора
        sw, sh = root.winfo_screenwidth(), root.winfo_screenheight()
        self.max_x, self.max_y = int(sw * 0.7), int(sh * 0.6)

        # Конфигурация начальных математических границ
        self.x_min, self.x_max = -20.0, 5.0
        self.y_min, self.y_max = -5.0, 5.0
        self.eps = 0.0001
        self.b_val = 0.0

        self.entries = {}
        self.create_widgets()
        self.root.resizable(False, False)

    def y_taylor(self, x, eps):
        """Расчет функции через разложение в ряд Тейлора"""
        if x < -1.0:
            s, n, term = -math.pi / 2, 0, -1 / x
            while abs(term) > eps and n < 1000:
                s += term
                term *= -(2 * n + 1) / ((2 * n + 3) * (x ** 2))
                n += 1
            return s
        elif -1.0 <= x <= 1.0:
            s, n, term = 0, 0, x
            while abs(term) > eps and n < 1000:
                s += term
                term *= -(x ** 2 * (2 * n + 1)) / (2 * n + 3)
                n += 1
            return s
        else:
            s, n, term = math.pi / 2, 0, -1 / x
            while abs(term) > eps and n < 1000:
                s += term
                term *= -(2 * n + 1) / ((2 * n + 3) * (x ** 2))
                n += 1
            return s

    def z_analytic(self, x, b):
        """Аналитическое вычисление точного значения функции"""
        return math.atan(x) + b

    def create_widgets(self):
        """Создание элементов графического интерфейса"""
        # Холст для рисования графиков
        self.cv = tk.Canvas(self.root, width=self.max_x, height=self.max_y, bg="white")
        self.cv.grid(row=0, column=0, columnspan=10, padx=10, pady=10)

        # Список параметров для генерации полей ввода
        inputs = [
            ("Начало X:", "ent_xmin", self.x_min), ("Конец X:", "ent_xmax", self.x_max),
            ("Минимум Y:", "ent_ymin", self.y_min), ("Максимум Y:", "ent_ymax", self.y_max),
            ("Точность:", "ent_eps", self.eps), ("Параметр b:", "ent_b", self.b_val)
        ]

        for i, (label, name, default) in enumerate(inputs):
            row, col = (1 if i < 3 else 2), (i % 3) * 2
            tk.Label(self.root, text=label).grid(row=row, column=col, sticky='e')
            ent = tk.Entry(self.root, width=10)
            ent.insert(0, str(default))
            ent.grid(row=row, column=col + 1, padx=5, pady=5)
            self.entries[name] = ent

        # Кнопки управления
        tk.Button(self.root, text="Нарисовать", bg="lightgreen", command=self.draw, width=15).grid(row=1, column=8, padx=10)
        tk.Button(self.root, text="Выход", bg="#ff9999", command=self.root.quit, width=15).grid(row=2, column=8, padx=10)

    def get_screen_coords(self, x_math, y_math):
        """Трансформация математических координат в экранные пиксели"""
        padding = 50
        usable_x, usable_y = self.max_x - 2 * padding, self.max_y - 2 * padding
        px = padding + (x_math - self.x_min) * (usable_x / (self.x_max - self.x_min))
        py = (self.max_y - padding) - (y_math - self.y_min) * (usable_y / (self.y_max - self.y_min))
        return px, py

    def draw_axes(self):
        """Отрисовка координатной сетки, осей и разметки"""
        x0, y0 = self.get_screen_coords(0, 0)
        self.cv.create_line(0, y0, self.max_x, y0, fill="black", width=2, arrow=tk.LAST)
        self.cv.create_line(x0, self.max_y, x0, 0, fill="black", width=2, arrow=tk.LAST)

        self.cv.create_text(self.max_x - 15, y0 + 15, text="X", font=("Arial", 12, "bold"))
        self.cv.create_text(x0 - 15, 15, text="Y", font=("Arial", 12, "bold"))

        # Числовые метки оси X
        step_x = 2 if abs(self.x_max - self.x_min) > 10 else 1
        for x in range(int(self.x_min), int(self.x_max) + 1, step_x):
            px, py = self.get_screen_coords(x, 0)
            self.cv.create_line(px, y0 - 3, px, y0 + 3)
            if x != 0:
                self.cv.create_text(px, y0 + 15, text=str(x), font=("Arial", 8))

        # Числовые метки оси Y
        for y in range(int(self.y_min), int(self.y_max) + 1):
            px, py = self.get_screen_coords(0, y)
            self.cv.create_line(x0 - 3, py, x0 + 3, py)
            if y != 0:
                self.cv.create_text(x0 - 15, py, text=str(y), font=("Arial", 8))

    def draw(self):
        """Валидация данных, построение легенды и отрисовка графиков функций"""
        try:
            self.x_min = float(self.entries['ent_xmin'].get())
            self.x_max = float(self.entries['ent_xmax'].get())
            self.y_min = float(self.entries['ent_ymin'].get())
            self.y_max = float(self.entries['ent_ymax'].get())
            self.eps = float(self.entries['ent_eps'].get())
            self.b_val = float(self.entries['ent_b'].get())
        except ValueError:
            messagebox.showerror("Ошибка", "Пожалуйста, введите корректные числа в поля ввода.")
            return

        self.cv.delete("all")
        self.draw_axes()

        # Отрисовка интерактивной легенды графиков
        self.cv.create_rectangle(20, 20, 180, 70, fill="#f9f9f9", outline="gray")
        self.cv.create_line(30, 35, 60, 35, fill="blue", width=2)
        self.cv.create_text(70, 35, text="Ряд Тейлора", anchor="w")
        self.cv.create_line(30, 55, 60, 55, fill="red", width=2)
        self.cv.create_text(70, 55, text=f"Arctg+b (b={self.b_val})", anchor="w")

        pts_t, pts_a = [], []
        steps = 600
        dx = (self.x_max - self.x_min) / steps

        # Сбор точек графиков через вызов внутренних методов класса
        for i in range(steps + 1):
            cx = self.x_min + i * dx
            pts_t.append(self.get_screen_coords(cx, self.y_taylor(cx, self.eps)))
            pts_a.append(self.get_screen_coords(cx, self.z_analytic(cx, self.b_val)))

        # Вывод линий на Canvas
        self.cv.create_line(pts_t, fill="blue", width=2, smooth=True)
        self.cv.create_line(pts_a, fill="red", width=2, smooth=True)


if __name__ == "__main__":
    root = tk.Tk()
    app = TaylorGraphApp(root)
    root.mainloop()
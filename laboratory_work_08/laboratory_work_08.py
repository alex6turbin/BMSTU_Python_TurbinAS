import tkinter as tk
from tkinter import messagebox
import math


# --- МАТЕМАТИЧЕСКИЕ РАСЧЕТЫ ---

def y_taylor(x, eps):
    # Используем три сегмента ряда для непрерывности графика
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


def z_analytic(x, b):
    # Аналитическая функция: арктангенс плюс параметр b
    return math.atan(x) + b


# --- ГРАФИЧЕСКОЕ ПРИЛОЖЕНИЕ ---

class GraphApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ввод параметров с клавиатуры")

        # Размер окна на 70% от ширины и 60% от высоты монитора
        sw, sh = root.winfo_screenwidth(), root.winfo_screenheight()
        self.MaxX, self.MaxY = int(sw * 0.7), int(sh * 0.6)

        # Стандартные границы и настройки
        self.Xmin, self.Xmax = -20.0, 5.0
        self.Ymin, self.Ymax = -5.0, 5.0
        self.eps = 0.0001
        self.b_val = 0.0  # Значение b по умолчанию

        self.create_widgets()
        self.root.resizable(False, False)

    def create_widgets(self):
        # Белое поле (холст)
        self.cv = tk.Canvas(self.root, width=self.MaxX, height=self.MaxY, bg="white")
        self.cv.grid(row=0, column=0, columnspan=10, padx=10, pady=10)

        # Список полей ввода для параметров
        inputs = [
            ("Начало X:", "ent_xmin", self.Xmin), ("Конец X:", "ent_xmax", self.Xmax),
            ("Минимум Y:", "ent_ymin", self.Ymin), ("Максимум Y:", "ent_ymax", self.Ymax),
            ("Точность:", "ent_eps", self.eps), ("Параметр b:", "ent_b", self.b_val)
        ]

        self.entries = {}
        for i, (label, name, default) in enumerate(inputs):
            row, col = (1 if i < 3 else 2), (i % 3) * 2
            tk.Label(self.root, text=label).grid(row=row, column=col, sticky='e')
            ent = tk.Entry(self.root, width=10)
            ent.insert(0, str(default))
            ent.grid(row=row, column=col + 1, padx=5, pady=5)
            self.entries[name] = ent

        # Кнопки
        tk.Button(self.root, text="Нарисовать", bg="lightgreen", command=self.draw, width=15).grid(row=1, column=8,
                                                                                                   padx=10)
        tk.Button(self.root, text="Выход", bg="#ff9999", command=self.root.quit, width=15).grid(row=2, column=8,
                                                                                                padx=10)

    def get_screen_coords(self, x_math, y_math):
        # Пересчет математических координат в пиксели экрана
        padding = 50
        usable_x, usable_y = self.MaxX - 2 * padding, self.MaxY - 2 * padding
        px = padding + (x_math - self.Xmin) * (usable_x / (self.Xmax - self.Xmin))
        py = (self.MaxY - padding) - (y_math - self.Ymin) * (usable_y / (self.Ymax - self.Ymin))
        return px, py

    def draw_axes(self):
        # Рисование осей со стрелками
        x0, y0 = self.get_screen_coords(0, 0)
        self.cv.create_line(0, y0, self.MaxX, y0, fill="black", width=2, arrow=tk.LAST)
        self.cv.create_line(x0, self.MaxY, x0, 0, fill="black", width=2, arrow=tk.LAST)

        self.cv.create_text(self.MaxX - 15, y0 + 15, text="X", font=("Arial", 12, "bold"))
        self.cv.create_text(x0 - 15, 15, text="Y", font=("Arial", 12, "bold"))

        # Числовая разметка по X
        step_x = 2 if abs(self.Xmax - self.Xmin) > 10 else 1
        for x in range(int(self.Xmin), int(self.Xmax) + 1, step_x):
            px, py = self.get_screen_coords(x, 0)
            self.cv.create_line(px, y0 - 3, px, y0 + 3)
            if x != 0:
                self.cv.create_text(px, y0 + 15, text=str(x), font=("Arial", 8))

        # Числовая разметка по Y
        for y in range(int(self.Ymin), int(self.Ymax) + 1):
            px, py = self.get_screen_coords(0, y)
            self.cv.create_line(x0 - 3, py, x0 + 3, py)
            if y != 0:
                self.cv.create_text(x0 - 15, py, text=str(y), font=("Arial", 8))

    def draw(self):
        try:
            # Чтение всех данных из полей ввода, включая параметр b
            self.Xmin = float(self.entries['ent_xmin'].get())
            self.Xmax = float(self.entries['ent_xmax'].get())
            self.Ymin = float(self.entries['ent_ymin'].get())
            self.Ymax = float(self.entries['ent_ymax'].get())
            self.eps = float(self.entries['ent_eps'].get())
            self.b_val = float(self.entries['ent_b'].get())
        except ValueError:
            messagebox.showerror("Ошибка", "Пожалуйста, введите корректные числа в поля ввода.")
            return

        self.cv.delete("all")
        self.draw_axes()

        # Легенда графиков
        self.cv.create_rectangle(20, 20, 180, 70, fill="#f9f9f9", outline="gray")
        self.cv.create_line(30, 35, 60, 35, fill="blue", width=2)
        self.cv.create_text(70, 35, text="Ряд Тейлора", anchor="w")
        self.cv.create_line(30, 55, 60, 55, fill="red", width=2)
        self.cv.create_text(70, 55, text=f"Arctg+b (b={self.b_val})", anchor="w")

        pts_t, pts_a = [], []
        steps = 600
        dx = (self.Xmax - self.Xmin) / steps

        for i in range(steps + 1):
            cx = self.Xmin + i * dx
            pts_t.append(self.get_screen_coords(cx, y_taylor(cx, self.eps)))
            pts_a.append(self.get_screen_coords(cx, z_analytic(cx, self.b_val)))

        # Отрисовка непрерывных линий
        self.cv.create_line(pts_t, fill="blue", width=2, smooth=True)
        self.cv.create_line(pts_a, fill="red", width=2, smooth=True)


if __name__ == "__main__":
    root = tk.Tk()
    app = GraphApp(root)
    root.mainloop()
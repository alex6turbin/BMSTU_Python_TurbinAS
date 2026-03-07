try:
    r = float(input("Введите положительный параметр R: "))
    if r <= 0:
        print("Ошибка: R должен быть больше нуля!")
    else:
        x = float(input("Введите X: "))
        y = float(input("Введите Y: "))

        in_circle = (x + r) ** 2 + (y - r) ** 2 <= r ** 2
        in_rectangle = (0 <= x <= 2 * r) and (-r <= y <= 0)

        if in_circle or in_rectangle:
            print("Точка внутри")
        else:
            print("Точка снаружи")

except ValueError:
    print("Ошибка: введите числовые значения!")
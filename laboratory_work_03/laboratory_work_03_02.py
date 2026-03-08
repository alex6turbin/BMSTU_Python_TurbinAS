import random

# Ввод R с проверкой на положительное значение
while True:
    try:
        r = float(input("Введите положительный параметр R: "))
        if r > 0:
            break
        print("Ошибка: R не может быть отрицательным или равным нулю.")
    except ValueError:
        print("Ошибка: введите числовое значение.")

print("\nРезультаты десяти выстрелов по мишени:")
print("+----------+----------+-----------+")
print("|    X     |    Y     | Попадание |")
print("+----------+----------+-----------+")

for i in range(10):
    # Генерируем X от -2R, чтобы охватить всю левую часть круга
    x = random.uniform(-2 * r, 2 * r)
    y = random.uniform(-r, r)

    in_circle = (x + r) ** 2 + (y - r) ** 2 <= r ** 2
    in_rectangle = (0 <= x <= 2 * r) and (-r <= y <= 0)

    res = "Yes" if (in_circle or in_rectangle) else "No"

    print("| {0:8.2f} | {1:8.2f} | {2:9} |".format(x, y, res))

print("+----------+----------+-----------+")
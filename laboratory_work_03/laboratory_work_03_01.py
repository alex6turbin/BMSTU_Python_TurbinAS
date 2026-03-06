from math import sqrt

# 1. Ввод значений переменных
xb = float(input("Введите X начальное (-7): "))
xe = float(input("Введите X конечное (11): "))
dx = float(input("Введите шаг dx: "))

# Открываем файл для записи результатов
with open("results.txt", "w", encoding="utf-8") as file:
    # Заголовок и шапка таблицы
    header = "+----------+----------+"
    title = "|    X     |    Y     |"

    print("\nТаблица значений функции:")
    print(header)
    print(title)
    print(header)

    file.write("Таблица значений функции:\n")
    file.write(header + "\n" + title + "\n" + header + "\n")

    # 2. Инициализация текущего значения X
    xt = xb

    # 3. Цикл расчета (пока xt не достигнет xe)
    while xt <= xe + dx / 1000:

        if xt <= -3:
            y = 3
        elif -3 < xt <= 3:
            # Защита от отрицательного значения под корнем (погрешность float)
            y = 3 - sqrt(max(0, 9 - xt ** 2))
        elif 3 < xt <= 6:
            y = -2 * xt + 9
        elif 6 < xt <= 11:
            y = xt - 9
        else:
            y = 2  # Конец графика на отметке y=2 при x=11

        # Формирование и вывод строки
        row = "| {0:8.2f} | {1:8.2f} |".format(xt, y)
        print(row)
        file.write(row + "\n")

        # Шаг аргумента
        xt += dx

    # Завершение таблицы
    print(header)
    file.write(header + "\n")

print("\nДанные успешно сохранены в файл 'results.txt'")
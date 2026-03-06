from math import sqrt, pi, sin, cos


def main():
    try:
        # --- 1. ЧТЕНИЕ ДАННЫХ ИЗ ФАЙЛА ---
        with open("input1.txt", "r") as f_in:
            data = f_in.read().split()
            if len(data) < 3:
                print("Ошибка: в файле должно быть 3 числа (начало, конец, шаг).")
                return

            ab = float(data[0])  # Alpha начальное
            ae = float(data[1])  # Alpha конечное
            da = float(data[2])  # Шаг dAlpha

        # --- 2. ПОДГОТОВКА И ВЫВОД В ФАЙЛ ---
        with open("output1.txt", "w", encoding="utf-8") as f_out:
            header = "+---------+----------+----------+----------+\n"
            title = "|  Alpha  |    Z1    |    Z2    | Разность |\n"

            f_out.write("Результаты сравнения выражений Z1 и Z2:\n")
            f_out.write(header + title + header)

            at = ab
            # Цикл вычислений (с поправкой на точность float)
            while at <= ae + da / 1000:
                # Вычисление z1
                term1 = cos(3 * pi / 8 - at / 4) ** 2
                term2 = cos(11 * pi / 8 + at / 4) ** 2
                z1 = term1 - term2

                # Вычисление z2
                z2 = (sqrt(2) / 2) * sin(at / 2)

                # Дополнительно считаем разность для проверки точности
                diff = abs(z1 - z2)

                # Формирование строки таблицы
                row = "| {0:7.2f} | {1:8.4f} | {2:8.4f} | {3:8.1e} |\n".format(at, z1, z2, diff)
                f_out.write(row)

                at += da

            f_out.write(header)

        print("Расчет окончен. Результаты сохранены в файл 'output1.txt'.")

    except FileNotFoundError:
        print("Ошибка: Файл 'input1.txt' не найден!")
    except ValueError:
        print("Ошибка: В файле 'input1.txt' должны быть только числа!")


if __name__ == "__main__":
    main()

import sys
import os

# 1. Получаем путь к папке laboratory_work_06 (где лежит этот файл)
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Поднимаемся на уровень выше в главную папку BMSTU_Python_TurbinAS
project_root = os.path.dirname(current_dir)

# 3. Формируем путь к папке с первой лабораторной
lab01_path = os.path.join(project_root, "laboratory_work_01")

# 4. Добавляем этот путь в систему поиска модулей Python
if lab01_path not in sys.path:
    sys.path.insert(0, lab01_path)

# 5. Импортируем функции (название файла указываем без .py)
try:
    from laboratory_work_01_02 import function_1, function_2
    print("Функции успешно импортированы!")
except ImportError as e:
    print(f"Ошибка импорта: {e}")
    sys.exit(1)


def main():
    try:
        with open("input1.txt", "r") as f_in:
            data = f_in.read().split()
            if len(data) < 3:
                print("Ошибка: нужно 3 числа.")
                return
            ab, ae, da = map(float, data)

        with open("output1.txt", "w", encoding="utf-8") as f_out:
            header = "+---------+----------+----------+----------+\n"
            title  = "|  Alpha  |    Z1    |    Z2    | Разность |\n"
            f_out.write("Результаты импортированных функций:\n")
            f_out.write(header + title + header)

            at = ab
            while at <= ae + da / 1000:
                # Используем импортированные функции
                z1 = function_1(at)
                z2 = function_2(at)
                diff = abs(z1 - z2)

                row = "| {0:7.2f} | {1:8.4f} | {2:8.4f} | {3:8.1e} |\n".format(at, z1, z2, diff)
                f_out.write(row)
                at += da

            f_out.write(header)
        print("Расчет окончен. Использованы функции из calculations.py")

    except FileNotFoundError:
        print("Ошибка: Файл 'input1.txt' или 'calculations.py' не найден!")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()
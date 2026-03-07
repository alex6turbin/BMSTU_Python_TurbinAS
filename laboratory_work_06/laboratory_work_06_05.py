import random
import os
import sys

# --- Настройка путей для импорта из соседней папки ---
current_dir = os.path.dirname(os.path.abspath(__file__))  # папка lab_06
project_root = os.path.dirname(current_dir)  # корень BMSTU_Python...
lab05_path = os.path.join(project_root, "laboratory_work_05")

if lab05_path not in sys.path:
    sys.path.insert(0, lab05_path)

# --- Импорт функций из ПЕРВОЙ программы ---
try:
    from laboratory_work_05 import find_matching_elements_k, sum_rows_with_negatives
except ImportError:
    print("Ошибка: Не удалось найти файл laboratory_work_05.py")
    sys.exit()


def create_matrix(rows, cols):
    """Генерация матрицы случайными числами"""
    return [[random.randint(-10, 10) for _ in range(cols)] for _ in range(rows)]


# Функции find_symmetric_k и process_negative_rows удалены,
# так как теперь используются импортированные аналоги.

def main():
    if not os.path.exists("input5.txt"):
        print("Ошибка: Создайте файл input5.txt с размерами матрицы!")
        return

    try:
        # --- ЧТЕНИЕ ИЗ ФАЙЛА ---
        with open("input5.txt", "r") as f_in:
            data = f_in.read().split()
            if len(data) < 2:
                print("Ошибка: В файле должно быть 2 числа (строки и столбцы)!")
                return
            r, c = int(data[0]), int(data[1])

        # Генерируем матрицу
        matrix = create_matrix(r, c)

        # --- ЗАПИСЬ В ФАЙЛ ---
        with open("output5.txt", "w", encoding="utf-8") as f_out:
            f_out.write("Исходная матрица:\n")
            for row in matrix:
                f_out.write(" ".join(f"{elem:4}" for elem in row) + "\n")

            # --- Использование импортированных функций ---

            # Задача №1 (вызываем импортированную find_matching_elements_k)
            k_indices = find_matching_elements_k(matrix)
            f_out.write("\n--- Результаты задачи №1 ---\n")
            if k_indices:
                f_out.write(f"Строки, совпадающие со столбцами (k): {k_indices}\n")
            else:
                f_out.write("Совпадений строк и столбцов не обнаружено.\n")

            # Задача №2 (вызываем импортированную sum_rows_with_negatives)
            neg_results = sum_rows_with_negatives(matrix)
            f_out.write("\n--- Результаты задачи №2 ---\n")
            if neg_results:
                f_out.write("Суммы в строках с отрицательными числами:\n")
                for row_num, row_sum in neg_results:
                    f_out.write(f"Строка №{row_num}: сумма = {row_sum}\n")
            else:
                f_out.write("Строк с отрицательными элементами не найдено.\n")

        print("Готово! Использованы функции из laboratory_work_05. Результаты в 'output5.txt'.")

    except ValueError:
        print("Ошибка: В файле input5.txt должны быть только целые числа!")
    except Exception as e:
        print(f"Непредвиденная ошибка: {e}")


if __name__ == "__main__":
    main()
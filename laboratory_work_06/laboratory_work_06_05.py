import random
import os

def create_matrix(rows, cols):
    """Генерация матрицы случайными числами"""
    return [[random.randint(-10, 10) for _ in range(cols)] for _ in range(rows)]

def find_symmetric_k(matrix):
    """Задача 1: Поиск k, где k-я строка совпадает с k-м столбцом"""
    matches = []
    size = min(len(matrix), len(matrix[0]))
    for k in range(size):
        row_k = matrix[k]
        col_k = [matrix[i][k] for i in range(len(matrix))]
        if row_k == col_k:
            matches.append(k + 1)
    return matches

def process_negative_rows(matrix):
    """Задача 2: Суммы для каждой строки с отрицательным элементом"""
    results = []
    for i, row in enumerate(matrix):
        if any(x < 0 for x in row):
            results.append((i + 1, sum(row)))
    return results

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
            # 1. Записываем исходную матрицу
            f_out.write("Исходная матрица:\n")
            for row in matrix:
                f_out.write(" ".join(f"{elem:4}" for elem in row) + "\n")

            # 2. Результаты задачи №1
            k_indices = find_symmetric_k(matrix)
            f_out.write("\n--- Результаты задачи №1 ---\n")
            if k_indices:
                f_out.write(f"Строки, совпадающие со столбцами (k): {k_indices}\n")
            else:
                f_out.write("Совпадений строк и столбцов не обнаружено.\n")

            # 3. Результаты задачи №2
            neg_results = process_negative_rows(matrix)
            f_out.write("\n--- Результаты задачи №2 ---\n")
            if neg_results:
                f_out.write("Суммы в строках с отрицательными числами:\n")
                for row_num, row_sum in neg_results:
                    f_out.write(f"Строка №{row_num}: сумма = {row_sum}\n")
            else:
                f_out.write("Строк с отрицательными элементами не найдено.\n")

        print("Готово! Матрица обработана, результаты в файле 'output5.txt'.")

    except ValueError:
        print("Ошибка: В файле input5.txt должны быть только целые числа!")

if __name__ == "__main__":
    main()
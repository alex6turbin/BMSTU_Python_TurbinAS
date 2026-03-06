import random


def create_matrix(rows, cols):
    """Функция генерации матрицы случайными числами"""
    # Локальная переменная matrix
    matrix = [[random.randint(-10, 10) for _ in range(cols)] for _ in range(rows)]
    return matrix


def print_matrix(matrix):
    """Функция вывода исходной матрицы"""
    print("\nИсходная матрица:")
    for row in matrix:
        print(" ".join(f"{elem:4}" for elem in row))


def find_symmetric_k(matrix):
    """Задача 1: Поиск k, где k-я строка совпадает с k-м столбцом"""
    matches = []
    # k ограничено минимальной из размерностей
    size = min(len(matrix), len(matrix[0]))

    for k in range(size):
        row_k = matrix[k]
        col_k = [matrix[i][k] for i in range(len(matrix))]

        if row_k == col_k:
            matches.append(k + 1)
    return matches


def process_negative_rows(matrix):
    """Задача 2: Вычисление сумм для каждой строки с отрицательным элементом"""
    results = []  # Список кортежей (номер_строки, сумма)

    for i, row in enumerate(matrix):
        # Локальная проверка наличия отрицательного числа
        has_negative = False
        for x in row:
            if x < 0:
                has_negative = True
                break

        if has_negative:
            row_sum = sum(row)
            results.append((i + 1, row_sum))

    return results


def main():
    """Основная функция управления программой"""
    # 1. Запрос размерностей
    try:
        r = int(input("Введите количество строк: "))
        c = int(input("Введите количество столбцов: "))
        if r <= 0 or c <= 0:
            print("Ошибка: размеры должны быть больше нуля.")
            return
    except ValueError:
        print("Ошибка: введите целое число.")
        return

    # 2. Создание и отображение массива
    matrix = create_matrix(r, c)
    print_matrix(matrix)

    # 3. Выполнение первой задачи
    k_indices = find_symmetric_k(matrix)
    print("\n--- Результаты задачи №1 ---")
    if k_indices:
        print(f"Строки, совпадающие со столбцами (k): {k_indices}")
    else:
        print("Совпадений строк и столбцов не обнаружено.")

    # 4. Выполнение второй задачи
    neg_results = process_negative_rows(matrix)
    print("\n--- Результаты задачи №2 ---")
    if neg_results:
        print("Суммы элементов в строках с отрицательными числами:")
        for row_num, row_sum in neg_results:
            print(f"Строка №{row_num}: сумма элементов = {row_sum}")
    else:
        print("Строк с отрицательными элементами не найдено.")


if __name__ == "__main__":
    main()
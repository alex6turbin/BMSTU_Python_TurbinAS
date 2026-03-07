import random


def create_matrix(size=8):
    """Генерация случайной матрицы 8x8"""
    return [[random.randint(-5, 10) for _ in range(size)] for _ in range(size)]


def create_matrix_manual(size=8):
    """Ручной ввод матрицы 8x8"""
    matrix = []
    print(f"\nВведите элементы матрицы {size}x{size}:")
    for i in range(size):
        while True:
            try:
                line = input(f"Строка {i + 1} (8 чисел через пробел): ").split()
                if len(line) != size:
                    print(f"Нужно ввести ровно {size} чисел!")
                    continue
                matrix.append([int(x) for x in line])
                break
            except ValueError:
                print("Ошибка! Вводите только целые числа.")
    return matrix


def print_matrix(matrix):
    print("\nТекущая матрица:")
    for row in matrix:
        print(" ".join(f"{elem:4}" for elem in row))


def find_matching_elements_k(matrix):
    """
    Задача 1: Поиск k, где k-я строка и k-й столбец состоят из одинаковых элементов.
    Порядок элементов не важен (сравнение через сортировку).
    """
    matches = []
    size = len(matrix)

    for k in range(size):
        row_k = matrix[k]
        col_k = [matrix[i][k] for i in range(size)]

        # Сравниваем отсортированные списки (состав элементов)
        if sorted(row_k) == sorted(col_k):
            matches.append(k + 1)
    return matches


def sum_rows_with_negatives(matrix):
    """
    Задача 2: Сумма элементов в строках, содержащих хотя бы один отрицательный элемент.
    """
    results = []
    for i, row in enumerate(matrix):
        if any(x < 0 for x in row):
            results.append((i + 1, sum(row)))
    return results


def main():
    size = 8
    print(f"Программа для работы с матрицей {size}x{size}")

    choice = input("Заполнить случайными числами? (y - да, n - вручную): ").lower()
    if choice == 'y':
        matrix = create_matrix(size)
    else:
        matrix = create_matrix_manual(size)

    print_matrix(matrix)

    # Решение задачи №1
    k_list = find_matching_elements_k(matrix)
    print("\n--- Задача №1 ---")
    if k_list:
        print(f"Индексы k, где составы строки и столбца совпадают: {k_list}")
    else:
        print("Строк и столбцов с одинаковым набором элементов не найдено.")

    # Решение задачи №2
    neg_sums = sum_rows_with_negatives(matrix)
    print("\n--- Задача №2 ---")
    if neg_sums:
        print("Суммы в строках с отрицательными элементами:")
        for num, s in neg_sums:
            print(f"Строка №{num}: сумма = {s}")
    else:
        print("Строк с отрицательными элементами нет.")


if __name__ == "__main__":
    main()
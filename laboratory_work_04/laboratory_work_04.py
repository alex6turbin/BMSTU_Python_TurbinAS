import random

# 1. Ввод массива
try:
    n = int(input("Введите количество элементов n: "))
    arr = []

    choice = input("Заполнить массив случайными числами? (y/n): ").lower()

    if choice == 'y':
        # Генерируем случайные числа от -10 до 10 (можно изменить диапазон)
        # Округляем до 1 знака для удобства проверки нулей
        arr = [round(random.uniform(-5, 5), 1) for _ in range(n)]
        # Чтобы в массиве гарантированно могли появиться нули для задачи 2:
        arr = [random.choice([0.0, round(random.uniform(-5, 5), 1)]) for _ in range(n)]
    else:
        print(f"Введите {n} вещественных чисел:")
        for i in range(n):
            arr.append(float(input(f"Элемент {i + 1}: ")))

except ValueError:
    print("Ошибка! Нужно вводить вещественные числа.")
    exit()

print("\nИсходный массив:", arr)

# --- Задача 1: Номер максимального элемента ---
max_val = max(arr)
max_index = arr.index(max_val) + 1  # +1 для порядкового номера (не индекса)
print(f"1. Порядковый номер максимального элемента ({max_val}): {max_index}")

# --- Задача 2: Произведение между первым и вторым нулями ---
zero_indices = [i for i, val in enumerate(arr) if val == 0]

if len(zero_indices) >= 2:
    start = zero_indices[0] + 1
    end = zero_indices[1]

    # Если между нулями есть элементы
    if start < end:
        product = 1
        for i in range(start, end):
            product *= arr[i]
        print(f"2. Произведение элементов между 0 и 0: {product}")
    else:
        print("2. Между первым и вторым нулями нет элементов.")
else:
    print("2. В массиве меньше двух нулей, произведение вычислить нельзя.")

# --- Задача 3: Преобразование массива (нечетные/четные позиции) ---
odd_positions = arr[0::2]  # С первого элемента через один (1-я, 3-я...)
even_positions = arr[1::2]  # Со второго элемента через один (2-я, 4-я...)

transformed_arr = odd_positions + even_positions
print("3. Преобразованный массив:", transformed_arr)
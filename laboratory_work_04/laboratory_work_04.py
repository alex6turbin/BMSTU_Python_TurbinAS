import random

# --- Функции для импорта ---

def get_max_element_info(array):
    """Задача 1: Максимальный элемент и его номер (индекс + 1)."""
    if not array: return None, None
    max_val = max(array)
    return max_val, array.index(max_val) + 1


def get_product_between_zeros(array):
    """Задача 2: Произведение между первой парой нулей, имеющей элементы между собой."""
    zero_indices = [i for i, val in enumerate(array) if val == 0]

    if not zero_indices:
        return "В массиве нет нулей"
    if len(zero_indices) < 2:
        return "В массиве только один ноль"

    # Ищем первый подходящий интервал
    for k in range(len(zero_indices) - 1):
        start = zero_indices[k] + 1
        end = zero_indices[k + 1]

        if start < end:  # Если между индексами есть элементы
            product = 1
            for i in range(start, end):
                product *= array[i]
            return product

    return "Нет элементов между нулями (все нули стоят рядом)"


def transform_array(array):
    """Задача 3: Сначала нечетные позиции, потом четные."""
    return array[0::2] + array[1::2]


# --- Исполняемый код (не сработает при импорте) ---
if __name__ == "__main__":
    n = int(input("Введите n: "))
    arr = [random.randint(-5, 5) for _ in range(n)]
    print(f"Массив: {arr}")
    print(f"Макс: {get_max_element_info(arr)}")
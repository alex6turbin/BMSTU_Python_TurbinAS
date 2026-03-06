import os


def main():
    try:
        # --- 1. ЧТЕНИЕ ДАННЫХ ИЗ ФАЙЛА ---
        if not os.path.exists("input4.txt"):
            print("Ошибка: Файл 'input4.txt' не найден!")
            return

        with open("input4.txt", "r") as f_in:
            # Считываем все данные и преобразуем в список вещественных чисел
            data = f_in.read().split()
            if not data:
                print("Ошибка: Файл пуст!")
                return

            n = int(data[0])  # Первое число — количество элементов
            arr = [float(x) for x in data[1:n + 1]]  # Остальные — элементы массива

        # --- 2. ВЫПОЛНЕНИЕ ЗАДАЧ ---
        results = []  # Список для хранения строк вывода
        results.append(f"Исходный массив: {arr}")

        # Задача 1: Номер максимального элемента
        max_val = max(arr)
        max_index = arr.index(max_val) + 1
        results.append(f"1. Порядковый номер максимального элемента ({max_val}): {max_index}")

        # Задача 2: Произведение между первым и вторым нулями
        zero_indices = [i for i, val in enumerate(arr) if val == 0]
        if len(zero_indices) >= 2:
            start, end = zero_indices[0] + 1, zero_indices[1]
            if start < end:
                product = 1.0
                for i in range(start, end):
                    product *= arr[i]
                results.append(f"2. Произведение элементов между первым и вторым нулями: {product}")
            else:
                results.append("2. Между первым и вторым нулями нет элементов.")
        else:
            results.append("2. В массиве меньше двух нулей, произведение вычислить нельзя.")

        # Задача 3: Преобразование массива
        transformed_arr = arr[0::2] + arr[1::2]
        results.append(f"3. Преобразованный массив: {transformed_arr}")

        # --- 3. ЗАПИСЬ РЕЗУЛЬТАТОВ В ФАЙЛ ---
        with open("output4.txt", "w", encoding="utf-8") as f_out:
            for line in results:
                f_out.write(line + "\n")

        print("Обработка завершена. Результаты сохранены в 'output4.txt'.")

    except ValueError:
        print("Ошибка: Некорректные данные в файле (ожидались числа)!")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
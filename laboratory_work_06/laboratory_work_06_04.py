import sys
import os

# 1. Настройка путей для импорта
current_dir = os.path.dirname(os.path.abspath(__file__)) # папка lab_06
project_root = os.path.dirname(current_dir)              # корень проекта
lab04_path = os.path.join(project_root, "laboratory_work_04")

if lab04_path not in sys.path:
    sys.path.insert(0, lab04_path)

# 2. Импорт функций
try:
    from laboratory_work_04 import get_max_element_info, get_product_between_zeros, transform_array
except ImportError:
    print("Ошибка: Не удалось найти файл laboratory_work_04.py")
    sys.exit()

def main():
    try:
        # Чтение данных из файла (как в вашей первой программе)
        input_file = "input4.txt" # Убедитесь, что файл лежит в папке lab_06
        if not os.path.exists(input_file):
            print(f"Файл {input_file} не найден!")
            return

        with open(input_file, "r") as f_in:
            data = f_in.read().split()
            if not data: return
            n = int(data[0])
            arr = [int(x) for x in data[1:n+1]]

        # ИСПОЛЬЗОВАНИЕ ИМПОРТИРОВАННЫХ ФУНКЦИЙ
        max_val, max_idx = get_max_element_info(arr)
        product = get_product_between_zeros(arr)
        new_arr = transform_array(arr)

        # Запись результатов
        with open("output4.txt", "w", encoding="utf-8") as f_out:
            f_out.write(f"Исходный массив: {arr}\n")
            f_out.write(f"1. Макс: {max_val} (№ {max_idx})\n")
            f_out.write(f"2. Произведение между нулями: {product}\n")
            f_out.write(f"3. Трансформированный массив: {new_arr}\n")

        print("Расчет завершен. Результаты в output4.txt")

    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
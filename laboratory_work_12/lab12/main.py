# main_package.py

print("--- Начало демонстрации импортов ---\n")

# 1. ИМПОРТ МОДУЛЯ ИЗ ПАКЕТА
# Мы импортируем весь модуль math_utils из папки my_package
import package.math
# Обращаемся через полную цепочку имен: пакет.модуль.функция
print("1. Импорт модуля из пакета:")
print(f"Результат сложения: {package.math.add_numbers(10, 5)}")


# 2. ИМПОРТ ОПРЕДЕЛЕННЫХ ЭЛЕМЕНТОВ ИЗ МОДУЛЯ В ПАКЕТЕ
# Импортируем только нужную функцию, чтобы не писать длинные пути
from package.strings import greet_user
print("\n2. Импорт определенных элементов:")
print(greet_user("Алексей"))


# 3. ИМПОРТ ИЗ ПОДПАКЕТА
# Импортируем функцию из вложенной папки (sub_package)
from package.sub_package.formatter import format_bold
print("\n3. Импорт из подпакета:")
print(format_bold("это сообщение отформатировано в подпакете"))


# 4. ИМПОРТ ВСЕХ ЭЛЕМЕНТОВ (с учетом __all__)
# Здесь импортируются только те функции, которые вы указали в __all__ внутри модуля
from package.math import *
print("\n4. Импорт всех элементов (через *):")
print(f"Результат умножения: {multiply_numbers(4, 5)}")
# Попробуем вызвать DEFAULT_VALUE (которой нет в __all__ модуля math)
try:
    print(DEFAULT_VALUE)
except NameError:
    print("Переменная DEFAULT_VALUE не импортирована, так как ее нет в __all__")


# ПРОВЕРКА ОТНОСИТЕЛЬНОГО ИМПОРТА
# Функция complex_task внутри модуля strings использует относительный импорт
# (from .math import add_numbers)
from package.strings import complex_task
print("\n5. Проверка работы относительного импорта внутри пакета:")
print(complex_task(100, 200))

print("\n--- Демонстрация завершена ---")
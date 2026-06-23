# Константа
DEFAULT_VALUE = 0

# Список имен, доступных при "from math_utils import *"
__all__ = ['add_numbers', 'multiply_numbers']

def add_numbers(a, b):
    return a + b

def multiply_numbers(a, b):
    return a * b

def _secret_function():
    return "Эту функцию не видно через импорт *"

if __name__ == "__main__":
    print(f"Модуль {__name__} запущен напрямую.")
    print("Тест сложения (5+5):", add_numbers(5, 5))
else:
    print(f"Модуль {__name__} импортирован.")
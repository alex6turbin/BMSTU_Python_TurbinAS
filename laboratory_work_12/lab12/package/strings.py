# Относительный импорт из соседнего модуля того же пакета
from .math import add_numbers

__all__ = ['greet_user', 'complex_task']

def greet_user(name):
    return f"Привет, {name}!"

def complex_task(a, b):
    res = add_numbers(a, b)
    return f"Результат вычислений внутри строк: {res}"

if __name__ == "__main__":
    # ВАЖНО: Прямой запуск этого файла выдаст ошибку из-за относительного импорта.
    # Относительные импорты работают только при запуске через главный файл (main).
    print(f"Модуль {__name__} запущен напрямую.")
else:
    print(f"Модуль {__name__} импортирован.")
"""
Модуль с математическими функиями
"""

# import

__all__ = ['add', 'multiply']

# Константы
_PI = 3.14159

# Функции
def add(a, b):
    return a + b

def _subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def _divide(a, b):
    if b == 0:
        raise ValueError('Делить на ноль нельзя')
    else:
        return a / b


if __name__ == '__main__':
    print(add(5, 10))
    print(_subtract(5, 10))
    print(multiply(2, 3))
    print(_divide(2, 3))
    print(_PI)
else:
    print("Модуль импортирован.")


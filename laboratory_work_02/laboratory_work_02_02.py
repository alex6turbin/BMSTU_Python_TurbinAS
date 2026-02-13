from math import sqrt

def main():
    radius = float(input("Введите значение для радиуса R: "))
    x = float(input("Введите значение для переменной X: "))
    y = float(input("Введите значение для переменной Y: "))

    if (-radius <= x <= 0 and 0 <= y <= sqrt(radius ** 2 - x ** 2)):
        print("Точка внутри")
    elif (0 <= x <= radius / 2 and -2 * x + radius <= y <= 0):
        print("Точка внутри")
    elif (radius / 2 <= x <= radius and 2 * x - 2 * radius <= y <= 0):
        print("Точка внутри")
    else:
        print("Точка снаружи")


if __name__ == "__main__":
    main()
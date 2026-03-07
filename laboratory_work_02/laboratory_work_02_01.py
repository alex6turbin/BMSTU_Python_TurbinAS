from math import sqrt


x = float(input("Введите значение для x: "))
y = 0.0

if -7 <= x <= -3:
    y = 3
    print("X = {0:.2f} Y = {1:.2f}".format(x, y))
elif -3 < x <= 3:
    y = 3 - sqrt(9 - x ** 2)
    print("X = {0:.2f} Y = {1:.2f}".format(x, y))
elif 3 < x <= 6:
    y = -2 * x + 9
    print("X = {0:.2f} Y = {1:.2f}".format(x, y))
elif 6 < x <= 11:
    y = x - 9
    print("X = {0:.2f} Y = {1:.2f}".format(x, y))
else:
    print("Функция не определена в данном диапазоне")
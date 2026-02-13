from math import sqrt, pi, sin, cos

alpha = float(input("Введите значение для alpha: "))# Поменял название переменной х на alpha

z1 = cos(alpha) + sin(alpha) + cos(3 * alpha) + sin(3 * alpha)# Поменял название переменных y1 и y2 на z1 и z2
z2 = 2 * sqrt(2) * cos(alpha) * sin((pi / 4) + 2 * alpha)

print("I    Alpha     Z     I")# Поменял вывод функции print под условие задачи
print("I{0: 7.2f}  {1: 7.2f}    I".format(alpha, z1))
print("I{0: 7.2f}  {1: 7.2f}    I".format(alpha, z2))

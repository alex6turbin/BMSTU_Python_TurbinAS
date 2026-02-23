from math import sqrt, pi, sin, cos

alpha = float(input("Введите значение для alpha: "))

z1 = cos(alpha) + sin(alpha) + cos(3 * alpha) + sin(3 * alpha)
z2 = 2 * sqrt(2) * cos(alpha) * sin((pi / 4) + 2 * alpha)

print("I    Alpha     Z     I")
print("I{0: 7.2f}  {1: 7.2f}    I".format(alpha, z1))
print("I{0: 7.2f}  {1: 7.2f}    I".format(alpha, z2))

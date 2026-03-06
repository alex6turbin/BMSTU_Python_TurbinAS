from math import sqrt, pi, sin, cos


alpha = float(input("Введите значение для alpha: "))

# Вычисление z1
term1 = cos(3 * pi / 8 - alpha / 4) ** 2
term2 = cos(11 * pi / 8 + alpha / 4) ** 2
z1 = term1 - term2

# Вычисление z2
z2 = (sqrt(2) / 2) * sin(alpha / 2)

print("   Alpha       Z        ")
print(" {0: 7.2f}  {1: 7.2f}     ".format(alpha, z1))
print(" {0: 7.2f}  {1: 7.2f}     ".format(alpha, z2))



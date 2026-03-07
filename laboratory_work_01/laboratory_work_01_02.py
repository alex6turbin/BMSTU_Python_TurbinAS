from math import sqrt, pi, sin, cos


alpha = float(input("Введите значение для alpha: "))

# Вычисление z1
def function_1(alpha):
    term1 = cos(3 * pi / 8 - alpha / 4) ** 2
    term2 = cos(11 * pi / 8 + alpha / 4) ** 2
    return term1 - term2

# Вычисление z2
def function_2(alpha):
    return (sqrt(2) / 2) * sin(alpha / 2)

if __name__ == "__main__":
    alpha = float(input("Введите значение для alpha: "))
    print("   Alpha       Z        ")
    print(" {0: 7.2f}  {1: 7.2f}     ".format(alpha, function_1(alpha)))
    print(" {0: 7.2f}  {1: 7.2f}     ".format(alpha, function_2(alpha)))


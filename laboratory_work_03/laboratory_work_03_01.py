from math import sqrt

print("Введите Xbeg, Xend и dx")
xb = float(input("Введите Xначальное: "))
xe = float(input("Введите Xконечное: "))
dx = float(input("Введите шаг dx: "))

y = 0.0

xt = xb
print("I    X   I    Y   I")
print("+--------+--------+")
while xt <= xe:
    if xt <= -8:
        y = -3
    elif -8 < xt < -3:
        y = (1 / 4) * xt + 3 / 4
    elif -3 <= xt < 3:
        y = -sqrt(9 - xt ** 2)
    elif 3 <= xt < 5:
        y = xt - 3
    else:
        y = 3
    print("I{0: 7.2f} I{1: 7.2f} I".format(xt, y))
    xt += dx
print("+--------+--------+")
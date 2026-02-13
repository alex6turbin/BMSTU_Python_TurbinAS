from math import sqrt

x=float(input("Введите значение для x: "))
y=0.0

if x <= -8:
    y = -3
elif -8<x<-3:
    y = (3/5)*x + 9/5
elif -3<=x<3:
    y = -sqrt(9-x**2)
elif 3<=x<5:
    y = x-3
else:
    y = 3
print("X = {0:.2f} Y = {1:.2f}".format(x, y))
try:
    n = float(input("Введите n (км за день, n > 0): "))
    m = int(input("Введите m (всего км, m >= 0): "))

    if n <= 0:
        print("Ошибка: n должно быть натуральным числом.")
    elif m < 0:
        print("Ошибка: m должно быть неотрицательным числом.")
    else:
        if m == 0:
            print(0)
        else:
            days = (m + n - 1) // n
            print(f"Результат: {int(days)}")

except ValueError:
    print("Ошибка: введите целое число.")
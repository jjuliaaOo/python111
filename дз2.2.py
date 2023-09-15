import math
x, y, z = input('Введите 3 числа (в строчку с пробелами):').split()
max = 0

if x <= y and x <= z:
    print('Наименьшее из чисел:', x)
if y <= x and y <= z:
    print('Наименьшее из чисел:', y)
else:
    print('Наименьшее из чисел:', z)

import math
a = int(input("Введите год для проверки на високосноть: \n"))

if a%4 == 0 and a%100 != 0:
    print('YES')
if a%400 == 0:
    print('YES')
else:
    print('NO')

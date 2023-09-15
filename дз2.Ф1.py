n = int(input("Введите натуральное число: "))
def f(n):
    s = 0
    for i in range(1, n+1):
        s = s + i**2
    return s
    
print(f(n))

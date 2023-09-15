import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(5,5))
plt.ylim([-5, 5])

x = np.arange(-4, 0.9, 0.1)
plt.plot(x, (x**3-4)/(x-1)**3, color='k')
x = np.arange(1.1, 4, 0.1)
plt.plot(x, (x**3-4)/((x-1)**3), color='k')
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.title('график функции')

plt.grid(True)
plt.show()


a = [-2, 2]
y = [((-2)**3-4)/((-2)-1)**3, (2**3-4)/(2-1)**3]
plt.scatter(a, y, color='r')

print('Точки локальных экстремумов можно найти по графику (отмечены точками):\n-2 - точка локального минимума (min)\n2 - точка локального максимума (max)')

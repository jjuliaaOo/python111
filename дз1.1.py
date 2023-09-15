import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(5,5))


x = np.arange(-5, -0.1, 0.1)
plt.plot(x, (-x**2+3*x-1)/x, color='k')
x = np.arange(0.1, 5, 0.1)
plt.plot(x, (-x**2+3*x-1)/x, color='k')
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.title('график функции')

plt.grid(True)
plt.show()

a = [-1, 1]
y = [(-(-1)**2+3*(-1)-1)/(-1), (-(1)**2+3*1-1)/(1)]
plt.scatter(a, y, color='r')

print('Точки локальных экстремумов можно найти по графику (отмечены точками):\n-1 - точка локального минимума (min)\n1 - точка локального максимума (max)')

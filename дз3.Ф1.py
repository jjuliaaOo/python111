import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(6, 4))
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.title('график функции y = $x^2$')
plt.xlim([-11, 11])

x = np.arange(-10, 10.1, 0.1)
plt.plot(x, x**2, '--r', linewidth=2, zorder=2)

x2 = np.arange(-10, 10.1, 0.95)
plt.scatter(x2, x2**2, s=35, c='mediumblue', marker='D', linewidths=1, edgecolors="black", zorder=3)

plt.grid(True, zorder=-2)
plt.show()

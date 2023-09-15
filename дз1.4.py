import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-6, 6.1, 0.1)
plt.figure(figsize=(5, 5))
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.title('график функции')
plt.xlim([-7, 7])

plt.plot(x, np.arcsin((2*abs(x))/(1+x**2)))
plt.grid(True)
plt.show()

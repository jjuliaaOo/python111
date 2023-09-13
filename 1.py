import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-6, 6.25, 0.25)
plt.figure(figsize=(5, 5))
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.title('график')
plt.plot(x, 1.1**(-2*x)*np.sin(x))
plt.grid(True)
plt.show()

import numpy as np
import matplotlib.pyplot as plt
a = np.arange(10, 100)
plt.plot(a, np.exp((a) * np.sin(a)), 'ro')
plt.yscale('log')
plt.xlabel('a')
plt.ylabel('b = ln(exp(a * sin(a))')
plt.show()
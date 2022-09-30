import numpy as np
import matplotlib.pyplot as plt
a = np.arange(10, 100)
plt.plot(a, np.exp((a) * np.sin(a)), 'ro', label="точки")
plt.yscale('log')
plt.xlabel('ось a')
plt.ylabel('b = log(exp(a * sin(a))')
plt.title('график')
plt.legend()
plt.show()

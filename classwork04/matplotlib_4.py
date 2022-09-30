import numpy as np
import matplotlib.pyplot as plt
a = np.linspace(10, 100)
plt.plot(a, np.exp((-a) * np.sin(a)))
plt.grid(True)
plt.xlabel('a')
plt.ylabel('b = exp(-a * sin(a)')
plt.show()

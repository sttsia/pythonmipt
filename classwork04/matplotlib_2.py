import numpy as np
import matplotlib.pyplot as plt
b = np.arange(0, 100, 10)
plt.plot(b, np.sin(b) * (b ** 0.5), 'ro')
plt.grid(True)
plt.xlabel('b')
plt.ylabel('c = sin(b) * b ^ 0.5')
plt.show()

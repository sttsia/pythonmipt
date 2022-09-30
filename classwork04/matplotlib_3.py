import numpy as np
import matplotlib.pyplot as plt
n = np.linspace(10, 100)
plt.plot(n, np.exp((-n) * np.sin(n)))
plt.show()

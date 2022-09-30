import numpy as np
import matplotlib.pyplot as plt
a = np.arange(0, 100, 10)
plt.plot(a, np.sin(a) * (a ** 0.5), 'ro')
plt.show()

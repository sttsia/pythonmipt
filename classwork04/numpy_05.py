import numpy as np
a=np.array([x for x in range (1, 100)], float)
x=a[::3]
print(x.reshape(11, 3).T)
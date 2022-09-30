import numpy as np
a=np.array([x for x in range (1, 100)], float)
x=a[::3]
vec2=np.array([x for x in range (-9, 2)])
print(vec2 @ x.reshape(11, 3))

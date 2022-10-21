import numpy as np
from numpy import linalg as lag
mat1=np.random.randint(0, 64, (8, 8))
mat2=np.delete(mat1, 7, axis = 0)
mat2=np.delete(mat2, 7, axis = 1)
print(mat2, lag.det(mat2))

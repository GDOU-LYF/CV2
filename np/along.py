import numpy as np
A2=np.array([[1,2,3],[4,5,6]])

print('ndim:',A2.ndim)
print('shape:',A2.shape)
print('size:',A2.size)
print('dtype:',A2.dtype)
A2=A2.astype(float)
print('dtype:',A2.dtype)
print('itemsize:',A2.itemsize)

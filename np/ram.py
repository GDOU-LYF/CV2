import numpy as np
A=np.array([[1,2],[3,4]])
c=np.copy(A)
r=np.copy(A)
print(A)

B=A
B[0,0]=-1 #x,y操作

print(A)

B[0,1]=-1 #x,y操作
print(A)

c[:,0]=0#对 0列进行操作
print('c:\n',c)

r[0,:]=0#对 0行进行操作
print('r:\n',r)
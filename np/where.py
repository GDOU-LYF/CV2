import cv2
import numpy as np
x=np.arange(9.).reshape(3,3)
print(x)
print(np.where(x>5))
#(array([2, 2, 2]), array([0, 1, 2]))
#y,x
#(0,2),(1,2),(2,2)

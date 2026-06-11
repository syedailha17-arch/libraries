import numpy as np
#array(start:end:step)
arr=np.array([['a','b','c','k'],
              ['d','e','f','o'],
              ['g','h','i','p'],
              ['j','k','l','r']])
print(arr[0:4:2])
print(arr[:,1:4:2])
print(arr[0:2,0:3])
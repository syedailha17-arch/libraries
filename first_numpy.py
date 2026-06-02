import numpy as np

array=np.array([1])
array=array*5
print(array)
print(array.ndim)
print(array.shape)
#multidimensional arrays
arr=np.array([[['a','b','c'],['d','e','f']],[['g','h','i'],['j','k','l']]])
word=arr[1,0,2]+arr[1,1,2]+arr[1,0,1]+arr[0,0,0]
print(word)
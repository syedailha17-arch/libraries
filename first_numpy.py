import numpy as np

#multidimensional arrays
arr=np.array([[['a','b','c'],['d','e','f']],[['g','h','i'],['j','k','l']]])
word=arr[1,0,2]+arr[1,1,2]+arr[1,0,1]+arr[0,0,0]
print(word)
import numpy as np
array=np.array([1,2,3])
print(array+1)
print(array**3)
print(array-1)
print(np.sqrt(array))
#to simply round the number use round function just like sqrt in line 5.to round up use ceil and to round down use floor
print(np.pi)
scores=np.array([19,67,98,92])
scores[scores<70]=0
print(scores)

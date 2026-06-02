import numpy as np
array=np.array([[1,4,56,34,23,12,14,15,16,89,60],[3,65,34,131,56,43,16,84,72,10,9]])
teenagers=array[array<20]
print(teenagers)
#in where there are three requirements:(condn,array,replacement).where is used when we need the original shape back
adults=np.where(array>18,array,0)
print(adults)
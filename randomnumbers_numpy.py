import numpy as np
rng=np.random.default_rng(seed=1)
array=[1,2,3,4,5]
#setting seed=1 means we will get the same result twice
print(rng.integers(1,101,(2,2)))
np.random.seed(seed=1)
print(np.random.uniform(2,5,(2,2)))
rng.shuffle(array)
print(array)
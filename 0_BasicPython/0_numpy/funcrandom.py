import numpy as np

rng = np.random.default_rng(seed=1) #1 kali random saja

print(rng.integers(1, 7, size=(3,2)))
                  #start, end, row x column

print()
#random float number
np.random.seed(seed=2)
print(np.random.uniform(size=3))

print()
#shuffle an array
rendem = np.random.default_rng()
array = np.array([1, 2, 3, 4, 5])
rendem.shuffle(array)
print(array)
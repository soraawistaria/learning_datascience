import numpy as np

matrixA = np.array([[1, 2, 3], 
                  [3, 2, 1],
                  [4, 5, 2]])

matrixB = np.array([[2, 3, 4],
                    [4, 5, 3],
                    [5, 6, 1]])

for i in range(len(matrixA)):
    times = matrixA[i] * matrixB[:, i]
    print(times)
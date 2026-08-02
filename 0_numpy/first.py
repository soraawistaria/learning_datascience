import numpy as np

ti_25 = np.array(["sora", "nayla", "rita", "fitri"])

for names in ti_25:
    print(names)

print("\nMULTIDIMENSIONAL ARRAY")

matrix = np.array([[[1, 2, 3], [4, 5 ,6], [7, 8, 9]],
                  [[10, 11, 12], [13, 14, 15], [16, 17, 18]], 
                  [[19, 20, 21], [22, 23, 24], [25, 26, 27]]])

print(matrix.ndim)
print(matrix.shape)

for i in matrix:
    for j in i:
        for k in j:
            tambah = k + k
            print(f"{k} + {k} = {tambah}")

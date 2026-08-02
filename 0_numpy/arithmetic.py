import numpy as np

# perkalian vektor
vector = np.array([2, 3, 4])

print(vector * 2)

#vectorized math func

print(np.sqrt(vector))

float = np.array([3.75, 3.5, 3.8])
round = np.round(float)
round_under = np.floor(float)
round_up = np.ceil(float)
pi = np.pi

#operasi vector
print(vector + float)

#comparison operators
ipk_mhs = np.array([2.5, 2.7, 2.4, 3.5, 3.15, 3.75, 3.85])
print(ipk_mhs > 3.00) #mengembalikan nilai boolean

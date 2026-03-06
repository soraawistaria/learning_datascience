import numpy as np

ages = np.array([[15, 16, 17, 20, 24], 
                 [21, 19, 18, 18, 19]])

teenagers = ages[ages < 18]

print(teenagers)

#mempertahankan array shape
print()
teenagers = np.where(ages <= 18, ages, np.nan)
                    # boolean statement, our variables, replace with 'what'
print(teenagers)


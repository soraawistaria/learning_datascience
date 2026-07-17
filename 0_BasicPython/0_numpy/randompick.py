import numpy as np

print()
sahur = np.array(["mie", "telur", "nasi", "energen", "kurma", "kopi"])
rng = np.random.default_rng()
choice = rng.choice(sahur)
print(choice)
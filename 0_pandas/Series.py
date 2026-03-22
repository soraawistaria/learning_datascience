import pandas as pd

# score = [100, 90, 80, 50]

# series = pd.Series(score)

# print(series)
# print()

# series2 = pd.Series(score, index = ["a", "b", "c", "d"])

# print(series2.loc["b"])
# print(series.iloc[3])
# print(series[series > 50])

# print( )

# indekk = ["a", "b", "c", "d"]
# series3 = pd.Series(score, index = [indekk])
# print(series3)

# print("\n\n")

bff = ["Gladis", "Deswita", "Cherry", "Syifa", "Syafa", "Aisya", "Natasya"]
no = range(1, (len(bff) + 1))
seriesbff = pd.Series(bff, index = no)
print(seriesbff)
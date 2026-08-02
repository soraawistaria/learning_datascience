import pandas as pd

df = pd.read_csv('US_Baby_Names_1880_2024.csv')

the_most_name = df[df['count'] > 20000]

print(the_most_name)
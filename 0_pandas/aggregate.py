# set values into a single summary value
# used to summarize and analyze data

import pandas as pd

df = pd.read_csv('0_pandas/data_siswa_bb_tb.csv')

print("\n============= MEAN =============")
print(df.mean(numeric_only=True))

print("\n============= SUM =============")
print(df.sum(numeric_only=True))

print("\n============= MIN =============")
print(df.min(numeric_only=True))

print("\n============= MAX =============")
print(df.max(numeric_only=True))

#tes
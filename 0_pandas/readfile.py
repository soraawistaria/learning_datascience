import pandas as pd

df = pd.read_csv("0_pandas/biodata.csv")



df = df.drop('No Whatsapp', axis=1)
df = df.drop('NIM', axis=1)
df = df.drop('Timestamp', axis=1)
df = df.drop('Agama', axis=1)

for call in df['Nama Panggilan']:
    call.capitalize()


print(df.to_string()) #menampilkan semua data
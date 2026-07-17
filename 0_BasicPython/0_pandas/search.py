import pandas as pd

df = pd.read_csv('spotify_wrapped_2025_top50_songs.csv', index_col="artist")

singer = input("Add artist: ")

try:
    print(df.loc[singer])
except:
    print(f"{singer} doesn't exist")
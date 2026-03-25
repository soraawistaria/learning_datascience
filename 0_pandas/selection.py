import pandas as pd

df = pd.read_csv('0_pandas\spotify_wrapped_2025_top50_songs.csv')

print(df[['song_title', 'artist']].to_string)
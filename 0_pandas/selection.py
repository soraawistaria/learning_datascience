import pandas as pd

df = pd.read_csv('spotify_wrapped_2025_top50_songs.csv')

print(df[['song_title', 'artist']].to_string)
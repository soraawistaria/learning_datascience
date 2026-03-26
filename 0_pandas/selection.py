import pandas as pd

df = pd.read_csv('spotify_wrapped_2025_top50_songs.csv')

# print(df[['song_title', 'artist']].to_string)


# selection by row

dff = pd.read_csv('spotify_wrapped_2025_top50_songs.csv', index_col='artist')  #sehingga indexnya bukan 0-habis, tapi nama artist jadi indexnya. mempermudah pencarian

print(dff.loc["Sabrina Carpenter"])

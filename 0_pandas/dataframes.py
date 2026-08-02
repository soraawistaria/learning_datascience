import pandas as pd

data = {"Name": ["Gladis", "Deswita", "Cherry", "Syifa", "Syafa", "Aisya", "Natasya"],
        "Since": [2018, 2018, 2019, 2019, 2019, 2019, 2023]}

df = pd.DataFrame(data)

# New Column
df["From"] = ["SD", "SD", "Insta", "SMP", "SMP", "SMP", "SMA"]

# New row
row8 = pd.DataFrame([{"Name": "Titi", "Since": 2025, "From": "Friends"}], index=[7])
df = pd.concat([df, row8])
print(df)
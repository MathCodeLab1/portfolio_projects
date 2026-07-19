

import pandas as pd

# create a dataframe

data = {"Name": ["Anna", "Ben", "Cara"], 
        "Sales": [120, 200, 150]
        }

df = pd.DataFrame(data)

df["Bonus"] = [10, 20, 15]

df["Total_pay"] = df["Sales"] + df["Bonus"]

print(df)

print(df["Sales"].mean())
print(df["Sales"].max())
print(df["Sales"].sum())

print(df[df["Sales"] > 150])

print(df[df["Total_pay"] > 160])

print(df.sort_values(by="Sales"))
print(df.describe())











import pandas as pd

df = pd.read_csv("sales2.csv")

df["Total_pay"] = df["Sales"] + df["Bonus"]

print(df)

print(df.loc[df["Sales"].idxmax()]) # Top performer overall

print(df.loc[df.groupby("Department")["Sales"].idxmax()]) # Top performer per department

print(df.groupby("Department")["Sales"].sum()) # Total sales per department

print(df.groupby("Region")["Total_pay"].mean()) # Average pay per region

print(df.sort_values(by="Sales", ascending=False).head(3)) # Top 3 employees overall

print(df.groupby("Region")["Sales"].sum()) # Best region(by total sales)

print(df.groupby("Department")["Sales"].mean()) # Department with highest average sales


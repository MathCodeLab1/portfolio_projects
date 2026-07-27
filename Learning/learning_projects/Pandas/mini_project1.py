import pandas as pd

# Create a csv file

df = pd.read_csv("sales.csv")

df["Department"] = ["HR", "IT", "HR", "IT", "HR"]


df["Total_pay"] = df["Sales"] + df["Bonus"]

df = df.sort_values(by="Sales", ascending=False)
df["Rank"] = range(1, len(df)+1)


print(df)
print(df["Sales"].mean())
print(df["Sales"].max())
print(df["Sales"].sum())

print(df[df["Sales"] > 150]) # sales greater than 150

print(df.groupby("Department")["Sales"].sum()) # sum of sales per department

print(df[df["Total_pay"] > 160]) # Total_pay greater than 160

print(df.groupby("Department")["Total_pay"].mean()) # Average Total_pay per department

print(df.loc[df.groupby("Department")["Sales"].idxmax()]) # top employee per department

print(df.groupby("Department")["Sales"].sum().sort_values(ascending=False)) # sort department by performance

print(df.sort_values(by="Sales", ascending=False).head(2)) # Top 2 employees overall


print(df.describe())




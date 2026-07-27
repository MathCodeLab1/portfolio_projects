

import pandas as pd

df = pd.read_csv("messy_sales.csv")


print( "=== Detect missing values ===" )
print(df.isnull().sum())

print("\n=== Fill missing values with 0: ===") 
df["Sales"] = df["Sales"].fillna(0) 
df["Bonus"] = df["Bonus"].fillna(0)
print(df)

print("\n=== Remove duplicates ===") 
df = df.drop_duplicates()
print(df)

print ("\n=== Remove extra spaces ===") 
df["Name"] = df["Name"].str.strip()
print(df)

print("\n=== Fix capitalization ===") 
df["Name"] = df["Name"].str.title()
print(df)

print("\n=== Create Total_pay ===")
df["Total_pay"] = df["Sales"] + df["Bonus"]
print(df)

print("\n=== Top performer ===")
print(df.loc[df["Sales"].idxmax()])

print("\n=== Total sales by department ===")
print(df.groupby("Department")["Sales"].sum())

print("\n=== Employees with 0 sales ===")
print(df[df["Sales"] == 0])

print("\n=== Average pay per department ===")
print(df.groupby("Department")["Total_pay"].mean())







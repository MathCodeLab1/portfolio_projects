
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../Pandas/sales2.csv")

# BAR CHART
dept_sales = df.groupby("Department")["Sales"].sum()

dept_sales.plot(kind = "bar")

plt.title("Total Sales by Department")
plt.xlabel("Department")
plt.ylabel("Sales")

plt.show()

# LINE CHART
df["Sales"].plot(kind="line")
plt.title("Sales Trend")
plt.xlabel("Employee")
plt.ylabel("Sales")

plt.show()

# HISTOGRAM
df["Sales"].plot(kind="hist")

plt.title("Sales Distibution")
plt.xlabel("Sales")

plt.show()
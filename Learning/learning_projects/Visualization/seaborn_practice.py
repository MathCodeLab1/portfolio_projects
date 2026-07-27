
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../Pandas/sales2.csv")

# Bar Plot
sns.barplot(data=df, x="Department", y="Sales")

plt.title("Department Sales")

plt.show()

# Box Plot
sns.boxplot(data=df, x="Department", y="Sales")

plt.title("Sales Spread by Department")

plt.show()

# Scatter Plot
sns.scatterplot(data=df, x="Bonus", y="Sales")

plt.title("Bonus vs Sales")

plt.show()

# Correlation / compare relationship between numbers

df["Total_pay"] = df["Sales"] + df["Bonus"]

correlation = df[["Sales", "Bonus", "Total_pay"]].corr()

sns.heatmap(correlation, annot=True)

plt.title("Correlation Heatmap")

plt.show()

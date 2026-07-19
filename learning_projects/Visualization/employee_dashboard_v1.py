
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../pandas/sales2.csv")

print(df.head())

print("\n=== Business Question #1 ===")

dept_sales = df.groupby("Department")["Sales"].sum() # Which department sells the most?

print(dept_sales)

print("\n=== Create Chart: ===")

sns.barplot(x=dept_sales.index, y=dept_sales.values)

plt.title("Total Sales by Department")
plt.show()

print("""
    Business Insight #1: 
    IT is the highest-performing department with total sales of 540.
    Sales department follows with 430, While HR generated 360.
     """)


print("\n=== Business Question #2 === ")

top_employee = df.loc[df["Sales"].idxmax()] # Who is the best employee?

print(top_employee)

print("Top Employee:", top_employee["Name"])

print("""
    Business Insight #2:
    Frank is the top-performing employee with sales of 220.
     """)


print("\n=== Business Question #3 ===") # Which region generates the most sales?

region_sales = df.groupby("Region")["Sales"].sum()

print(region_sales)

print("\n=== Chart ===")

sns.barplot("x=region_sales.index, y=region_sales.values")
plt.title("Sales by Region")
plt.show()

print("""
    Business Insight #3:
    East region generated the highest sales.
    South followed as the second strongest region.
    North had moderate performance.
    West generated the lowest sales.
     """)


print("\n=== Business Question #4 ===")

avg_sales = df.groupby("Department")["Sales"].mean() # Which department performs best on average?

print(avg_sales)

print("\n=== Chart ===")

sns.barplot("x=avg_Sales.index, y=avg_Sales.values")
plt.title("Average Sales by Department")
plt.show()

print("""
    Business Insight #4:
    IT department has a lower average total pay.
    HR department has a lower average pay compared to IT.
    This indicates IT employees are compensated more on average.
     """)


print("\n=== Business Question #5 ===") # Relationship Analysis

sns.scatterplot(data=df, x="Bonus", y="Sales") # Do bigger bonuses lead to bigger sales?

plt.title("Bonus vs Sales")
plt.show()

print(""" 
    Business Insight #5: 
    Employees with larger bonuses generally tend to have higher sales. 
     """)

print("\n=== FINAL BUSINESS REPORT ===")

print("""
    1. IT generated the highest total sales.
    2. Frank was the top-performing employee.
    3. East region generated the most sales.
    4. Sales department had the highest average sales.
    5. Higher bonuses generally correspond to higher sales.
     """ )
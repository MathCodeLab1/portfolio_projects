
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("regional_sales.csv")

df["total_pay"] = df["Sales"] + df["Bonus"]

print(df.head())

print("\n=== Business Question #1 ===")

dept_sales = df.groupby("Department")["Sales"].sum() # Which department generates the most sales?

print(dept_sales)

sns.barplot(x=dept_sales.index,
            y=dept_sales.values)

plt.title("Total Sales by Department")
plt.show()

print("\nBusiness Insight #1:")

print("""
Sales generated the highest total sales 1150.
IT follows with 940.
HR generated 700.
Marketing generated the lowest sales at 650.
""")


print("\n=== Business Question #2 ===")

top_employee = df.loc[df["Sales"].idxmax()] # Who is the top-performing employee?

print(top_employee)

print(f"\nTop Employee: {top_employee['Name']}")

print(f"\n{top_employee['Name']} generated the highest sales"
      f"with {top_employee['Sales']}")

print("\nBusiness Insight #2:")

print("""
Steve was the top-performing employee with sales of 250.
This indicates that Steve contributed the most individual sales in the company.
""")


print("\n=== Business Question #3 ===")

region_sales = df.groupby("Region")["Sales"].sum()

print(region_sales)


print("\nBusiness Insight #3:")

print("""
East region generated the highest sales with 1310.
South followed with 950.
West generated 640.
North generated the lowest sales with 540.
""")

print("\n=== Business Question #4 ===")

avg_sales = df.groupby("Department")["Sales"].mean() # Which department has the highest average sales per employee?

print(avg_sales)


print("\n=== Chart ===")

sns.barplot(
    x=avg_sales.index,
    y=avg_sales.values
)

plt.title("Average Sales by Department")

plt.show()

print("\nBusiness Insight #4:")

print("""
Sales department has the highest average sales per employee at 230.
IT follows with an average of 188.
Marketing averaged 162.5.
HR had the lowest average sales at 116.67.   
""")


print("\n=== Business Question #5 ===")

correlation = df[["Sales", "Bonus"]].corr()

print(correlation)


print("\n=== Chart ===")

sns.scatterplot(data=df, x="Bonus", y="Sales")

plt.title("Bonus vs Sales")

plt.show()

print("""
Business Insight #5:
      
Employees with larger bonuses generally tend to have higher sales.
""")

print("\n=== FINAL BUSINESS REPORT ===")

print("""
1. Sales department generated the highest total sales.
2. Steve was the top-performing employee.
3. East region generated the highest sales.
4. Sales department had the highest average sales per employee.
5. Higher bonuses generally correspond to higher sales.
""")


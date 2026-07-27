
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("messy_company_sales.csv")

print(df.head())

print("\n=== Missing Values ===")
print(df.isnull().sum())

print("\n=== Clean Missing Values ===")
df["Sales"] = df["Sales"].fillna(0)
df["Bonus"] = df["Bonus"].fillna(0)
print(df)


print("\n=== Remove Duplicates ===")
df = df.drop_duplicates()
print(df)

print("\n=== Clean Names ===")
df["Name"] = df["Name"].str.strip()
df["Name"] = df["Name"].str.title()
print(df)

print("\n=== Create Total Pay ===")
df["Total_pay"] = df["Sales"] + df["Bonus"]
print(df)

print("\n=== Cleaned Dataset ===")
print(df.head())

print("\nRemaining Missing Values:")
print(df.isnull().sum())


print("\n=== Business Question #1 ===")

dept_sales = df.groupby("Department")["Sales"].sum() # Which department generated the most sales?

print(dept_sales)

print("\nChart:")

sns.barplot(x=dept_sales.index,
            y=dept_sales.values
)

plt.title("Total Sales by Department")

plt.show()

print("\nInsight #1:")
print("""
    Sales department generated the highest total sales(1150).
    IT followed with 750,Marketing generated 650,and
    HR generated the lowest total sales at 550.
     """)


print("\n=== Business Question #2 ===")

top_employee = df.loc[df["Sales"].idxmax()] # Who is the top-performing employee?

print(top_employee)


print("\nInsight #2:")
print(f"\nTop Employee:{top_employee['Name']}")

print("\nInsight #2:")
print("""
    Steve was the top-performing employee with sales of 250,making him the
    highest individual contributor in the company.
     """)


print("\n=== Business Question #3 ===")

region_sales = df.groupby("Region")["Sales"].sum()

print(region_sales)


print("\nChart:")

sns.barplot(x=region_sales.index,
            y=region_sales.values
)

plt.title("Sales by Region")

plt.show()


print("\nInsight #3:")
print("""
    East region generated the highest sales(1310).South was second with 760,
    while North generated the lowest sales at 390.  
      """)


print("\n=== Business Question #4 ===")

avg_sales = df.groupby("Department")["Sales"].mean()

print(avg_sales)

print("\nInsight #4:")
print("""
    Sales department had the highest average sales per employee(230).
    Marketing averaged 162.5,IT averaged 150,and HR had the lowest average sales at 91.67.
      """)

print("\n=== Business Question #5 ===")

print(df[["Sales", "Bonus"]].corr())

print("\nScatter plot:")

sns.scatterplot(data=df,
                x="Bonus",
                y="Sales"
)

plt.title("Bonus vs Sales")

plt.show()

print("\nInsight #5:")
print("""
    There is a moderate positive relationship between bonuses and sales.
    Employees with higher bonuses tend to have higher sales,but the relationship
    is not as strong as in project 2.
      """)


print("\n=== FINAL BUSINESS REPORT ===")

print("""
    1. Sales department generated the highest total sales(1150).
    2. Steve was the top-performing employee with sales of 250.
    3. East region generated the highest sales(1310).
    4. Sales department had the highest average sales per employee(230).
    5. Bonus and sales show a moderate positive relationship(correlation = 0.51).
    
      """)






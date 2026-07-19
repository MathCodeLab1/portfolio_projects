


import pandas as pd

employees = pd.read_csv("employees.csv") # Load both datasets
budget = pd.read_csv("budget.csv")

df = pd.merge(employees, budget, on="Department") # merge the datasets

sales = df.groupby("Department")["Sales"].sum() # compare sales vs budgets
budgets = budget.set_index("Department")["Budget"]

comparison = pd.DataFrame({"Sales": sales, "Budgets": budgets})

print(comparison) 

print(employees) 
print(budget)
print(df)
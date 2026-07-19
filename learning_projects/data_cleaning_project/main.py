

import pandas as pd
from load import load_data
from cleaning import clean_data

# 1. Load data


df = load_data("data/students_scores.csv")

print("Original data:")
print(df)

# 2. Clean data
df_clean = clean_data(df)

print("\nCleaned data:")
print(df_clean)
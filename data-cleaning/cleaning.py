import pandas as pd

# 1. Load the CSV
df = pd.read_csv("students_scores.csv")
print("=== ORIGINAL DATA ===")
print(df)

print("\n=== CHECK FOR DUPLICATES ===")
print(df.duplicated())
print("\nTotal duplicates:", df.duplicated().sum())

df = df.drop_duplicates()
print("\n=== AFTER REMOVING DUPLICATES ===")
print(df)

print("\n=== MISSING VALUES ===")
print(df.isna().sum())

print("\n=== AVERAGE SCORE PER STUDENT ===")
avg_per_student = df.groupby("student")["score"].mean()
print(avg_per_student)

print("\n=== AVERAGE SCORE PER SUBJECT ===")
avg_per_subject = df.groupby("subject")["score"].mean()
print(avg_per_subject)

print("\n=== TOP STUDENTS (SORTED) ===")
print(avg_per_student.sort_values(ascending=False))

print("\n=== MEDIAN SCORE PER SUBJECT ===")
median_per_subject = df.groupby("subject")["score"].median()
print(median_per_subject)

print("\n=== STANDARD DEVIATION PER SUBJECT ===")
std_per_subject = df.groupby("subject")["score"].std()
print(std_per_subject)

print("\n=== SUMMARY TABLE ===")
summary = pd.DataFrame({
    "mean": df.groupby("subject")["score"].mean(),
    "median": df.groupby("subject")["score"].median(),
    "std": df.groupby("subject")["score"].std()
})
print(summary)

print("\n=== OUTLIER DETECTION (IQR METHOD) ===")

Q1 = df["score"].quantile(0.25)
Q3 = df["score"].quantile(0.75)
IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

print(f"Lower limit: {lower_limit}")
print(f"Upper limit: {upper_limit}")

outliers = df[(df["score"] < lower_limit) | (df["score"] > upper_limit)]
print("\nOutliers found:")
print(outliers)

def dutch_grade(score):
    if score >= 8.5:
        return "Excellent"
    elif score >= 7.0:
        return "Good"
    elif score >= 6.0:
        return "Sufficient"
    else:
        return "Insufficient"

df["grade"] = df["score"].apply(dutch_grade)

df.to_csv("students_scores_cleaned.csv", index=False)
print("\n=== CLEANED FILE SAVED AS students_scores_cleaned.csv ===")

print("\n=== FINAL SUMMARY REPORT ===")
print("Number of rows:", len(df))
print("Columns:", list(df.columns))
print("\nAverage score per subject:")
print(df.groupby("subject")["score"].mean())
print("\nAverage score per student:")
print(df.groupby("student")["score"].mean().sort_values(ascending=False))

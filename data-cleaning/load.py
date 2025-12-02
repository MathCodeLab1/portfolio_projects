import pandas as pd
#load a csv file with students score to a dataframe
df = pd.read_csv("students_scores.csv")

# function with dutch grade
def dutch_grade(score):
    if score >= 8.5:
        return "Excellent"
    elif score >= 7.0:
        return "Good"
    elif score >= 6.0:
        return "Sufficient"
    else:
        return "Insufficient"
# use a function to add extra column by converting score to dutch grade    
df["grade"] = df["score"].apply(dutch_grade)

#print the first 10 rows
print(df.head(10))
import pandas as pd

df = pd.read_csv("students.csv")

# 1. First 5 rows
print("First 5 rows:\n")
print(df.head())

# 2. Shape & Data Types
print("\nShape (rows, columns):", df.shape)

print("\nData Types:\n")
print(df.dtypes)

# 3. Summary Statistics
print("\nSummary Statistics:\n")
print(df.describe())

# 4. Pass/Fail Count
print("\nPass/Fail Count:\n")
print(df["passed"].value_counts())

# 5. Average scores (Pass vs Fail)

subjects = ["math", "science", "english", "history", "pe"]

print("\nAverage Scores (Pass Students):")
print(df[df["passed"] == 1][subjects].mean())

print("\nAverage Scores (Fail Students):")
print(df[df["passed"] == 0][subjects].mean())

# 6. Highest Average Student

df["avg_score"] = df[subjects].mean(axis=1)

top_student = df.loc[df["avg_score"].idxmax()]

print("\nTop Student:")
print(top_student["name"], "-", round(top_student["avg_score"], 2))
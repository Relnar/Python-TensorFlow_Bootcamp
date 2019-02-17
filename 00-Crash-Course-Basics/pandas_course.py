import pandas as pd
import os

print(os.getcwd())
df = pd.read_csv("./00-Crash-Course-Basics/salaries.csv")
print(df)
print(df["Salary"])
print(df[["Salary", "Name"]])
print(df["Salary"].max())
print(df.describe())
print(df["Salary"] > 60000)
print(df[df["Salary"] > 60000])
print(df.as_matrix())
import pandas as pd

# Load dataset
df = pd.read_csv("data.csv")

print("Dataset:")
print(df)

# Identify missing values
print("\nMissing values using isnull():")
print(df.isnull())

print("\nNon-missing values using notnull():")
print(df.notnull())

# Total missing values in each column
print("\nTotal missing values in each column:")
print(df.isnull().sum())
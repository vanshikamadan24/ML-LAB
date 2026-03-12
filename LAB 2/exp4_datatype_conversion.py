import pandas as pd

# Load dataset
df = pd.read_csv("data.csv")

print("Original Data Types:")
print(df.dtypes)

# Convert columns
df["Age"] = df["Age"].astype(float)
df["Marks"] = df["Marks"].astype(int)

print("\nUpdated Data Types:")
print(df.dtypes)
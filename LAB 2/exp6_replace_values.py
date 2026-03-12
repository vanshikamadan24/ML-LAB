import pandas as pd

# Load dataset
df = pd.read_csv("data.csv")

print("Original Data:")
print(df)

# Replace incorrect values
df.replace({"Male": "M", "Female": "F"}, inplace=True)

print("\nCorrected Data:")
print(df)
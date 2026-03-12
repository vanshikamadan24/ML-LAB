import pandas as pd

# Load dataset
df = pd.read_csv("data.csv")

# Replace numerical missing values with mean
df.fillna(df.mean(numeric_only=True), inplace=True)

# Replace categorical missing values
df.fillna("Unknown", inplace=True)

print("Dataset after replacing missing values:")
print(df)
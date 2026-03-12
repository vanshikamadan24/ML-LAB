import pandas as pd

# Load dataset
df = pd.read_csv("data.csv")

# Display dataset information
print("Dataset Info:")
print(df.info())

# Number of rows and columns
print("\nShape of dataset:", df.shape)

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())
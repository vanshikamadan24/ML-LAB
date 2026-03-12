import pandas as pd

# Load dataset
df = pd.read_csv("data.csv")

print("Original Columns:")
print(df.columns)

# Rename columns
df.rename(columns={
    "Name": "Student_Name",
    "Marks": "Student_Marks"
}, inplace=True)

print("\nUpdated DataFrame:")
print(df)
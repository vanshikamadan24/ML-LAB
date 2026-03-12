import pandas as pd

# Dictionary data
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Marks": [85, 90, 78, 92]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Student DataFrame:")
print(df)

# Display data types
print("\nData Types:")
print(df.dtypes)
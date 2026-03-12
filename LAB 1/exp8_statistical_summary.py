import pandas as pd

# Read CSV file
df = pd.read_csv("data.csv")

# Display statistical summary
print("Statistical Summary:")
print(df.describe())

print("\nInterpretation:")
print("Mean: Average value of the column")
print("Std: Standard deviation (spread of data)")
print("Min: Minimum value")
print("Max: Maximum value")
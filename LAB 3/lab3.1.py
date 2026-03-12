import pandas as pd

# Load dataset directly from GitHub raw link
url = "https://raw.githubusercontent.com/rashida048/Datasets/master/StudentsPerformance.csv"
df = pd.read_csv(url)

# Display first few rows
print("First 5 Records:")
print(df.head())

# Identify column types
print("\nDataset Info:")
print(df.info())

# Separate numerical and categorical columns
num_cols = df.select_dtypes(include=['int64','float64']).columns
cat_cols = df.select_dtypes(include=['object']).columns

print("\nNumerical Columns:", list(num_cols))
print("Categorical Columns:", list(cat_cols))

# Measures of Central Tendency
print("\nMean:\n", df[num_cols].mean())
print("\nMedian:\n", df[num_cols].median())
print("\nMode:\n", df[num_cols].mode().iloc[0])

# Measures of Dispersion
print("\nMin:\n", df[num_cols].min())
print("\nMax:\n", df[num_cols].max())
print("\nSum:\n", df[num_cols].sum())
print("\nVariance:\n", df[num_cols].var())
print("\nStandard Deviation:\n", df[num_cols].std())

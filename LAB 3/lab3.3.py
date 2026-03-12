import pandas as pd

# Load dataset
url = "https://raw.githubusercontent.com/rashida048/Datasets/master/StudentsPerformance.csv"
df = pd.read_csv(url)

# Select numerical columns
num_cols = df.select_dtypes(include=['int64','float64']).columns

# -------------------------------
# Correlation
# -------------------------------
corr_matrix = df[num_cols].corr()
print("Correlation Matrix:\n")
print(corr_matrix)

# -------------------------------
# Covariance
# -------------------------------
cov_matrix = df[num_cols].cov()
print("\nCovariance Matrix:\n")
print(cov_matrix)

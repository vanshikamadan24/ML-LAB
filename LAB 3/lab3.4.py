import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
url = "https://raw.githubusercontent.com/rashida048/Datasets/master/StudentsPerformance.csv"
df = pd.read_csv(url)

# Select numerical columns
num_cols = df.select_dtypes(include=['int64','float64']).columns

# -------------------------------
# Histograms
# -------------------------------
print("Showing Histograms...")
df[num_cols].hist(figsize=(10,6))
plt.show()

# -------------------------------
# Boxplot
# -------------------------------
print("Showing Boxplot...")
df[num_cols].plot(kind='box', figsize=(8,6))
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data.csv")

# Histogram
plt.hist(df["Marks"], bins=10)

plt.title("Distribution of Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")

plt.show()
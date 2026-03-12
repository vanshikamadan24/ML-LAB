import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data.csv")

# Boxplot
plt.boxplot(df["Marks"])

plt.title("Boxplot of Marks")

plt.show()
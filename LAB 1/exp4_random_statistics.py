import numpy as np

# Create array of 10 random integers (1–100)
arr = np.random.randint(1, 101, 10)

print("Random Array:")
print(arr)

# Find statistics
print("Minimum:", np.min(arr))
print("Maximum:", np.max(arr))
print("Mean:", np.mean(arr))
print("Sum:", np.sum(arr))
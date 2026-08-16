import numpy as np

heart_rates = np.array([72, 75, 80, 68, 90])

print("Mean:", np.mean(heart_rates))  # average value
print("Minimum:", np.min(heart_rates))
print("Maximum:", np.max(heart_rates))
print("Standard deviation:", np.std(heart_rates)) # standard deviation

group_a = np.array([78, 79, 80, 81, 82])
group_b = np.array([50, 65, 80, 95, 110])

print("A mean:", np.mean(group_a))
print("A std:", np.std(group_a))

print("B mean:", np.mean(group_b))
print("B std:", np.std(group_b))
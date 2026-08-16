import numpy as np
heart_rates = np.array([55, 75, 110, 90, 50, 120, 100])
low_mask = heart_rates < 60
high_mask = heart_rates > 100
normal_mask = (heart_rates <= 100) & (heart_rates>=60)
print(low_mask)
print(high_mask)
print(heart_rates[low_mask])
print(heart_rates[high_mask])
print(heart_rates[normal_mask])
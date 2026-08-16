import numpy as np
rr_stable = np.array([0.79, 0.81, 0.80, 0.78, 0.82])

rr_variable = np.array([0.55, 0.70, 0.80, 0.95, 1.00])
print("rr_variable:")
print(np.mean(rr_variable))
print(np.min(rr_variable))
print(np.max(rr_variable))
print(np.std(rr_variable))
print("rr_stable")
print(np.mean(rr_stable))
print(np.min(rr_stable))
print(np.max(rr_stable))
print(np.std(rr_stable))
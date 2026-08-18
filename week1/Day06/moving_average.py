import numpy as np

data = np.array([1, 2, 10, 2, 1])

window_size = 3

kernel = np.ones(window_size) / window_size

print(kernel)

smoothed_data = np.convolve(data,kernel,mode="same")

print(data)
print(smoothed_data)
import numpy as np
import matplotlib.pyplot as plt

time = np.array([0, 1, 2, 3, 4])
signal = np.array([1, 3, 1, 3, 1])

plt.plot(time, signal)
plt.title("Example Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

plt.show()
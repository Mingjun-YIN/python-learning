import numpy as np
import matplotlib.pyplot as plt

signal = np.array([0.0, 0.2, 0.5, 1.0, 0.6,0.2, 0.0, -0.2, 0.0, 0.3])

sampling_rate = 20
sampling_interval = 1 / sampling_rate
time = np.arange(signal.size) / sampling_rate
print(time.size == signal.size)
print(time)
plt.plot(time, signal)
plt.title("Sampled Biomedical Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()
plt.show()
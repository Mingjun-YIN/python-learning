import numpy as np
import matplotlib.pyplot as plt

signal_frequency = 5
duration = 1
sampling_rate = 12

time = np.arange(sampling_rate * duration) / sampling_rate
signal = np.sin(2 * np.pi * signal_frequency * time)

plt.plot(time, signal)
plt.grid()
plt.show()
import numpy as np
import matplotlib.pyplot as plt

sampling_rate = 100
duration = 2
signal_frequency = 2

time = np.arange(sampling_rate * duration) / sampling_rate
signal = np.sin(2 * np.pi * signal_frequency * time)

plt.plot(time, signal)
plt.title("2 Hz Sine Wave")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()
plt.show()
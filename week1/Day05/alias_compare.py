import numpy as np
import matplotlib.pyplot as plt

sampling_rate = 8
duration = 2

time = np.arange(sampling_rate * duration) / sampling_rate

signal_5hz = np.sin(2 * np.pi * 5 * time)
signal_alias = -np.sin(2 * np.pi * 3 * time)

print(signal_5hz)
print(signal_alias)

print(np.allclose(signal_5hz, signal_alias))

plt.plot(time, signal_5hz, marker="o")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("5 Hz Signal Sampled at 8 Hz")
plt.grid()
plt.show()
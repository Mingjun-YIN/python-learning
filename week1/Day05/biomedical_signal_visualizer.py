import numpy as np
import matplotlib.pyplot as plt

sampling_rate = 100
duration = 3
signal_frequency = 2

sampling_interval = 1 / sampling_rate
nyquist_frequency = sampling_rate / 2
samples_percycle = sampling_rate / signal_frequency

time = np.arange(sampling_rate * duration) / sampling_rate
signal = np.sin(2 * np.pi * signal_frequency * time)
high_signal = signal > 0.8

print("Number of sample:",signal.size)
print("Sample interval:",sampling_interval)
print("Nyquist frequency:",nyquist_frequency)
print("Signal frequency:",signal_frequency)
print("Sample per cycle",samples_percycle)
print("")
print("Mean amplitude",signal.mean())
print("Minimum amplitude:",signal.min())
print("Maximum amplitude:",signal.max())
print("Standard deviation",signal.std())
print("Number of samples with amplitude > 0.8:",signal[high_signal].size)

plt.plot(time, signal)
plt.title("Signal Map")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()
plt.show()


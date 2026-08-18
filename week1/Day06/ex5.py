import numpy as np
import matplotlib.pyplot as plt

sampling_rate = 100
duration = 2

low_frequency = 3
high_frequency = 25

time = np.arange(sampling_rate * duration) / sampling_rate
low_signal = np.sin(2 * np.pi * low_frequency * time)
high_signal = 0.4 * np.sin(2 * np.pi * high_frequency * time)
mixed_signal = low_signal + high_signal

window_size = 5
kernel = np.ones(window_size) / window_size
smoothed_signal = np.convolve(mixed_signal,kernel,mode="same")

mixed_mae = np.mean(np.abs(low_signal - mixed_signal))
smoothed_mae = np.mean(np.abs(low_signal - smoothed_signal))
print("Mixed MAE:", mixed_mae)
print("Smoothed MAE:", smoothed_mae)
print("Filtering improved:",smoothed_mae < mixed_mae)

plt.plot(time, low_signal, label="Original 3 Hz")
plt.plot(time, mixed_signal, label="3 Hz + 25 Hz")
plt.plot(time, smoothed_signal, label="Smoothed")

plt.title("Frequency Components and Smoothing")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()
plt.legend()

plt.show()
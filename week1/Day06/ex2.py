import numpy as np
import matplotlib.pyplot as plt

sampling_rate = 100
duration = 2
signal_frequency = 3

time = np.arange(sampling_rate * duration) / sampling_rate
clean_signal = np.sin(2 * np.pi * signal_frequency * time)
noise = np.random.normal(0,0.3,time.size)
noisy_signal = clean_signal + noise

weindow_size = 5
kernel = np.ones(weindow_size) / weindow_size
smoothed_signal = np.convolve(noisy_signal,kernel,mode="same")

print("Noisy size:", noisy_signal.size)
print("Smoothed size:", smoothed_signal.size)
print("Same size:",noisy_signal.size == smoothed_signal.size)

noisy_error = np.mean(np.abs(clean_signal - noisy_signal))
smoothed_error = np.mean(np.abs(clean_signal - smoothed_signal))

print("Noisy MAE:", noisy_error)
print("Smoothed MAE:", smoothed_error)
print("Smoothing improved:",smoothed_error < noisy_error)

plt.plot(time, noisy_signal, label="Noisy")
plt.plot(time, smoothed_signal, label="Smoothed")
plt.title("Moving Average Smoothing")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()
plt.legend()
plt.show()
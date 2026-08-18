import numpy as np
import matplotlib.pyplot as plt

sampling_rate = 100
duration = 3
signal_frequency = 3
interference_frequency = 25
noise_std = 0.2
window_size = 5

time = np.arange(sampling_rate * duration) / sampling_rate
clean_signal = np.sin(2 * np.pi * signal_frequency * time)
interference = 0.3 * np.sin(2 * np.pi * interference_frequency * time)
noise = np.random.normal(0,noise_std,time.size)
measured_signal = noise + interference + clean_signal
kernel = np.ones(window_size) / window_size
smoothed_signal = np.convolve(measured_signal,kernel,mode="same")

original_error = measured_signal - clean_signal
smoothed_error = smoothed_signal - clean_signal

print("Number of samples:", measured_signal.size)
print("Sampling interval:",1 / sampling_rate,"s")
print("Measured MAE:",np.mean(np.abs(clean_signal - measured_signal)))
print("Filtered MAE:",np.mean(np.abs(clean_signal - smoothed_signal)))
print("Measured error std:", np.std(original_error))
print("Filtered error std:", np.std(smoothed_error))
print("Filtering improved:", np.mean(np.abs(clean_signal - smoothed_signal)) < np.mean(np.abs(clean_signal - measured_signal)))

plt.plot(time, clean_signal, label="Clean Signal")
plt.plot(time, measured_signal, label="Measured Signal")
plt.plot(time, smoothed_signal, label="Filtered Signal")
plt.title("final task")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()
plt.legend()
plt.show()
import numpy as np
import matplotlib.pyplot as plt

sampling_rate = 100 
duration = 4 
signal_frequency = 2 
clean_amplitude = 1.0
interference_frequency = 20 
interference_amplitude = 0.3
noise_std = 0.2

time = np.arange(sampling_rate * duration) / sampling_rate
clean_signal = clean_amplitude * np.sin(2 * np.pi * signal_frequency * time)
interference = interference_amplitude * np.sin(2 * np.pi * interference_frequency * time)
noise = np.random.normal(0, noise_std, time.size)
measured_signal = clean_signal + interference + noise

print("Number of samples:",measured_signal.size)
print("Sample interval:",1 / sampling_rate, "s")
print("Nyquist frecquency:",sampling_rate / 2)
print("Mean:",np.mean(measured_signal))
print("Min:",np.min(measured_signal))
print("Max:",np.max(measured_signal))
print("Std:",np.std(measured_signal))
print("")

boolean_mask = measured_signal > 1
print("Measured signal > 1",measured_signal[boolean_mask])
print("The number of measured signal > 1:",np.sum(boolean_mask))
print("")

window_size = 5
kernel = np.ones(window_size) / window_size
filtered_signal = np.convolve(measured_signal,kernel,mode="same")
print("If all signal have same size:",time.size == clean_signal.size == measured_signal.size == filtered_signal.size)
print("")

measured_mae = np.mean(np.abs(clean_signal - measured_signal))
filtered_mae = np.mean(np.abs(clean_signal - filtered_signal))
print("Measured MAE:",measured_mae)
print("Filtered MAE:",filtered_mae)
print("If filtering improved:",filtered_mae < measured_mae)
print("Measured error std:",np.std(measured_signal - clean_signal))
print("Filtered error std:",np.std(filtered_signal - clean_signal))

plt.plot(time, clean_signal,label="Clean signal")
plt.plot(time, measured_signal,label="Measured signal")
plt.plot(time, filtered_signal,label="Filtered signal")
plt.title("Week 1 Biomedical Signal Processing")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()
plt.legend()
plt.show()
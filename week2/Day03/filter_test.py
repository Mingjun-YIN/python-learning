import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sci

sampling_rate = 250 
duration = 5 
useful_signal_frequency = 5 
baseline_wander_frequency = 0.2 
high_frequency = 50

time = np.arange(sampling_rate * duration) / sampling_rate
useful_signal = 1 * np.sin(2 * np.pi * useful_signal_frequency * time)
baseline_wander = 0.5 * np.sin(2 * np.pi * baseline_wander_frequency * time)
high_frequency_signal = 0.2 * np.sin(2 * np.pi * high_frequency * time)
measured_signal = useful_signal + baseline_wander + high_frequency_signal

high_pass_cutoff = 0.5
low_pass_cutoff = 20
order = 4
b,a = sci.butter(order,high_pass_cutoff,btype="highpass",fs=sampling_rate)
c,d = sci.butter(order,low_pass_cutoff,btype="lowpass",fs=sampling_rate)
high_pass_filtered_signal = sci.filtfilt(b,a,measured_signal)
band_pass_filtered_signal = sci.filtfilt(c,d,high_pass_filtered_signal)

measured_mae = np.mean(np.abs(useful_signal - measured_signal))
filtered_mae = np.mean(np.abs(useful_signal - band_pass_filtered_signal))
std_measured_error = np.std(useful_signal - measured_signal)
std_filtered_error = np.std(useful_signal - band_pass_filtered_signal)

print("Measured MAE/Error:",measured_mae,"/",std_measured_error)
print("Filtered MAE/Error:",filtered_mae,"/",std_filtered_error)


plt.plot(time,useful_signal,label="Useful Signal")
plt.plot(time,measured_signal,label="Measured Signal")
plt.plot(time,band_pass_filtered_signal,label="Filtered Signal")
plt.title("Filter Test")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()
plt.legend()
plt.show()
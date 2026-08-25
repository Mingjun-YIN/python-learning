import numpy as np
import matplotlib.pyplot as plt

sampling_rate = 250
duration = 5

time = np.arange(sampling_rate * duration) / sampling_rate
ecg = 0.05 * np.sin(2 * np.pi * 1 * time)
r_peaks = np.array([100,300,550,725,975,1175])
ecg[r_peaks] = 1.2

plt.plot(time, ecg)
plt.scatter(time[r_peaks],ecg[r_peaks])
plt.title("ECG with R Peaks")
plt.xlabel("Time (s)")
plt.ylabel("ECG Amplitude")
plt.grid()
plt.show()
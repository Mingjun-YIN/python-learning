import numpy as np
from scipy.signal import find_peaks
import matplotlib.pyplot as plt


sampling_rate = 250
duration = 5


time = np.arange(sampling_rate * duration) / sampling_rate
ecg = 0.05 * np.sin(2*np.pi*1*time)
r_positions = np.array([100,300,550,750,1000])

ecg[r_positions] = 1.2

peaks, properties = find_peaks(ecg,height = 0.8,distance = 100)

print("Detected peaks:", peaks)

plt.plot(time, ecg)
plt.scatter(time[peaks], ecg[peaks])
plt.xlabel("Time(s)")
plt.ylabel("ECG amplitude")
plt.grid()
plt.show()
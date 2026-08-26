import numpy as np
from scipy.signal import find_peaks
import matplotlib.pyplot as plt

sampling_rate = 250
duration = 10
# time axis
time = np.arange(sampling_rate * duration) / sampling_rate
# create ECG-like signal
ecg = 0.05 * np.sin(2*np.pi*1*time)
r_positions = np.array([100,300,550,750,1000,1250,1500,1750,2100])
ecg[r_positions] = 1.2

# detect R peaks
peaks, properties = find_peaks(ecg,height=0.8,distance=100)


# convert index to time
r_times = peaks / sampling_rate
rr_intervals = np.diff(r_times)
heart_rates = 60 / rr_intervals

print("R peaks:", peaks)
print("R times:", r_times)
print("RR intervals:", rr_intervals)
print("Heart rates:", heart_rates)
print("Average HR:", np.mean(heart_rates))

plt.plot(time, ecg)
plt.scatter(r_times, ecg[peaks])
plt.xlabel("Time(s)")
plt.ylabel("ECG")
plt.grid()
plt.show()
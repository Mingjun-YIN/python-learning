import numpy as np
import matplotlib.pyplot as plt

sampling_rate = 250
r_peaks = np.array([100,300,550,725,975,1175])

r_peak_times = r_peaks / sampling_rate
rr_samples = np.diff(r_peaks)
rr_intervals = rr_samples / sampling_rate
heart_rates = 60 / rr_intervals
hr_times = r_peak_times[1:]

print("R peak indices:",r_peaks)
print("R peak times:",r_peak_times)
print("RR intervals:",rr_intervals)
print("Heart rates:",heart_rates)
print("HR times",hr_times)
print("Average HR:",np.mean(heart_rates))
print("Minimum HR:",np.min(heart_rates))
print("Maximum HR:",np.max(heart_rates))
print("HR std:",np.std(heart_rates))

plt.plot(hr_times, heart_rates, marker="o")
plt.title("Instantaneous Heart Rate")
plt.xlabel("Time (s)")
plt.ylabel("Heart Rate (bpm)")
plt.grid()
plt.show()
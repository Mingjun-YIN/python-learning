import numpy as np

sampling_rate = 250
r_peaks = np.array([100,300,550,750])
rr_samples = np.diff(r_peaks)
rr_intervals = rr_samples / sampling_rate
hr_rates = 60 / rr_intervals

print("R peaks:", r_peaks)
print("RR differences in samples:", rr_samples)
print("RR intervals in seconds", rr_intervals)
print("Heart rates", hr_rates)
print("Average HR:",np.mean(hr_rates))
print("Minimum HR:",np.min(hr_rates))
print("Maximum HR:",np.max(hr_rates))
print("Number of RR intervals",rr_samples.size)
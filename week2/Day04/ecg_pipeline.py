import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sci
from preprocessing import bandpass_filter
from peak_detection import peak_detect
from hr_calculation import hr_calculate

sampling_rate = 250
duration = 10
clean_frequency = 1
baseline_wander_frequency = 0.2
interference_frequency = 50
r_peak = np.array([150, 350, 550, 760, 960, 1160, 1370, 1570, 1770, 1980, 2180])

time = np.arange(sampling_rate * duration) / sampling_rate
r_times = r_peak / sampling_rate
clean_signal = 0.05 * np.sin(2 * np.pi * clean_frequency * time)
clean_signal[r_peak] = 1.2
baseline_wander = 0.3 * np.sin(2 * np.pi * baseline_wander_frequency * time)
interference = 0.15 * np.sin(2 * np.pi * interference_frequency * time)
raw_ecg = clean_signal + baseline_wander + interference

filtered_signal = bandpass_filter(raw_ecg,sampling_rate)

raw_peaks,raw_properties = peak_detect(raw_ecg)
filtered_peaks,flitered_properties = peak_detect(filtered_signal)

print("True R peaks:",r_peak)
print("Raw detected peaks:",raw_peaks)
print("Filtered detected peaks:",filtered_peaks)
print("Raw ECG Maximum:",np.max(raw_ecg))
print("Filtered ECG Maximum",np.max(filtered_signal))

edge_margin_seconds = 0.2
raw_hr_rates = hr_calculate(edge_margin_seconds,r_peak,raw_ecg,sampling_rate)
detected_hr_rates = hr_calculate(edge_margin_seconds,filtered_peaks,filtered_signal,sampling_rate)

print("HR Rate")
print("True HR Rates:",raw_hr_rates)
print("Detected HR Rates:",detected_hr_rates)

plt.plot(time,raw_ecg,label="Measured Signal")
plt.plot(time,filtered_signal,label="Filtered Signal")
plt.scatter(r_times, raw_ecg[r_peak])
plt.title("ECG pipeline")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()
plt.legend()
plt.show()

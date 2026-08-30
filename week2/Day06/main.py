import numpy as np
import scipy.signal as sci
import matplotlib.pyplot as plt
from evaluation import evaluate_peaks
from peak_detection import peak_detect
from preprocessing import bandpass_filter 
from preprocessing import edg_process
from wave_creator import sin_wave_creat
from wave_creator import add_r_waves
from hr_calculation import hr_calculate

sampling_rate = 250 
duration = 10 
clean_signal_frequency = 1
clean_amplitude = 0.05
r_peaks = np.array([150,350,550,760,960,1160,1370,1570,1770,1980,2180])

time = np.arange(sampling_rate * duration) / sampling_rate
clean_signal = add_r_waves(sin_wave_creat(clean_signal_frequency,clean_amplitude,time),time,r_peaks,sampling_rate)
baseline_wander = sin_wave_creat(0.2,0.3,time)
interference = sin_wave_creat(50,0.15,time)
np.random.seed(42)
noise = np.random.normal(0,0.1,time.size)
raw_ecg = clean_signal + baseline_wander + interference + noise
filtered_signal = bandpass_filter(raw_ecg,sampling_rate)

filtered_peak,filtered_properties = peak_detect(filtered_signal)
valid_filtered_peaks = edg_process(filtered_signal,filtered_peak,sampling_rate=sampling_rate)

true_hr_rates = hr_calculate(sampling_rate=sampling_rate,r_peak=r_peaks)
filtered_hr_rates = hr_calculate(sampling_rate,valid_filtered_peaks)
tp,fp,fn,precision,recall,f1 = evaluate_peaks(r_peaks,valid_filtered_peaks,sampling_rate)

peak_times = valid_filtered_peaks / sampling_rate
hr_times = peak_times[1:]

print("True R peaks:",r_peaks)
print("Detected R peaks:",valid_filtered_peaks)
print("")
print("Heart rates:",filtered_hr_rates)
print("Average HR:",np.mean(filtered_hr_rates))
print("Minimum HR:",np.min(filtered_hr_rates))
print("Maximum HR:",np.max(filtered_hr_rates))
print("")
print("TP:",tp)
print("FP:",fp)
print("FN:",fn)
print("Precision:",precision)
print("Recall:",recall)
print("F1:",f1)

'''
plt.plot(time, clean_signal)
'''
plt.figure()
plt.plot(hr_times,filtered_hr_rates,marker="o")
plt.title("Instantaneous Heart Rate")
plt.xlabel("Time (s)")
plt.ylabel("Heart Rate (bpm)")
plt.grid()
plt.show()

plt.figure()
plt.plot(time,filtered_signal)
plt.scatter(peak_times,filtered_signal[valid_filtered_peaks])
plt.title("Filtered ECG with Detected R Peaks")
plt.xlabel("Time (s)")
plt.ylabel("ECG Amplitude")
plt.grid()
plt.show()

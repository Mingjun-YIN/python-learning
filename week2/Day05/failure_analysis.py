import numpy as np
import scipy.signal as sci
from wave_creator import sin_wave_creat
from preprocessing import bandpass_filter
from preprocessing import edg_process
from evaluation import evaluate_peaks
from peak_detection import peak_detect

sampling_rate = 250 
duration = 10 
clean_signal_frequency = 1
clean_amplitude = 0.05
r_peak = np.array([150,350,550,760,960,1160,1370,1570,1770,1980,2180])
baseline_wander_frequency = 0.2
baseline_amplitude = 0.3
interference_frequency = 50
interference_amplitude = 0.15
noise_std = 0.3
edge_margin = 0.2 
height_ratios = np.array([0.3, 0.4, 0.5, 0.6, 0.7])

time = np.arange(sampling_rate * duration) / sampling_rate
clean_signal = sin_wave_creat(clean_signal_frequency,clean_amplitude,time)
clean_signal[r_peak] = 1.2
baseline_wander = sin_wave_creat(baseline_wander_frequency,baseline_amplitude,time)
interference = sin_wave_creat(interference_frequency,interference_amplitude,time)
np.random.seed(42)
base_noise = np.random.normal(0,1,time.size)

for height_ratio in height_ratios:
    measured_signal = clean_signal + baseline_wander + interference + noise_std * base_noise
    filtered_signal = bandpass_filter(measured_signal,sampling_rate)
    detected_peaks,detected_properties,height_threshold = peak_detect(filtered_signal,height_ratio)
    clean_r_peak,clean_properties,clean_height= peak_detect(clean_signal,height_ratio)
    valid_clean_r_peak = edg_process(time,r_peak,sampling_rate)
    valid_filtered_r_peak = edg_process(time,detected_peaks,sampling_rate)
    tp,fp,fn,precision,recall = evaluate_peaks(valid_clean_r_peak,valid_filtered_r_peak,sampling_rate)
    if precision == 0 and recall == 0:
        f1 = 0
    else:
        f1 = f1 = 2 * precision * recall / (precision + recall)

    print("Height Ratio:",height_ratio)
    print("Height threshold:",height_threshold)
#print("Detected peaks:",detected_peaks)
    print("TP:",tp)
    print("FP:",fp)
    print("FN:",fn)
    print("Precision:",precision)
    print("Recall:",recall)
    print("F1:",f1)
    print("")
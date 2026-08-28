import numpy as np
import scipy.signal as sci

def bandpass_filter(signal,sampling_rate,order=4,low_cutoff=0.5,high_cutoff=20):
    a,b=sci.butter(order,[low_cutoff,high_cutoff],btype="bandpass",fs=sampling_rate)
    filtered_signal = sci.filtfilt(a,b,signal)
    return filtered_signal

def edg_process(signal,rpeak,sampling_rate,edge_margin_seconds=0.2):
    edge_margin_samples = edge_margin_seconds * sampling_rate
    valid_r_peak = (edge_margin_samples <  rpeak) & (rpeak < np.size(signal) - edge_margin_samples)
    return rpeak[valid_r_peak]
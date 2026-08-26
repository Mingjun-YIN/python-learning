import numpy as np
import scipy.signal as sci

def bandpass_filter(signal,sampling_rate,low_cutoff=0.5,high_cutoff=20,order=4):
    a,b=sci.butter(order,[low_cutoff,high_cutoff],btype="bandpass",fs=sampling_rate)
    filtered_signal = sci.filtfilt(a,b,signal)
    return filtered_signal
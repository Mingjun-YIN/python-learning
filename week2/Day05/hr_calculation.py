import numpy as np
import scipy.signal as sci

def hr_calculate(signal,sampling_rate,r_peak,edge_margin_seconds):
    edge_margin_samples = edge_margin_seconds * sampling_rate
    valid_r_peak = (edge_margin_samples <  r_peak) & (r_peak < np.size(signal) - edge_margin_samples)
    rr_intervals = np.diff(r_peak[valid_r_peak]) / sampling_rate
    hr_rates = 60 / rr_intervals
    return hr_rates
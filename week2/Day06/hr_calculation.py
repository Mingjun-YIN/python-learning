import numpy as np
import scipy.signal as sci

def hr_calculate(sampling_rate,r_peak):
    rr_intervals = np.diff(r_peak) / sampling_rate
    hr_rates = 60 / rr_intervals
    return hr_rates
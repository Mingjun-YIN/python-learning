import numpy as np
import scipy.signal as sci

def peak_detect(signal,distance=100):
    height = 0.6 * np.max(signal)
    peak,properties = sci.find_peaks(signal,height=height,distance=distance)
    return peak,properties

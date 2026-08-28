import numpy as np
import scipy.signal as sci

def peak_detect(signal,height_ratio=0.6,distance=100):
    height = height_ratio * np.max(signal)
    peak,properties = sci.find_peaks(signal,height=height,distance=distance)
    return peak,properties,height

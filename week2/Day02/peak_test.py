import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks


x = np.array([0,1,0,2,0,3,0])


peaks, properties = find_peaks(x)

print("Peak indices:", peaks)
print("Peak values:", x[peaks])
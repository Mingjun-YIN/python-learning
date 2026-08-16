import numpy as np
import matplotlib.pyplot as plt

signal = np.array([0.1,0.3,0.8,1.2,0.7,0.2,-0.1,-0.3])
time = np.arange(0,0.8,0.1)
print(time)
print(signal)
print(signal.size)
print(time.size)
print(signal.size == time.size)
plt.plot(time,signal)
plt.title("Simplified Biomedical Signal")
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")
plt.grid()
plt.show()
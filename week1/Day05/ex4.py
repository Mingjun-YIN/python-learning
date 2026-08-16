import numpy as np
import matplotlib.pyplot as plt

sampling_rate = 100 
duration = 3 
signal_frequency = 3 

time = np.arange(sampling_rate * duration) / sampling_rate
signal = np.sin(2 * np.pi * signal_frequency * time)

print(time.size)
print(signal.size)
print(time.size == signal.size)

plt.plot(time, signal)
plt.title("sine wave")
plt.xlabel("time (s)")
plt.ylabel("Amplitude")
plt.grid()
plt.show()
import numpy as np
import matplotlib.pyplot as plt

sampling_rate = 100 
duration = 2
signal_frequency = 3
noise_mean = 0
noise_std = 0.4

time = np.arange(sampling_rate * duration) / sampling_rate
clean_signal = np.sin(2 * np.pi * signal_frequency * time)
noise = np.random.normal(0,0.4,time.size)
noisy_signal = clean_signal + noise

print("Number of samples:",time.size)
print("Clean signal mean/std:",clean_signal.mean(),"/",clean_signal.std())
print("Noise mean/std:",noise.mean(), "/", noise.std())
print("Noisy signal mean/std:", noisy_signal.mean(), "/", noisy_signal.std())

plt.plot(time,noisy_signal)
plt.title("Noisy 3 Hz Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()
plt.show()
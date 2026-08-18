import numpy as np
import matplotlib.pyplot as plt

sampling_rate = 100
duration = 3
signal_frequency = 2

time = np.arange(sampling_rate * duration) / sampling_rate

clean_signal = np.sin(2 * np.pi * signal_frequency * time)

noise = np.random.normal(0,0.3,time.size)

noisy_signal = clean_signal + noise
print("Clean size:", clean_signal.size)
print("Noise size:", noise.size)
print("Noisy size:", noisy_signal.size)

print("Same size:",clean_signal.size == noise.size == noisy_signal.size)
plt.plot(time, noisy_signal)

plt.title("Noisy Biomedical Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()

plt.show()
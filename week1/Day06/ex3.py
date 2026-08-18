import numpy as np
import matplotlib.pyplot as plt

sampling_rate = 100 
duration = 2 
signal_frequency = 3 
noise_std = 0.3

time = np.arange(sampling_rate * duration) / sampling_rate
clean_signal = np.sin(2 * np.pi * signal_frequency * time)
noise = np.random.normal(0,noise_std,time.size)
noisy_signal = clean_signal + noise

window_size = [3, 5, 15]
kernel1 = np.ones(window_size[0])/window_size[0]
kernel2 = np.ones(window_size[1])/window_size[1]
kernel3 = np.ones(window_size[2])/window_size[2]
smoothed_signal1 = np.convolve(noisy_signal,kernel1,mode="same")
smoothed_signal2 = np.convolve(noisy_signal,kernel2,mode="same")
smoothed_signal3 = np.convolve(noisy_signal,kernel3,mode="same")

print("Noisy MAE:", np.mean(np.abs(clean_signal - noisy_signal)))
print("Window 3 MAE:", np.mean(np.abs(clean_signal - smoothed_signal1)))
print("Window 5 MAE:",np.mean(np.abs(clean_signal - smoothed_signal2)))
print("Window 15 MAE:",np.mean(np.abs(clean_signal - smoothed_signal3)))

plt.plot(time,clean_signal,label = "Clean Signal")
plt.plot(time,noisy_signal,label = "Noisy Signal")
plt.plot(time,smoothed_signal2,label = "Smooth Signal")
plt.title("Three Signals")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()
plt.legend()
plt.show()
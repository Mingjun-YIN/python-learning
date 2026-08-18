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
window_size = 5
kernel = np.ones(window_size)/window_size
smoothed_signal = np.convolve(noisy_signal,kernel,mode="same")

original_error = noisy_signal - clean_signal
smoothed_error = smoothed_signal - clean_signal

print("Noisy MAE",np.mean(np.abs(clean_signal - noisy_signal)))
print("Smoothed MAE",np.mean(np.abs(clean_signal - smoothed_signal)))
print("Original error std:", np.std(original_error))
print("Smoothed error std:", np.std(smoothed_error))

smoothed_clean = np.convolve(clean_signal,kernel,mode="same")
distortion = smoothed_clean - clean_signal

print("Filter distortion MAE:",np.mean(np.abs(distortion)))
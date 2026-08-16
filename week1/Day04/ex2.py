import numpy as np

ecg_samples = np.array([0.1, 0.3, 0.8, 1.2, 0.7, 0.2, -0.1, -0.3])
print(ecg_samples)
print(ecg_samples.size)
print(ecg_samples.shape)
print(ecg_samples.dtype)
print(ecg_samples[0])
print(ecg_samples[3])
print(ecg_samples[1:4])
print(ecg_samples[:3])
print(ecg_samples[4:])
print(ecg_samples[::2])
import wfdb
import numpy as np
import matplotlib.pyplot as plt

record=wfdb.rdrecord("100",pn_dir = "mitdb")

print(record.fs)
print(record.sig_len)
print(record.n_sig)
print(record.sig_name)
print(record.p_signal.shape)
ecg_signal = record.p_signal[:,0]
print(ecg_signal.shape)

duration = 5
sample_count = duration * record.fs

time = np.arange(record.fs * duration)/record.fs
signal = ecg_signal[:sample_count]

print(time.size)
print(signal.size)

plt.plot(time,signal)
plt.title("Real ECG - Record 100 - MLII")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()
plt.show()

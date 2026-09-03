import wfdb
import numpy as np
import matplotlib.pyplot as plt

whole_annotation = wfdb.rdann("100",extension="atr",pn_dir="mitdb")
record=wfdb.rdrecord("100",pn_dir = "mitdb")

ecg_signal = record.p_signal[:,0]
duration = 8
sample_count = duration * record.fs
time = np.arange(record.fs * duration)/record.fs
signal = ecg_signal[:sample_count]
whole_symbols = np.array(whole_annotation.symbol)

time_mask = whole_annotation.sample < sample_count
normal_mask = np.isin(whole_symbols,["N","A","V"])
reference_mask = time_mask & normal_mask
reference_samples = whole_annotation.sample[reference_mask]
reference_times = reference_samples / record.fs
reference_symbols = whole_symbols[reference_mask]
print("Reference samples:",reference_samples)
print("Reference symbols:",reference_symbols)

symbols_categories,symbols_count = np.unique(whole_annotation.symbol,return_counts=True)
print("Symbols Classes:",symbols_categories)
print("The count of symbols:",symbols_count)
'''
plt.plot(time,signal)
plt.scatter(reference_times,signal[reference_samples],label="Reference beats")
plt.title("Record 100 MLII - Reference Beat Annotations")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()
plt.show()
'''
import numpy as np
import scipy.signal as sci
def evaluate_peaks(true_peaks,detected_peaks,sampling_rate,tolerance_seconds=0.05):
    tolerance_samples = tolerance_seconds * sampling_rate
    matched = np.zeros(detected_peaks.size,dtype=bool)
    tp = 0
    fn = 0
    for true_peak in true_peaks:
        matched_this_peak = False
        for index,detected_peak in enumerate(detected_peaks):
            if matched[index] == False and np.abs(detected_peak - true_peak) <= tolerance_samples:
                matched[index] = True
                tp += 1
                matched_this_peak = True
                break
        if not matched_this_peak:
            fn += 1
    fp = detected_peaks.size - tp
    if tp == 0:
        precision = 0
        recall = 0
    else:
        precision = tp / (tp + fp)
        recall = tp / (tp + fn)
    return tp,fp,fn,precision,recall

#test
true_peaks = np.array([100, 300, 500])
detected_peaks = np.array([102, 295, 700])
tp,fp,fn,precision,recall = evaluate_peaks(true_peaks,detected_peaks,sampling_rate=200)
print(tp,fp,fn,precision,recall)
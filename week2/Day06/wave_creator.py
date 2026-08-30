import numpy as np

def sin_wave_creat(frequency,amplitude,time):
    wave = amplitude * np.sin(2 * np.pi * frequency * time)
    return wave

def add_r_waves(signal,time,r_positions,sampling_rate,amplitude=1.2,width_seconds=0.04):
    time_r_peaks = r_positions / sampling_rate
    sigma = width_seconds / 4
    final_signal = signal
    for time_r_peak in time_r_peaks:
        mask = np.abs(time - time_r_peak) <= width_seconds / 2
        pluse = amplitude * np.exp(-((time-time_r_peak)**2)/(2*(sigma**2)))
        for i in np.arange(time.size):
            if mask[i] == False:
                pluse[i] = 0
        final_signal = final_signal + pluse
    return final_signal


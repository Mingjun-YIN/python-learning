import numpy as np

def sin_wave_creat(frequency,amplitude,time):
    wave = amplitude * np.sin(2 * np.pi * frequency * time)
    return wave
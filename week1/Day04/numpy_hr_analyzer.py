import numpy as np
rr_intervals = np.array([0.8,0.6,1.2,0.75,1.0,0.5,1.1,0.9])
hr_intervals = 60 / rr_intervals
print("RR intervals: ",rr_intervals)
print("HR intervals: ",hr_intervals)
print("Statistics")
print("Mean HR: ",round(np.mean(hr_intervals),2))
print("Min HR: ",np.min(hr_intervals))
print("Max HR: ",np.max(hr_intervals))
print("Std HR: ",np.std(hr_intervals))
print("Measurements: ",hr_intervals.size)
print("Classification")
low_mask = hr_intervals < 60
high_mask = hr_intervals > 100
normal_mask = (hr_intervals <= 100) & (hr_intervals >= 60)
outside_range_mask = low_mask | high_mask
print("Low HR: ",hr_intervals[low_mask])
print("High HR: ",hr_intervals[high_mask])
print("Normal HR: ",hr_intervals[normal_mask])
print("Outside HR: ",hr_intervals[outside_range_mask])
print("Low count: ",np.sum(low_mask))
print("High count: ",np.sum(high_mask))
print("Normal count: ",np.sum(normal_mask))
print("Outside count: ",np.sum(outside_range_mask))
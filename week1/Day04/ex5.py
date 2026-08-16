import numpy as np

heart_rates = np.array([55, 75, 110, 90, 50, 120, 100, 80, 45, 105])
low_mask = heart_rates < 60
high_mask = heart_rates > 100
normal_mask = (heart_rates <= 100) & (heart_rates >= 60)
outside_mask = low_mask | high_mask
low_heart_rates = heart_rates[low_mask]
high_heart_rates = heart_rates[high_mask]
normal_heart_rates = heart_rates[normal_mask]
outside_heart_rates = heart_rates[outside_mask]
print("All HR: ",heart_rates)
print("Low HR: ",low_heart_rates)
print("High HR: ",high_heart_rates)
print("Outside-range HR: ",outside_heart_rates)
print("Low count: ",np.sum(low_mask))
print("High count: ",np.sum(high_mask))
print("Normal count: ",np.sum(normal_mask))
print("Outside count: ",np.sum(outside_mask))
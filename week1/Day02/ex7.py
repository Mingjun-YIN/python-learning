rr_intervals = [0.8, 0.75, 1.0, 0.6, 1.2]
heart_rates = []
for rr_interval in rr_intervals:
    heart_rate = 60 / rr_interval
    heart_rates.append(heart_rate)
print(heart_rates)
print(len(heart_rates))
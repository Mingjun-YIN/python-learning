rr_intervals = [0.8, 0.6, 1.2, 0.75, 1.0, 0.5, 1.1]
heart_rates = []
high_count = 0
low_count = 0
normal_count = 0
for rr_interval in rr_intervals:
    heart_rate = 60 / rr_interval
    heart_rates.append(heart_rate)
    if heart_rate < 60:
        statu = "Low"
        low_count += 1
    elif heart_rate > 100:
        statu = "High"
        high_count += 1
    else:
        statu = "Normal"
        normal_count += 1
    print("RR:",rr_interval," | HR:",heart_rate," | Status:",statu)
print("Average HR:", sum(heart_rates)/len(heart_rates))
print("Maximum HR:", max(heart_rates))
print("Minimum HR:", min(heart_rates))
print("Measurements:", len(heart_rates))
print("Low:", low_count)
print("Normal:", normal_count)
print("High:", high_count)
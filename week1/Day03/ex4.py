def calculate_hr(rr_interval):
    heart_rate = 60 / rr_interval
    return heart_rate
def classify_hr(heart_rate):
    if heart_rate < 60:
        status = "Low"
    elif heart_rate <= 100:
        status = "Normal"
    else:
        status = "High"
    return status
rr_intervals = [0.8, 0.6, 1.2, 0.75, 1.0, 0.5]
heart_rates = []
for rr_interval in rr_intervals:
    heart_rate = calculate_hr(rr_interval)
    heart_rates.append(heart_rate)
    status = classify_hr(heart_rate)
    print("RR:",rr_interval," | HR:",round(heart_rate,2)," | Status:",status)
print("Average HR:",round(sum(heart_rates)/len(heart_rates),2))
print("Maximum HR:",max(heart_rates))
print("Minimum HR:",min(heart_rates))
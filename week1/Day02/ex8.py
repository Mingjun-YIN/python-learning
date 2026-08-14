rr_intervals = [0.8, 0.6, 1.2, 0.75, 1.0]
for rr_interval in rr_intervals:
    heart_rate = 60/rr_interval
    if heart_rate < 60:
        statu = "Low"
    elif heart_rate > 100:
        statu = "High"
    else:
        statu = "Normal"
    print("RR:",rr_interval,"HR:",heart_rate,"Status:",statu)
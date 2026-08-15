def classify_hr(heart_rate):
    if heart_rate < 60:
        return "Low"
    elif heart_rate <= 100:
        return "Normal"
    else:
        return "High"
heart_rates = [50,60,75,100,120]
for heart_rate in heart_rates:
    status = classify_hr(heart_rate)
    print("HR:",heart_rate,"status: ",status)
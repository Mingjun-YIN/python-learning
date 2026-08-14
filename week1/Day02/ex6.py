heart_rates = [55, 75, 110, 90, 50]
high_count = 0
for heart_rate in heart_rates:
    if heart_rate < 60:
        print("Heart rate:",heart_rate,"Status: Low")
    elif heart_rate > 100:
        high_count = high_count + 1
        print("Heart rate:",heart_rate,"Status: High")
    else:
        print("Heart rate:",heart_rate,"Status: Normal")
print("Number of high rates:",high_count)
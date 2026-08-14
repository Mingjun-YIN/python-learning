heart_rates = [72, 75, 80, 68, 90]
print(sum(heart_rates))
print(min(heart_rates))
print(max(heart_rates))
average_hr = sum(heart_rates)/len(heart_rates)
print(average_hr)
heart_rates.append(100)
average_hr2 = sum(heart_rates)/len(heart_rates)
print(average_hr2)
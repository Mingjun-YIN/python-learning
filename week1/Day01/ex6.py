rr_interval = float(input("Enter RR interval (s):"))
temperature = float(input("Enter temperature (C):"))
heart_rate = 60/rr_interval
print("Heart rate:",heart_rate)
print("Temperature:",temperature)
if heart_rate < 60:
    heart_rate_statu = "Low"
    hs = False
elif heart_rate > 100:
    heart_rate_statu = "High"
    hs = False
else:
    heart_rate_statu = "Normal"
    hs = True
print("Heart rate status: ",heart_rate_statu)
if temperature < 36:
    temperature_status = "Low"
    ts = False
elif temperature > 37.5:
    temperature_status = "High"
    ts = False
else:
    temperature_status = "Normal"
    ts = True
print("Temperature status: ",temperature_status)
if ts and hs:
    print("Overall status: All values are in range.")
else:
    print("Overall status: At least one value is outside the range.")
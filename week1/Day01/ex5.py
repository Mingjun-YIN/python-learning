heart_rate = float(input("Enter heart rate (bpm):"))
temperature = float(input("Enter temperature (C):"))
if 60 <= heart_rate <= 100:
    hr_in_range = True
else:
    hr_in_range = False
if 36 <= temperature <= 37.5:
    temp_in_range = True
else:
    temp_in_range = False
if hr_in_range and temp_in_range:
    print("All values are in range.")
else:
    print("At least one value is outside the range.")
if hr_in_range == False:
    print("Heart rate is outside the range.")
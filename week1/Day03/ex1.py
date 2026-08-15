def show_vital_sign(name,value):
    print(name, value)
show_vital_sign("Heart rate:", 75)
show_vital_sign("Temperature:", 36.8)
show_vital_sign("Sp02:",98)
def calculate_hr(rr_interval):
    heart_rate = 60 / rr_interval
    print(heart_rate)
calculate_hr(0.8)
calculate_hr(0.6)
calculate_hr(1.2)
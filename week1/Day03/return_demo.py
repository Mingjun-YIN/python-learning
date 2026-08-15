def calculate_hr_print(rr_interval):
    heart_rate = 60 / rr_interval
    print(heart_rate)
    
def calculate_hr_return(rr_interval):
    heart_rate = 60 / rr_interval
    return heart_rate

a = calculate_hr_print(0.8)
b = calculate_hr_return(0.8)

print("a =", a)
print("b =", b)
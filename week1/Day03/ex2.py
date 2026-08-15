def calculate_bmi(weight,hight):
    bmi = weight / (hight ** 2)
    return bmi
bmi = calculate_bmi(70, 1.75)
print("BMI: ",bmi)
if bmi < 18.5:
    statu = "Underweight"
elif 18.5 <= bmi < 25:
    statu = "Normal"
elif 25 <= bmi < 30:
    statu = "Overweight"
else:
    statu = "Obesity"
print(statu)
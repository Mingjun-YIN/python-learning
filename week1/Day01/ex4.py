weight = float(input("Enter weight (kg):"))
height = float(input("Enter height (m):"))
height_squared = height ** 2
bmi = weight/height_squared
print("BMI:", round(bmi,2))
if bmi < 18.5:
     Category = "Underweight"
elif 18.5 <= bmi < 25:
    Category = "Normal"
elif 25 <= bmi < 30:
    Category = "Overweight"
else:
    Category = "Obesity"
print("Category:",Category)
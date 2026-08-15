def classify_bmi(bmi):
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obesity"
    return category
def caculate_bmi(weight,hight):
    bmi = weight / (hight ** 2)
    return bmi
weights_heights = [(50,1.75),(70,1.75),(80,1.75),(100,1.75)]
for (weight,hight) in weights_heights:
    bmi = caculate_bmi(weight,hight)
    category = classify_bmi(bmi)
    print("BMI:", round(bmi,2))
    print("Category:",category)
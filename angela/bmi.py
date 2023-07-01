height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")


BMI = int(weight) / float(height) ** 2
bmi_as_int = int(BMI)
print(bmi_as_int)


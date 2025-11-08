weight = float(input("Enter your weight in kilogram :"))
height = float(input("Enter your height in meter :"))

bmi= weight/(height ** 2)

print ("You BMI is :",bmi)
if bmi<18.5:
    print("You are Under Weight")
elif bmi>=18.5 and bmi<=24.9:
    print("You are Healthy")
elif bmi>=25 and bmi<=29.9:
    print("You are Overweight")
elif bmi>=30 and bmi<=34.5:
    print("You are Obese (Class 1)")
elif bmi>=35 and bmi<=39.9:
    print("You are Obese(Class 2) ")
elif bmi>=40:
    print("You are Obese(Class 3) ")
else:
    print("Please enter valid numeric values for weight and height")

weight = int(input("Enter your weight:"))
height = float(input("Enter yout height:"))
bmi = int(weight / height ** 2)
bmi_status = ""
if bmi < 18.5 :
    bmi_status = "underweight"
elif bmi > 18.5 and bmi < 25:
    bmi_status = "normal weight"
elif bmi > 25 and bmi < 30:
    bmi_status = "overweight"
elif bmi > 30 and bmi < 35:
    bmi_status = "obese"
elif bmi > 35 :
    bmi_status = "clinically obese"
print("Your BMI is: " +  str(bmi) + ", you are " + bmi_status)

print("WELCOME TO BMI CALCULATOR")

weight = float(input("Please enter your weight in kg's: "))
height = float(input("Please enter your height in metres: "))

# formula to calculate bmi
bmi = int(weight) / float(height) ** 2
print("Your exact bmi: ")
print(bmi)

# print bmi as whole number
bmi_as_int = int(bmi)
print("Your bmi in whole numbers: ")
print(bmi_as_int)
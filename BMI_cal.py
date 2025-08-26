# BMI Calculator with Age & Gender

print(" --- BMI Calculator ---")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
gender = input("Enter your gender (male/female): ").lower()
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

print("\n--- BMI Report ---")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Gender: {gender.capitalize()}")
print(f"Your BMI is: {round(bmi, 2)}")

if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 24.9:
    category = "Normal weight"
elif 25 <= bmi < 29.9:
    category = "Overweight"
else:
    category = "Obese"

print("Category:", category)

if age < 18:
    print("Note: BMI may not be fully accurate for children/teens.")
elif gender == "male":
    print("Tip: For men, staying active helps maintain healthy BMI.")
elif gender == "female":
    print("Tip: For women, maintaining balanced diet is very important.")

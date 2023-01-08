ht = float(input("Height (CM)?:\t"))
wt = float(input("Weight (KG)?:\t"))

# BMI Formula Calculation
BMI = lambda h, w: round((w/(h*h)) * 10000, 3)

bmi = BMI(ht, wt)

print(f"Your {bmi = }")
if bmi <= 18.5:
    print("Underweight")
elif bmi <= 24.9:
    print("Normal Weight")
elif bmi <= 29.9:
    print("Overweight")
else:
    print("Obese")

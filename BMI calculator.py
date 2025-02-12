print("Welcome to the BMI calculator!")
height=1.65
weight=84
BMI=(weight/height**2)
print(BMI)
if BMI<18.5:
  print("underweight")
elif 18.5 <= BMI <= 24.9:
  print("normal weight")
else:
  print("overweight")
  

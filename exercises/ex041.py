# Classify a swimmer by its age

age = int(input("Type the swimmer's age: "))
classification: str
if age <= 14:
  classification = "junior swimming"
elif age <= 17:
  classification = "youth swimming"
else:
  classification = "master or senior swimming"

print(f"With the age of {age}, he belongs to the {classification} group.")
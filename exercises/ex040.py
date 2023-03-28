# Calculate the mean of a student grade

grade1 = float(input("Type the first grade: "))
grade2 = float(input("Type the second grade: "))

mean = (grade1 + grade2) / 2

print(f"your mean is {mean}")
if mean >= 6:
  print("Congratulations, you're approved!")
elif mean >= 4.5:
  print(f"You will need to go to remedial classes.")
else:
  print("You're failed the school year.")
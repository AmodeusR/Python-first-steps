
# Determine which number of 2 is greater or if both are equal

number1 = int(input("Type a number: "))
number2 = int(input("Type another number: "))

if number1 > number2:
  print("The first number is greater")
elif number1 < number2:
  print("The second number is greater")
else:
  print("Both numbers are the same")
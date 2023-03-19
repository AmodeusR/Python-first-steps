# Get input from user. print the double, triple and square root of the input

number = int(input("Insert a number: "))

print(f"The double of {number} is {number * 2}")
print(f"The triple of {number} is {number * 3}")
print(f"The square root of {number} is {round(number ** (1/2), 2)}")
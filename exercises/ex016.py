# Get a value and take its integer part

from math import trunc

user_input = float(input("Type a number: "))

print(f"The integer part of {user_input} is {trunc(user_input)}")
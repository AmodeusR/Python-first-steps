# from 3 inputs, print the lowest and highest number

user_numbers = []

for i in range(3):
  user_number = input(f"Type the {i + 1}º number: ")
  user_numbers.append(user_number)

user_numbers.sort()

print(f"The lowest typed number is {user_numbers[0]}")
print(f"The highest typed number is {user_numbers[2]}")
# Parse a number specifying its ones, tens, hundreds and thousands

measurements = ["Ones", "Tens", "Hundreds", "Thousands"]


while True:
  user_number = input("Type a number to be parsed: ")
  number_length = len(user_number)
  if number_length > 4:
    print("Please, type a number with less than 5 numbers.")
  else:
    for i in range(number_length):
      print(f"{measurements[i]}: {user_number[-i - 1]}")
    break

# Based in the car speed, check if should pay or not a fine

from termcolor import colored

while True:
  user_input = input("What's the car speed?\n")
  try:
    car_speed = int(user_input)
    break
  except:
    print("You need to insert an integer number!")

fine = round(7 * (car_speed - 60), 2)

if car_speed > 60:
  print(colored(f"You exceeded the speed limit! You must pay a fine of R${fine}", "red"))
else:
  print(colored("It's all okay, you can keep driving!", "green"))

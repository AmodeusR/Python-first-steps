# Choose randomly between the user's input values

import random

choices: str = []

for i in range(4):
  user_input = input(f"Type the {i + 1}º thing: ")
  choices.append(user_input)

chosen = random.choice(choices)

print(f"{chosen} was selected.")
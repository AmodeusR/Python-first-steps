import random

print("\n")

is_not_valid_choice = True

options = {
  "1": "rock",
  "2": "paper",
  "3": "scissors"
}

player_input: str
player_choice: str

while is_not_valid_choice:
  player_input = input("Enter:\n1 for rock\n2 for paper\n3 for scissors\n")
  if player_input in options:
    player_choice = options[player_input]
    is_not_valid_choice = False
  else:
    print("\nInvalid input, try again")

computer_input = random.choice("123")
computer_choice = options[computer_input]

print(f"You've chosen {player_choice}")
print(f"Python have chosen {computer_choice}")

result = int(player_input) - int(computer_input)

if result == 0:
  print("It's a draw!")
elif result == -2 or result == 1:
  print("You've won! 🎉")
else:
  print("You've lost! 😔")
# Guess game: Guess the number python chose

import random
from termcolor import colored
from time import sleep

number_to_guess = random.randint(0, 5)

print(colored(str("-=-" * 21), "yellow"))
print(colored("Hey! Let's play a game? Try guessing the number I thought of!", "blue"))
print(colored(str("-=-" * 21), "yellow"))

guessed_number = int(input("What number did I think of?\n"))

print("That's your choice? So you...")
sleep(.8)
for dot in "...":
  print(dot)
  sleep(.8)

if number_to_guess == guessed_number:
  print(colored(f"You won! I indeed thought of the number {guessed_number}!", "green"))
else:
  print(
      colored(f"You lost! I thought of the number {number_to_guess}, not {guessed_number} :(", "red"))

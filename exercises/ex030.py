# Check if the number is even or odd

from termcolor import colored

user_number = int(input(colored("Type a number: ", "magenta")))

is_even = user_number % 2 == 0
even_or_odd: str

if is_even:
  even_or_odd = colored("even", "blue")
  print(f"The number is {even_or_odd}")
else:
  even_or_odd = colored("odd", "blue")
  print(f"The number is {even_or_odd}")

# Determine if the year inserted by the user is a leap year or not

from datetime import date
from termcolor import colored

input_year = int(
    input(colored("Type a year to be analyzed. Type 0 to analyze the current year.\n", "magenta")))

year: int

if input_year == 0:
  year = date.today().year
else:
  year = input_year

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
  print(f"{year} is a leap year.")
else:
  print(f"{year} is not a leap year.")

# Based on the year someone was born, determine:
# - Their age
# - If they need or have done his military enlistment
# - Date of when the enlistment will or happened

from datetime import date

born_year = int(input("Type the year you were born: "))
current_year = date.today().year
age = current_year - born_year
enlistment_period = 18 - age

print(f"Who was born in {born_year} is {age} years old in {current_year}")
if age < 18:
  if enlistment_period == 1:
    print(f"You should enlist in about {enlistment_period} year")
  else:
    print(f"You should enlist in about {enlistment_period} years")
  print(f"Your enlistment will happen in {born_year + 18}")
elif age == 18:
  print(f"You should enlist this year!")
else:
  if abs(enlistment_period) == 1:
    print(f"You should have enlisted {abs(enlistment_period)} year ago")
  else:
    print(f"You should have enlisted {abs(enlistment_period)} years ago")
  print(f"Your enlistment happened in {current_year + enlistment_period}")
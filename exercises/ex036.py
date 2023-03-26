# Write a program that analyzes wheter someone
# can take a loan or not for buying a house
# the installment should not exceed 30% of the person's salary. If so, it'll be denied

from termcolor import colored

house_price = float(input("Insert the price of the house: "))
person_salary = float(input("Insert your salary: "))
year_installment = int(input("Insert in how many years you want to pay the house: "))

installment = house_price / (year_installment * 12)

installment_exceeds = installment >= person_salary * .3

if installment_exceeds:
  print(f"The installment of R${installment:.2f} exceeds 30% of your salary.")
  print(colored("Loan denied".center(21, "="), "red"))
else:
  print(f"The installment of R${installment:.2f} doesn't exceed 30% of your salary.")
  print(colored("Loan granted!".center(21, "="), "blue"))
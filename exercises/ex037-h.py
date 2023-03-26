# get a number from the user and convert it to either:
# binary, octal or hexadecimal

import inquirer

number = int(input("What number do you want to convert?\n"))
question = [inquirer.List("convert", message="Select to which value you want to convert to", choices=[
                          "Binary", "Octal", "Hexadecimal"])]
answer = inquirer.prompt(question)

convert = answer

conversion_type: str
converted_value: int

if convert == "Binary":
  conversion_type = "binary"
  converted_value = str(bin(number))[2:]
elif convert == "Octal":
  conversion_type = "binary"
  converted_value = str(oct(number))[2:]
else:
  conversion_type = "binary"
  converted_value = str(hex(number))[2:]

print(f"The number {number} converted to {conversion_type} is {converted_value}")
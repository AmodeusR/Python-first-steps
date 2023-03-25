# Convert temperatures (Celsius <-> Farenheit)

import inquirer

question = [
    inquirer.List("temperature",
                  message="Which unit of temperature you want to convert from/to?",
                  choices=["From Celsius to Farenheit", "From Farenheit to Celsius"]
                  )
]

answer = inquirer.prompt(question)
temperature = float(input("Inform the temperature: "))
result: float


def calculate_temperature(to, temperature):
  if to == "farenheit":
    return round((9 * temperature / 5) + 32, 1)
  elif to == "celsius":
    return round((temperature - 32) / 9 * 5, 1)


if answer.get("temperature", "oops, something went wrong!") == "From Celsius to Farenheit":
  result = calculate_temperature("farenheit", temperature)
  print(f"{temperature}ºC in Farenheit is {result}ºF")
else:
  result = calculate_temperature("celsius", temperature)
  print(f"{temperature}ºF in Celcius is {result}ºC")

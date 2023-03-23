# Get an input from the user and do the following:
# • Get how many A letters has in the string
# • Specify the first and last position it shows up


user_input = input("Type a phrase: ").strip().lower()

parsed_string = user_input
chars_to_replace = "àá"
for char in chars_to_replace:
  parsed_string = parsed_string.replace(char, "a")

letter_a_count = parsed_string.count("a")
if letter_a_count == 1:
  print(f"The letter \"A\" occur one time")
else:
  print(f"The letter \"A\" occurs {letter_a_count} times.")
  
print(f"The first letter \"A\" occurred in the {parsed_string.find('a') + 1}º position.")
print(f"The first letter \"A\" occurred in the {parsed_string.rfind('a') + 1}º position.")

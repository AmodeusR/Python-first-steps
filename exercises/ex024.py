# Check if the first word of a string starts with the word "saint" or not

user_input = input("Type a text: ")
text = user_input.lower().strip().split()

if text[0] == "saint":
  print("The text starts with the word \"saint\"")
else:
  print("The text doesn't start with the word \"saint\"")

# Check if a text inputted by the user has the "movie" word

user_input = input("Type a text: ").lower()

# First solution

# words = user_input.split()

# for word in words:
#   if word == "movie":
#     print("The text has the word \"movie\"")
#     break
#   elif word == words[-1]:
#     print("The text doesn't have the word \"movie\"")


# Second solution

if "movie" in user_input:
  print("The text has the word \"movie\"")
else:
  print("The text doesn't have the word \"movie\"")

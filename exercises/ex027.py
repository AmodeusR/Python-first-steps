# Get the first and last words of a string

user_input = input("Type a text: ").strip()

words = user_input.split(" ")

print(f"The first word of the string is \"{words[0]}\"")
print(f"The last word of the string is \"{words[-1]}\"")

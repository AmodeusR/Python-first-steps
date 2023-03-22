# Get a user input and do the following:
# • print it in uppercase and lowercase
# • count the number of letters on string
# • count hte number of letters on the first word

user_text = input("Write a text to be parsed: ")
words = user_text.split(" ")
letters_count = len(user_text) - user_text.count(" ")
first_word_letter_count = len(words[0])

print(f"The text in uppercase is: {user_text.upper()}")
print(f"The text in lowercase is: {user_text.lower()}")
print(f"The text has at total {letters_count} letters")
print(f"The first word has {first_word_letter_count} letters")

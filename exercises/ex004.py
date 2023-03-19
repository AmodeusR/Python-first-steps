# List characteristics of input

userinput = input("Type something: ")


print(f"The primitive type of this value is {type(userinput)}")
print(f"Are there only spaces? {userinput.isspace()}")
print(f"Is it a number? {userinput.isnumeric()}")
print(f"Is it a text (alphabetic)? {userinput.isalpha()}")
print(f"Is it alphaunmeric? {userinput.isalnum()}")
print(f"Is it in uppercase? {userinput.isupper()}")
print(f"Is it in lowercase? {userinput.islower()}")
print(f"Is it capitalized? {userinput.istitle()}")
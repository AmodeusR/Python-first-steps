import math

def generate_title(title):
  print("\n" + title.center(30, "=") + "\n")

# String data type

# Literal assingment

first = "This is"
last = "a string"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# Constructor function

# if tested, the results will be the same as the above, True to the tests
pizza = str("Mozarella")

# Concatenation

fullString = first + " " + last
# print(fullString)

# fullString += "!"
# print(fullString)

# Casting number to string and vice-versa
generate_title("num to str & vice-versa")
decade = str(1980)
decade_as_number = int(decade)
print("decade")
print(type(decade))
print(decade)
print("\ndecade as number")
print(type(decade_as_number))
print(decade_as_number)

# Multiple lines
generate_title("Multiple lines")

multiline = """
This is a multiline string

Just like template literals work in javascript, I suppose
"""

print(multiline)

# Escaping special characters
# \t creates a tab, \n creates a new line. Just like C.

sentence = "\"I'm busy\", he said"
print(sentence)

# String methods
generate_title("String methods")

print(first.lower())
print(first.upper())

print(fullString.title())
print(last.capitalize())

# replaces all ocassions of "string"
print(fullString.replace("string", "text"))
print(len(fullString))

# Removes whitespace from beginning and end of a string, just like javascript trim() method.
# There's also lstrip and rstrip (left and right)
print(fullString.strip())

print("\n\n")

# Build a menu
generate_title("Menu building")

title = "menu".upper()
print(title.center(20, "="))
print("Suco".ljust(16, ".") + "R$2".rjust(4))  # left/right justify
print("Pizza".ljust(16, ".") + "R$25".rjust(4))
print("Pastel".ljust(16, ".") + "R$5".rjust(4))

# String index values

print(first[0])  # Gets first value of an array
print(first[-1])  # Gets last value of an array
print(first[1:-1])  # Gets a range of values in an array
print(first[1:])  # Gets from x position to the end of an array

# Booleans

booleanValue = True
x = bool(False)

# Numeric data types

# Integer
generate_title("Integer")

num = 100
num2 = int(50)

print(num)
print(num2)
print(type(num2))

# Float
generate_title("Float")

pi = 3.14159
another_pi = float(3.16)

print(pi)
print(another_pi)
print(type(another_pi))

# Complex type
generate_title("Complex type")

comp_value = 5+3j

print(comp_value)
print(comp_value.real)
print(comp_value.imag)

# Built-in functions for numbers

# checks absolute value (e.g. if negative, becomes positive)
print(abs(pi))

# rounds to the nearest integer
print(round(pi))

# rounds to the decimal we specify
print(round(pi, 3))

  # Math module methods
generate_title("Math module methods")

true_pi = math.pi

print(true_pi)
print(math.sqrt(true_pi))
print(math.ceil(true_pi))
print(math.floor(true_pi))

#
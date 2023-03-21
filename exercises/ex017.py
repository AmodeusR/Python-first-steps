# Calculate the hypotenuse


opposite = float(input("Type the opposite leg: "))
adjacent = float(input("Type the adjacent leg: "))

# Solution 1

# hypotenuse = round((opposite ** 2 + adjacent ** 2) ** (1 / 2), 2)
# print(f"The hypotenuse measures {hypotenuse}")


# Solution 2

from math import hypot

hypotenuse = round(hypot(opposite, adjacent), 2)
print(f"The hypotenuse measures {hypotenuse}")


# Get the lenght of 3 lines and determine
# if it's possible to make a triangle with it

from termcolor import colored

print(colored("-=-" * 6, "yellow"))
print(colored("Triangle analyzer", "yellow"))
print(colored("-=-" * 6, "yellow"))

line_lenghts = []

for i in range(3):
  line_length = float(input(f"Type the {i + 1}º Segment: "))
  line_lenghts.append(line_length)

ln1, ln2, ln3 = line_lenghts
it_can_make_a_triangle = ln1 < ln2 + ln3 and ln2 < ln3 + ln1 and ln3 < ln2 + ln1

if it_can_make_a_triangle:
  print("It is possible to make a triangle from the given line lenghts")
else:
  print("It isn't possible to make a triangle from the given line lenghts")

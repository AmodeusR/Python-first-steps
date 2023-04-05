# Triangle analyzer v2

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

is_all_equal = ln1 == ln2 == ln3
is_none_equal = ln1 != ln2 != ln3 and ln1 != ln3

if it_can_make_a_triangle:
  if is_none_equal:
    print("It makes a scalene triangle.")
  elif is_all_equal:
    print("It makes an equilateral triangle")
  else:
    print("It makes a isosceles triangle")
else:
  print("It isn't possible to make a triangle from the given line lenghts")
# Calculate the area of a wall and how much ink will need to paint it all

wall_width = float(input("Wall width: "))
wall_height = float(input("Wall height: "))
area = round(wall_width * wall_height, 3)
ink_quantity = round(area * .5, 4)
print(f"The wall has a dimension of {wall_width}x{wall_height}, its area is {area}m²")
print(f"You'll need {ink_quantity}l of paint.")
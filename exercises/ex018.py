# Calculate sine, cosine, tangent

import math

angle = float(input("Insert the desired angle: "))
radian_angle = math.radians(angle)
sine = round(math.sin(radian_angle), 2)
cosine = round(math.cos(radian_angle), 2)
tangent = round(math.tan(radian_angle), 2)

print(f"sine: {sine}")
print(f"cosine: {cosine}")
print(f"tangent: {tangent}")
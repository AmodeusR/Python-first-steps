# Calculate cost of rented car

days_used = int(input("For how many days did you rent the car?\n"))
km_traveled = float(input("How many kilometers traveled?\n"))

car_rent_price = round((days_used * 60) + (km_traveled * 0.15), 2)

print(f"The car rent to be paid is R${car_rent_price}")
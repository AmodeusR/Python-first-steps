# Calculate the price of a ticket.
# If the distance is higher than 200km, apply a discount

travel_distance = float(input("What's the travel distance in km?\n"))

price: float

price = travel_distance * .5 if travel_distance <= 200 else travel_distance * .45

print(f"The travel price will be R${price}")